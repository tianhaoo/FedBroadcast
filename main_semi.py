# 只过一遍数据集的semi训练


import pickle
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import random
import os


import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import copy
import numpy as np
from torchvision import datasets, transforms
import torch

from utils.sampling import mnist_iid, mnist_noniid, cifar_iid, cifar_noniid, semi_data_adjust, semi_dataset_test, \
    semi_dataset_test_adjust, get_day_k_train
from utils.options import args_parser
from utils import seed_all, get_model_info
from models.Update import LocalUpdate
from models.Nets import MLP, CNNMnist, CNNCifar
from models.Fed import FedAvg
from models.test import test_img, test_semi_iid, test_semi_fb, test_semi_pla, test_semi_sep, test_semi_fedavg

from utils.simulation import get_devices_locations, get_devices_download_latencies, \
    get_devices_computation_latencies, get_partition_lst
from utils.show import show_devices_info, show_devices_partition, show_dict_users, show_group_dataset_test

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
    # 在半循环这里没有iid了，全都是人为操纵的non-iid
    # dict_users : { 用户序号 ： 数据集序号集合 }
    if args.dataset == 'mnist':
        trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
        dataset_train = datasets.MNIST('../data/mnist/', train=True, download=True, transform=trans_mnist)
        dataset_test = datasets.MNIST('../data/mnist/', train=False, download=True, transform=trans_mnist)
        args.data_num = len(dataset_train)
        # sample users
        if args.iid or args.semi:
            dict_users = mnist_iid(dataset_train, args)
        else:
            dict_users = mnist_noniid(dataset_train, args)
    elif args.dataset == 'cifar':
        trans_cifar = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        dataset_train = datasets.CIFAR10('../data/cifar', train=True, download=True, transform=trans_cifar)
        dataset_test = datasets.CIFAR10('../data/cifar', train=False, download=True, transform=trans_cifar)
        args.data_num = len(dataset_train)
        if args.iid or args.semi:
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
    net_glob.train()  # 改为训练模式

    # 获取运算次数 和模型大小
    temp_net = copy.deepcopy(net_glob).to(args.device)
    args.macs, args.model_size = get_model_info(temp_net, img_size, args)
    print(args.macs, args.model_size)
    if args.macs == 0 or args.model_size == 0:
        exit('Error: Unknown model info')

    # 给设备分组
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
    partition_lst = groups
    args.semi_m = len(partition_lst)

    if args.semi:
        # 看一下train_dataset未操纵前的iid数据分布
        labels = dataset_train.targets
        # show_dict_users(partition_lst, dict_users, labels)

        # 开始操纵train_dataset的数据分布
        dict_users = semi_data_adjust(partition_lst, dict_users, labels, args)
        # show_dict_users(partition_lst, dict_users, labels)

        # 按照group均等划分测试集
        # group_dataset_test = { group_id: set(测试集序号) }
        group_dataset_test = semi_dataset_test(dataset_test, partition_lst, args)
        # 看一下测试集的数据分布
        labels = dataset_test.targets
        # show_group_dataset_test(group_dataset_test, labels)

        # 调整测试集 使之和训练集的数据分布相同
        group_dataset_test = semi_dataset_test_adjust(partition_lst, group_dataset_test, labels, args)
        # 再看一下调整后的测试集分布
        labels = dataset_test.targets
        # show_group_dataset_test(group_dataset_test, labels)
        # 存放现有所有的测试集的序号，供iid的方式使用
        group_dataset_test_idxs = set()
        for group_id, idxs in group_dataset_test.items():
            group_dataset_test_idxs = group_dataset_test_idxs.union(idxs)
    else:
        # 半循环聚合，但是使用的是普通non-iid
        # dict_users 不变
        # group_dataset_test 是iid的/是non-iid的
        # 按照group均等划分测试集
        # group_dataset_test = { group_id: set(测试集序号) }
        group_dataset_test = semi_dataset_test(dataset_test, partition_lst, args)
        # 看一下测试集的数据分布
        labels = dataset_test.targets
        # show_group_dataset_test(group_dataset_test, labels)

        # # 调整测试集 使之和训练集的数据分布相同
        # group_dataset_test = semi_dataset_test_adjust(partition_lst, group_dataset_test, labels, args)
        # # 再看一下调整后的测试集分布
        # labels = dataset_test.targets
        # show_group_dataset_test(group_dataset_test, labels)

        # 存放现有所有的测试集的序号，供iid的方式使用
        group_dataset_test_idxs = set()
        for group_id, idxs in group_dataset_test.items():
            group_dataset_test_idxs = group_dataset_test_idxs.union(idxs)

    # 确定round_user
    if args.semi_type == 'fedavg':
        m = max(int(args.num_users * args.frac), 1)
        seed_all(args.seed)
        round_users = [list(np.random.choice(all_devices, m, replace=False)) for i in range(args.semi_K * args.semi_m)]
    elif args.semi_type == 'rr':
        # 给设备分组
        all_devices = list(range(args.num_users))
        m = max(int(args.frac * args.num_users), 1)
        seed_all(args.seed+1124234)
        np.random.shuffle(all_devices)
        groups = []
        p = 0
        while (p + 1) * m <= len(all_devices):
            groups.append(all_devices[p * m:(p + 1) * m])
            p += 1
        if p * m < len(all_devices):
            groups.append(all_devices[p * m:])
        partition_lst = groups
        round_users = []
        for k in range(args.semi_K):
            for i in range(args.semi_m):
                round_users.append(partition_lst[i])
    else:
        # 每天把每个block的所有users 直接 append进去
        round_users = []
        for k in range(args.semi_K):
            for i in range(args.semi_m):
                round_users.append(partition_lst[i])


    # 有semi_K天，每天训练semi_m轮

    if args.semi_type == "iid":
        record = {}
        loss_train_lst = []
        acc_test_lst = []

        # 开始训练
        w_glob = net_glob.state_dict()
        for k in range(args.semi_K):
            k_day_dataset = set()
            for i in range(args.semi_m):
                # 先拿到今天每一个block里的数据
                idxs_users = partition_lst[i]  # block i 中全部users
                for idx in idxs_users:
                    k_day_dataset = k_day_dataset.union(
                        get_day_k_train(dict_users[idx], k, args.semi_K)
                    )
            # 拿到今天所有数据后，只需进行一次训练，无需聚合
            local = LocalUpdate(args=args, net_glob=copy.deepcopy(net_glob).to(args.device),
                                dataset=dataset_train,
                                idxs=k_day_dataset)
            w_glob, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
            loss_train_lst.append(copy.deepcopy(loss))
            # copy weight to net_glob
            net_glob.load_state_dict(w_glob)

            net_glob.eval()  # 改为验证模式
            # 开始测试今天的准确率
            acc_test, loss_test = test_semi_iid(net_glob, dataset_test, group_dataset_test_idxs, args)
            acc_test_lst.append(acc_test)
            print("iid, day", k, "acc_test", acc_test, "train_loss", loss)

        # 画图
        plt.figure()
        plt.plot(range(len(loss_train_lst)), loss_train_lst)
        plt.ylabel('loss_train')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.loss.train.png'.format(args.seed, args.dataset, args.model, args.semi_K,
                                                                              args.semi_m, args.semi, args.semi_type))

        # plot acc curve
        plt.figure()
        plt.plot(range(len(acc_test_lst)), acc_test_lst)
        plt.ylabel('acc_test')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.acc.test.png'.format(args.seed, args.dataset, args.model, args.semi_K,
                                                                              args.semi_m, args.semi, args.semi_type))

        # 保存实验记录
        record["loss_train_lst"] = loss_train_lst
        record["acc_test_lst"] = acc_test_lst
        record["args"] = args
        record["partition_lst"] = partition_lst
        record["dict_users"] = dict_users
        record["round_users"] = round_users
        pickle.dump(record, open(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.record'.format(args.seed, args.dataset, args.model, args.semi_K,
                                                                              args.semi_m, args.semi, args.semi_type), 'wb'))

    elif args.semi_type == 'fedavg' or args.semi_type == 'rr':
        record = {}
        loss_train_lst = []
        acc_test_lst = []
        w_all = {}  # {day1: { group1: w1, group2: w2, ..., group_m: w_m}, day2:{ ... }, ... }
        # 开始训练
        w_glob = net_glob.state_dict()
        for k in range(args.semi_K):
            w_all[k] = {}
            group_loss = []
            for i in range(args.semi_m):
                w_locals = []
                w_weights = []
                n = k * args.semi_m + i
                idxs_users = round_users[n]
                for idx in idxs_users:
                    local = LocalUpdate(args=args, net_glob=copy.deepcopy(net_glob).to(args.device), dataset=dataset_train,
                                        idxs=dict_users[idx])
                    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
                    w_locals.append(copy.deepcopy(w))
                    w_weights.append(len(dict_users[idx]))
                    group_loss.append(copy.deepcopy(loss))
                # 聚合，相当于将block i 中的全部数据迭代了一遍
                w_glob = FedAvg(w_locals, w_weights)
                # copy weight to net_glob
                net_glob.load_state_dict(w_glob)
                # 记录下第k天，第i块的模型参数
                w_all[k][i] = w_glob

            # 到这相当于一天过去了，把所有block都按顺序迭代了一遍。
            # 需要看一下今天的loss和准确率。
            loss_train_lst.append(sum(group_loss) / len(group_loss))

            net_glob.eval()  # 改为验证模式
            # 开始测试今天的准确率
            acc_test, loss_test = test_semi_fedavg(net_glob, w_all[k], dataset_test, group_dataset_test, args)
            acc_test_lst.append(acc_test)
            if args.semi_type == 'fedavg':
                print("fedavg, day", k, "acc_test", acc_test, "train_loss", sum(group_loss) / len(group_loss))
            else:
                print("rr, day", k, "acc_test", acc_test, "train_loss", sum(group_loss) / len(group_loss))

        # 画图
        plt.figure()
        plt.plot(range(len(loss_train_lst)), loss_train_lst)
        plt.ylabel('loss_train')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.loss.train.png'.format(args.seed, args.dataset,
                                                                                        args.model, args.semi_K,
                                                                                        args.semi_m, args.semi,
                                                                                        args.semi_type))
        # plot acc curve
        plt.figure()
        plt.plot(range(len(acc_test_lst)), acc_test_lst)
        plt.ylabel('acc_test')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.acc.test.png'.format(args.seed, args.dataset,
                                                                                       args.model, args.semi_K,
                                                                                       args.semi_m, args.semi,
                                                                                       args.semi_type))
        # 保存实验记录
        record["loss_train_lst"] = loss_train_lst
        record["acc_test_lst"] = acc_test_lst
        record["args"] = args
        record["partition_lst"] = partition_lst
        record["dict_users"] = dict_users
        record["round_users"] = round_users
        pickle.dump(record, open(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.record'.format(args.seed, args.dataset,
                                                                                 args.model, args.semi_K,
                                                                                 args.semi_m, args.semi,
                                                                                 args.semi_type), 'wb'))


    elif args.semi_type == "fb" or args.semi_type == "pla":
        # 一个SGD链， 每天随机选一个block的w用于验证 / 每天聚合这个块之前的所有w用于验证
        record = {}
        loss_train_lst = []
        acc_test_lst = []
        w_all = {}   # {day1: { group1: w1, group2: w2, ..., group_m: w_m}, day2:{ ... }, ... }

        # 开始训练
        w_glob = net_glob.state_dict()
        for k in range(args.semi_K):
            w_all[k] = {}
            group_loss = []
            for i in range(args.semi_m):
                w_locals = []
                w_weights = []
                idxs_users = partition_lst[i]  # block i 中全部users
                for idx in idxs_users:
                    local = LocalUpdate(args=args, net_glob=copy.deepcopy(net_glob).to(args.device), dataset=dataset_train,
                                        idxs=dict_users[idx])
                    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
                    w_locals.append(copy.deepcopy(w))
                    group_loss.append(copy.deepcopy(loss))
                    w_weights.append(len(dict_users[idx]))
                # 聚合，相当于将block i 中的全部数据迭代了一遍
                w_glob = FedAvg(w_locals, w_weights)
                # copy weight to net_glob
                net_glob.load_state_dict(w_glob)
                # 记录下第k天，第i块的模型参数
                w_all[k][i] = w_glob
            # 到这相当于一天过去了，把所有block都按顺序迭代了一遍。
            # 需要看一下今天的loss和准确率。
            loss_train_lst.append(sum(group_loss) / len(group_loss))

            if args.semi_type == "fb":
                net_glob.eval()  # 改为验证模式
                # 开始测试今天的准确率
                acc_test, loss_test = test_semi_fb(net_glob, w_all[k], dataset_test, group_dataset_test, args)
                acc_test_lst.append(acc_test)
                print("fb, day", k, "acc_test", acc_test, "train_loss", sum(group_loss) / len(group_loss))
            elif args.semi_type == 'pla':
                net_glob.eval()  # 改为验证模式
                # 开始测试今天的准确率
                acc_test, loss_test = test_semi_pla(net_glob, w_all, dataset_test, group_dataset_test, args)
                acc_test_lst.append(acc_test)

                print("pla, day", k, "acc_test", acc_test, "train_loss", sum(group_loss) / len(group_loss))
            else:
                exit("Error: Unknown semi type")

        # 画图
        plt.figure()
        plt.plot(range(len(loss_train_lst)), loss_train_lst)
        plt.ylabel('loss_train')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.loss.train.png'.format(args.seed, args.dataset,
                                                                                        args.model, args.semi_K,
                                                                                        args.semi_m, args.semi,
                                                                                        args.semi_type))
        # plot acc curve
        plt.figure()
        plt.plot(range(len(acc_test_lst)), acc_test_lst)
        plt.ylabel('acc_test')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.acc.test.png'.format(args.seed, args.dataset,
                                                                                       args.model, args.semi_K,
                                                                                       args.semi_m, args.semi,
                                                                                       args.semi_type))
        # 保存实验记录
        record["loss_train_lst"] = loss_train_lst
        record["acc_test_lst"] = acc_test_lst
        record["args"] = args
        record["partition_lst"] = partition_lst
        record["dict_users"] = dict_users
        record["round_users"] = round_users
        pickle.dump(record, open(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.record'.format(args.seed, args.dataset,
                                                                                 args.model, args.semi_K,
                                                                                 args.semi_m, args.semi,
                                                                                 args.semi_type), 'wb'))

    elif args.semi_type == "sep":
        # m个SGD链， 每天在各自的数据集上验证这m个w
        record = {}
        loss_train_lst = []
        acc_test_lst = []
        w_all = {}  # {day1: { group1: w1, group2: w2, ..., group_m: w_m}, day2:{ ... }, ... }

        # 开始训练
        w_glob = net_glob.state_dict()
        for k in range(args.semi_K):
            w_all[k] = {}
            group_loss = []
            for i in range(args.semi_m):
                # 每块训练之前，全局模型要加载前一天 对应块的w
                net_glob.train()
                if k >= 1:
                    net_glob.load_state_dict(w_all[k - 1][i])
                w_locals = []
                w_weights = []
                idxs_users = partition_lst[i]  # block i 中全部users
                for idx in idxs_users:
                    local = LocalUpdate(args=args, net_glob=copy.deepcopy(net_glob).to(args.device),
                                        dataset=dataset_train,
                                        idxs=dict_users[idx])
                    w, loss = local.train(net=copy.deepcopy(net_glob).to(args.device))
                    w_locals.append(copy.deepcopy(w))
                    group_loss.append(copy.deepcopy(loss))
                    w_weights.append(len(dict_users[idx]))
                # 聚合，相当于将block i 中的全部数据迭代了一遍
                w_glob = FedAvg(w_locals, w_weights)
                # copy weight to net_glob
                net_glob.load_state_dict(w_glob)
                # 记录下第k天，第i块的模型参数
                w_all[k][i] = w_glob
            # 到这相当于一天过去了，把所有block都按顺序迭代了一遍。
            # 需要看一下今天的loss和准确率。
            loss_train_lst.append(sum(group_loss) / len(group_loss))

            net_glob.eval()  # 改为验证模式
            # 开始测试今天的准确率
            acc_test, loss_test = test_semi_sep(net_glob, w_all[k], dataset_test, group_dataset_test, args)
            acc_test_lst.append(acc_test)
            print("sep, day", k, "acc_test", acc_test, "train_loss", sum(group_loss) / len(group_loss))

        # 画图
        plt.figure()
        plt.plot(range(len(loss_train_lst)), loss_train_lst)
        plt.ylabel('loss_train')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.loss.train.png'.format(args.seed, args.dataset,
                                                                                        args.model, args.semi_K,
                                                                                        args.semi_m, args.semi,
                                                                                        args.semi_type))
        # plot acc curve
        plt.figure()
        plt.plot(range(len(acc_test_lst)), acc_test_lst)
        plt.ylabel('acc_test')
        plt.savefig(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.acc.test.png'.format(args.seed, args.dataset,
                                                                                       args.model, args.semi_K,
                                                                                       args.semi_m, args.semi,
                                                                                       args.semi_type))
        # 保存实验记录
        record["loss_train_lst"] = loss_train_lst
        record["acc_test_lst"] = acc_test_lst
        record["args"] = args
        record["partition_lst"] = partition_lst
        record["dict_users"] = dict_users
        record["round_users"] = round_users
        pickle.dump(record, open(
            './main_semi_save/semi_seed{}_{}_{}_K{}_C{}_semi{}.{}.record'.format(args.seed, args.dataset,
                                                                                 args.model, args.semi_K,
                                                                                 args.semi_m, args.semi,
                                                                                 args.semi_type), 'wb'))

    else:
        exit("Error: Unknown semi type")
