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

from draw.options import *

if __name__ == '__main__':

    # parse args
    args = args_parser()

    args.R = 600
    args.num_users = 100
    args.epochs = 1000
    args.seed = 1

    # 固定随机性
    seed_all(args.seed)

    trans_mnist = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    mnist_dataset_train = datasets.MNIST('../../data/mnist/', train=True, download=True, transform=trans_mnist)
    mnist_dataset_test = datasets.MNIST('../../data/mnist/', train=False, download=True, transform=trans_mnist)
    mnist_iid_dict_users = mnist_iid(mnist_dataset_train, args)
    mnist_noniid_dict_users = mnist_noniid(mnist_dataset_train, args)

    trans_cifar = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    cifar_dataset_train = datasets.CIFAR10('../..//data/cifar', train=True, download=True, transform=trans_cifar)
    cifar_dataset_test = datasets.CIFAR10('../../data/cifar', train=False, download=True, transform=trans_cifar)
    cifar_iid_dict_users = cifar_iid(cifar_dataset_train, args)
    cifar_noniid_dict_usres = cifar_noniid(cifar_dataset_train, args)




    # 固定随机性
    seed_all(args.seed)

    # 设备随机分组
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

    # 看一下train_dataset未操纵前的iid数据分布
    labels = mnist_dataset_train.targets
    mnist_iid_ylsts = show_dict_users(partition_lst, mnist_iid_dict_users, labels)
    mnist_noniid_ylsts = show_dict_users(partition_lst, mnist_noniid_dict_users, labels)

    # 开始操纵train_dataset的数据分布
    dict_users = mnist_iid_dict_users
    dict_users = semi_data_adjust(partition_lst, dict_users, labels, args)
    mnist_semi_ylsts = show_dict_users(partition_lst, dict_users, labels)



    # 画图
    fig = plt.figure(dpi=800)
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    class_color_lst = ['r', 'g', 'b', 'gold', 'pink', 'magenta', 'yellow', 'darkcyan', 'orange', 'dodgerblue']
    color_lst = []
    for i in range(len(partition_lst)):
        color_lst.extend(class_color_lst)
        color_lst.append("white")
    label_lst = list(range(1, m + 1))
    loc_lst = list(range(0, len(partition_lst) * 11, 11))
    x_lst = range(0, sum([len(group) for group in partition_lst]) + len(partition_lst))

    y_lst = []
    for i in range(len(mnist_iid_ylsts)):
        y_lst.extend(mnist_iid_ylsts[i])
        y_lst.append(0)
    ax1.vlines(x_lst, [0], y_lst)
    ax1.set_xticks(loc_lst)
    ax1.set_xticklabels(label_lst)
    ax1.set_ylabel('i.i.d., number', fontsize=draw_args.fontsize)
    # ax1.axvspan(xmin=0, xmax=10, facecolor='r', alpha=0.1)

    y_lst = []
    for i in range(len(mnist_noniid_ylsts)):
        y_lst.extend(mnist_noniid_ylsts[i])
        y_lst.append(0)
    ax2.vlines(x_lst, [0], y_lst)
    ax2.set_xticks(loc_lst)
    ax2.set_xticklabels(label_lst)
    ax2.set_ylabel('non i.i.d., number', fontsize=draw_args.fontsize)

    y_lst = []
    for i in range(len(mnist_semi_ylsts)):
        y_lst.extend(mnist_semi_ylsts[i])
        y_lst.append(0)
    ax3.vlines(x_lst, [0], y_lst)
    ax3.set_xticks(loc_lst)
    ax3.set_xticklabels(label_lst)
    ax3.set_ylabel('cyclic non i.i.d., number', fontsize=draw_args.fontsize)

    fig.tight_layout()
    plt.savefig("C:\\Users\\tian\\Desktop\\figs4\\{}_dataset_distribution.pdf".format(args.dataset))
    plt.show()



    # 画图2
    figsize = (10, 3)

    fig, ax1 = plt.subplots(dpi=800, figsize=figsize)

    class_color_lst = ['r', 'g', 'b', 'gold', 'pink', 'magenta', 'yellow', 'darkcyan', 'orange', 'dodgerblue']
    vline_x_lst = []  # 在组与组之间画上虚线分隔
    for i in range(1, 10):
        vline_x_lst.append(i+0.5)

    ax1.vlines(vline_x_lst, [0], [800 for i in range(9)], linestyle="dashed", color='gray')
    class_count = 0
    for y_lst in mnist_iid_ylsts:
        ax1.plot(range(1, 11), y_lst, marker='.', color=class_color_lst[class_count])
        class_count += 1
    ax1.set_xticks(range(1, 11))
    ax1.set_ylabel('Number', fontsize=draw_args.fontsize)
    ax1.set_xlabel('Round', fontsize=draw_args.fontsize)
    fig.tight_layout()
    plt.savefig("C:\\Users\\tian\\Desktop\\figs4\\dataset_distribution_iid.pdf".format(args.dataset))

    fig, ax2 = plt.subplots(dpi=800, figsize=figsize)
    ax2.vlines(vline_x_lst, [0], [1600 for i in range(9)], linestyle="dashed", color='gray')
    class_count = 0
    for y_lst in mnist_noniid_ylsts:
        ax2.plot(range(1, 11), y_lst, marker='.', color=class_color_lst[class_count])
        class_count += 1
    ax2.set_xticks(range(1, 11))
    ax2.set_ylabel('Number', fontsize=draw_args.fontsize)
    ax2.set_xlabel('Round', fontsize=draw_args.fontsize)
    fig.tight_layout()
    plt.savefig("C:\\Users\\tian\\Desktop\\figs4\\dataset_distribution_noniid.pdf".format(args.dataset))


    fig, ax3 = plt.subplots(dpi=800, figsize=figsize)
    ax3.vlines(vline_x_lst, [0], [800 for i in range(9)], linestyle="dashed", color='gray')
    class_count = 0
    for y_lst in mnist_semi_ylsts:
        ax3.plot(range(1, 11), y_lst, marker='.', color=class_color_lst[class_count])
        class_count += 1
    ax3.set_xticks(range(1, 11))
    ax3.set_ylabel('Number', fontsize=draw_args.fontsize)
    ax3.set_xlabel('Round', fontsize=draw_args.fontsize)

    fig.tight_layout()
    plt.savefig("C:\\Users\\tian\\Desktop\\figs4\\dataset_distribution_cyclic_noniid.pdf".format(args.dataset))