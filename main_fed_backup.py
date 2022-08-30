#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6


import ssl

from utils.show import show_dict_users, show_devices_info, show_devices_partition, show_group_dataset_test
from utils.simulation import get_devices_download_latencies, get_devices_locations, get_devices_computation_latencies, \
    get_partition_lst

ssl._create_default_https_context = ssl._create_unverified_context
import pickle

import matplotlib.pyplot as plt
import copy
import numpy as np
from torchvision import datasets, transforms
import torch

from utils.sampling import mnist_iid, mnist_noniid, cifar_iid, cifar_noniid, semi_data_adjust, semi_dataset_test, \
    semi_dataset_test_adjust
from utils.options import args_parser
from utils import seed_all, get_model_info
from models.Update import LocalUpdate
from models.Nets import MLP, CNNMnist, CNNCifar
from models.Fed import FedAvg
from models.test import test_img


if __name__ == '__main__':
    # 测试gpu是否可用
    if torch.cuda.is_available():
        print("GPU可用")
    else:
        print("GPU不可用")
    # parse args
    args = args_parser()
    args.device = torch.device('cuda:{}'.format(args.gpu) if torch.cuda.is_available() and args.gpu != -1 else 'cpu')

    # 固定随机性
    seed_all(args.seed)

    # load dataset and split users
    # dict_users : { 用户序号 ： 数据集序号集合 }
    if args.dataset == 'mnist':
        trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        dataset_train = datasets.MNIST('../data/mnist/', train=True, download=True, transform=trans_mnist)
        dataset_test = datasets.MNIST('../data/mnist/', train=False, download=True, transform=trans_mnist)
        args.data_num = len(dataset_train)
        # sample users
        if args.iid or args.cyclic_non_iid:  # cyclic_non_iid需要首先用iid，后续再操作
            dict_users = mnist_iid(dataset_train, args)
        else:
            dict_users = mnist_noniid(dataset_train, args)
    elif args.dataset == 'cifar':
        trans_cifar = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10('../data/cifar', train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10('../data/cifar', train=False, download=True, transform=trans_cifar)
        args.data_num = len(dataset_train)
        if args.iid or args.cyclic_non_iid:  # cyclic_non_iid需要首先用iid，后续再操作
            dict_users = cifar_iid(dataset_train, args)
        else:
            dict_users = cifar_noniid(dataset_train, args)
    else:
        exit('Error: unrecognized dataset')
    img_size = dataset_train[0][0].shape

    # 固定随机性
    seed_all(args.seed)

    # build model
    if args.model == 'cnn' and args.dataset == 'cifar':
        net_glob = CNNCifar(args=args).to(args.device)
    elif args.model == 'cnn' and args.dataset == 'mnist':
        net_glob = CNNMnist(args=args).to(args.device)
    elif args.model == 'mlp':
        len_in = 1
        for x in img_size:
            len_in *= x
        net_glob = MLP(dim_in=len_in, dim_hidden=200, dim_out=10).to(args.device)
    else:
        exit('Error: unrecognized model')
    print(net_glob)
    net_glob.train()   # 改为训练模式

    # 获取运算次数 和模型大小
    temp_net = copy.deepcopy(net_glob).to(args.device)
    args.macs, args.model_size = get_model_info(temp_net, img_size, args)
    print(args.macs, args.model_size)
    if args.macs == 0 or args.model_size == 0:
        exit('Error: Unknown model info')


    # ##############################################################################################################################
    # # 设备位置分布
    # devices_locations = get_devices_locations(args)
    # # 基站下发给设备花费时间
    # devices_download_latencies = get_devices_download_latencies(devices_locations, args)
    # # 设备计算时间
    # devices_computation_latencies = get_devices_computation_latencies(args)
    # # 获取设备分组信息
    # partition_lst = get_partition_lst(devices_download_latencies, devices_computation_latencies, args)
    # print(partition_lst)
    #
    # show_devices_info(devices_locations, devices_download_latencies, devices_computation_latencies, args)
    # show_devices_partition(devices_locations, devices_download_latencies, devices_computation_latencies, partition_lst, args)
    #
    # labels = dataset_train.targets
    # # 看一下未操纵前的iid数据分布
    # show_dict_users(partition_lst, dict_users, labels)
    #
    # # 开始操纵数据分布
    # dict_users = semi_data_adjust(partition_lst, dict_users, labels, args)
    # show_dict_users(partition_lst, dict_users, labels)
    # ##############################################################################################################################


    # 确定每轮的具体用户 round_users
    if args.type == 'fedAvg':
        # 用每轮随机选的方法
        all_devices = list(range(args.num_users))
        m = max(int(args.frac * args.num_users), 1)
        seed_all(args.seed)
        round_users = [list(np.random.choice(all_devices, m, replace=False)) for i in range(args.epochs)]
    elif args.type == 'group' or args.type == 'semi':
        # 随机分组，每轮安排一个分组去训练
        all_devices = list(range(args.num_users))
        m = max(int(args.frac * args.num_users), 1)
        seed_all(args.seed)
        np.random.shuffle(all_devices)
        groups = []
        p = 0
        while (p + 1) * m <= len(all_devices):
            groups.append(all_devices[p * m:(p + 1) * m])
            p += 1
        if p * m < len(all_devices):
            groups.append(all_devices[p * m:])
        # 把每个group 直接 append进去
        round_users = []
        cnt = 0
        while cnt < args.epochs:
            for group in groups:
                round_users.append(group)
                cnt += 1
                if cnt >= args.epochs:
                    break
    else:
        exit('Error: Unknown type')


    # 操纵一下每个设备的本地数据集，随机drop一些数据
    if args.cyclic_non_iid:
        partition_lst = groups
        args.semi_m = len(partition_lst)

        # 看一下train_dataset未操纵前的iid数据分布
        labels = dataset_train.targets
        show_dict_users(partition_lst, dict_users, labels)

        # 开始操纵train_dataset的数据分布
        dict_users = semi_data_adjust(partition_lst, dict_users, labels, args)
        show_dict_users(partition_lst, dict_users, labels)

        # 按照group均等划分测试集
        # group_dataset_test = { group_id: set(测试集序号) }
        group_dataset_test = semi_dataset_test(dataset_test, partition_lst, args)
        # 看一下测试集的数据分布
        labels = dataset_test.targets
        show_group_dataset_test(group_dataset_test, labels)

        # 调整测试集 使之和训练集的数据分布相同
        group_dataset_test = semi_dataset_test_adjust(partition_lst, group_dataset_test, labels, args)
        # 再看一下调整后的测试集分布
        labels = dataset_test.targets
        show_group_dataset_test(group_dataset_test, labels)


    # 上面是确定数据分布  dict_users 和 group_dataset_test
    # 下面可以根据训练类型进行训练

    # copy weights
    w_glob = net_glob.state_dict()

    loss_train_lst = []
    acc_train_lst = []
    acc_test_lst = []
    loss_test_lst = []
    record = {}

    if args.semi:  # 半循环聚合
        pass


    else:
        # 一般的聚合方式
        for iter in range(args.epochs):
            args.lr *= args.decay
            w_locals = []
            w_weights = []
            # m = max(int(args.frac * args.num_users), 1)
            # idxs_users = np.random.choice(range(args.num_users), m, replace=False)
            idxs_users = round_users[iter]
            for idx in idxs_users:
                local = LocalUpdate(args=args, net_glob=copy.deepcopy(net_glob).to(args.device), dataset=dataset_train, idxs=dict_users[idx])
                w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
                w_locals.append(copy.deepcopy(w))
                w_weights.append(len(dict_users[idx]))
            # update global weights
            w_glob = FedAvg(w_locals, w_weights)

            # copy weight to net_glob
            net_glob.load_state_dict(w_glob)

            net_glob.eval()  # 改为验证模式
            # 测试本轮模型的loss
            acc_train, loss_train = test_img(net_glob, dataset_train, args)
            loss_train_lst.append(loss_train)
            acc_train_lst.append(acc_train)

            # 测试本轮模型的准确率
            acc_test, loss_test = test_img(net_glob, dataset_test, args)
            acc_test_lst.append(acc_test)
            loss_test_lst.append(loss_test)

            # print 本轮信息
            print('Round {:3d}, Train Accuracy {:.3f}, Train Loss {:.3f}'.format(iter, acc_train, loss_train))
            print('Round {:3d}, Test Accuracy {:.3f}, Test Loss {:.3f}'.format(iter, acc_test, loss_test))

        # 画图
        plt.figure()
        plt.plot(range(len(loss_train_lst)), loss_train_lst)
        plt.ylabel('loss_train')
        plt.savefig('./main_fed_save/fed_seed{}_{}_{}_{}_C{}_iid{}_cyclic{}.{}.{}.loss.train.png'.format(args.seed, args.dataset, args.model, args.epochs, args.frac, args.iid, args.cyclic_non_iid, args.type, args.semi_type))

        # plot acc curve
        plt.figure()
        plt.plot(range(len(acc_test_lst)), acc_test_lst)
        plt.ylabel('acc_test')
        plt.savefig('./main_fed_save/fed_seed{}_{}_{}_{}_C{}_iid{}_cyclic{}.{}.{}.acc.test.png'.format(args.seed, args.dataset, args.model, args.epochs, args.frac, args.iid, args.cyclic_non_iid, args.type, args.semi_type))

        # 保存实验记录
        record["loss_train_lst"] = loss_train_lst
        record["acc_train_lst"] = acc_train_lst
        record["acc_test_lst"] = acc_test_lst
        record["loss_test_lst"] = loss_test_lst
        record["args"] = args
        record["round_users"] = round_users
        pickle.dump(record, open('./main_fed_save/fed_seed{}_{}_{}_{}_C{}_iid{}_cyclic{}.{}.{}.record'.format(args.seed, args.dataset, args.model, args.epochs, args.frac, args.iid, args.cyclic_non_iid, args.type, args.semi_type), 'wb'))


