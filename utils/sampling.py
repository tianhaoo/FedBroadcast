#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6
import copy

import numpy as np
from torchvision import datasets, transforms
from utils import seed_all


def mnist_iid(dataset, args):
    """
    Sample I.I.D. client data from MNIST dataset
    :param dataset:
    :param num_users:
    :return: dict of image index
    """
    seed_all(args.seed)
    num_items = int(len(dataset)/args.num_users)
    dict_users, all_idxs = {}, [i for i in range(len(dataset))]
    for i in range(args.num_users):
        dict_users[i] = set(np.random.choice(all_idxs, num_items, replace=False))
        all_idxs = list(set(all_idxs) - dict_users[i])
    return dict_users


def mnist_noniid(dataset, args):
    """
    Sample non-I.I.D client data from MNIST dataset
    :param dataset:
    :param num_users:
    :return:
    """
    seed_all(args.seed)
    num_shards, num_imgs = 200, 300
    # 每个用户有2类，100个client，所以有200个shards， 共60000个数据，所以每个shards有60000/200=300个
    idx_shard = [i for i in range(num_shards)]
    dict_users = {i: np.array([], dtype='int64') for i in range(args.num_users)}
    idxs = np.arange(num_shards*num_imgs)
    # labels = dataset.train_labels.numpy()
    labels = np.array(dataset.targets, dtype=np.int64)


    # sort labels
    idxs_labels = np.vstack((idxs, labels))  # 沿竖直方向将两个数组堆叠起来
    # 此时idxs_labels第一行是有序的，第二行无序
    idxs_labels = idxs_labels[:, idxs_labels[1, :].argsort()]  # 按照类编号排序
    # 此时idxs_labels第二行是有序的，第一行无序
    idxs = idxs_labels[0, :]

    # divide and assign
    for i in range(args.num_users):
        rand_set = set(np.random.choice(idx_shard, 2, replace=False))   # 200个shards中随机选俩
        idx_shard = list(set(idx_shard) - rand_set)  # 去掉已选的这俩
        for rand in rand_set:
            # 把选的这俩shards对应的全部序号放进字典， 因为idxs是按照标签排好的，所以只要像这样连续300个地拿，就可以保证每个客户端只有1或2个标签
            dict_users[i] = np.concatenate((dict_users[i], idxs[rand*num_imgs:(rand+1)*num_imgs]), axis=0)
            # { 客户端id : 数据集序号列表 }
    return dict_users


def cifar_iid(dataset, args):
    """
    Sample I.I.D. client data from CIFAR10 dataset
    :param dataset:
    :param num_users:
    :return: dict of image index
    """
    seed_all(args.seed)
    num_items = int(len(dataset)/args.num_users)
    dict_users, all_idxs = {}, [i for i in range(len(dataset))]
    for i in range(args.num_users):
        dict_users[i] = set(np.random.choice(all_idxs, num_items, replace=False))
        all_idxs = list(set(all_idxs) - dict_users[i])
    return dict_users


def cifar_noniid(dataset, args):
    """
    Sample non-I.I.D. client data from CIFAR10 dataset
    :param dataset:
    :param num_users:
    :return: dict of image index
    """
    seed_all(args.seed)
    num_shards, num_imgs = 200, 250
    # 每个用户有2类，100个client，所以有200个shards， 共50000个数据，所以每个shards有50000/200=250个
    idx_shard = [i for i in range(num_shards)]
    dict_users = {i: np.array([], dtype='int64') for i in range(args.num_users)}
    idxs = np.arange(num_shards * num_imgs)
    labels = np.array(dataset.targets, dtype=np.int64)

    # sort labels
    idxs_labels = np.vstack((idxs, labels))  # 沿竖直方向将两个数组堆叠起来
    # 此时idxs_labels第一行是有序的，第二行无序
    idxs_labels = idxs_labels[:, idxs_labels[1, :].argsort()]  # 按照类编号排序
    # 此时idxs_labels第二行是有序的，第一行无序
    idxs = idxs_labels[0, :]

    # divide and assign
    for i in range(args.num_users):
        rand_set = set(np.random.choice(idx_shard, 2, replace=False))  # 200个shards中随机选俩
        idx_shard = list(set(idx_shard) - rand_set)  # 去掉已选的这俩
        for rand in rand_set:
            # 把选的这俩shards对应的全部序号放进字典， 因为idxs是按照标签排好的，所以只要像这样连续300个地拿，就可以保证每个客户端只有1或2个标签
            dict_users[i] = np.concatenate((dict_users[i], idxs[rand * num_imgs:(rand + 1) * num_imgs]), axis=0)
            # { 客户端id : 数据集序号列表 }
    return dict_users

# 调整训练集的数据分布
def semi_data_adjust(partition_lst, dict_users, labels, args):
    # 把一组的数据合并到一起
    # group_datas :{group_id: set(本组设备的全部数据集合), ..., ...}
    group_datas = {}
    for group_id in range(len(partition_lst)):
        group = partition_lst[group_id]
        group_data = set()
        for user in group:
            group_data = group_data.union(dict_users[user])
        group_datas[group_id] = group_data
    # 统计每组内，每类的个数
    # group_sums: {group_id: [类0的数量， 类1的数量 ,..., 类9的数量]， 。。。 ，}
    group_sums = {}
    for group_id, group_data in group_datas.items():
        group_sum = [0 for i in range(10)]
        for data in group_data:
            group_sum[int(labels[data])] += 1
        group_sums[group_id] = group_sum

    # 确定drop的比例
    ratio_step = int(round(1/len(partition_lst), 2) * 100)
    ratio_lst = list(range(0, 100, ratio_step))

    # 设置每组，每类应该drop的比例、数量和应该drop的数据
    # group_drop: { group_id: { 'ratio_lst':[ 10, 20, ...], 'drop_num_lst': [234, 345, ...], 'drop_data': {34, 43656, 565, ...}},
    #                     group_id2: { 'ratio_lst':[ 10, 20, ...], 'drop_num_lst': [234, 345, ...], 'drop_data': {34, 43656, 565, ...}}, ...}
    group_drop = {}
    for group_id in range(len(partition_lst)):
        temp = {}
        # 循环右移一位
        ratio_lst.insert(0, ratio_lst.pop())
        temp['ration_lst'] = copy.deepcopy(ratio_lst)

        drop_num_lst = []
        group_sum = group_sums[group_id]
        for i in range(10):
            drop_num_lst.append(int(group_sum[i] * ratio_lst[i] / 100))
        temp['drop_num_lst'] = drop_num_lst

        drop_data = set()
        group_data = group_datas[group_id]  # 此group内所有数据序号组成的集合、
        for class_id in range(10):
            drop_num = drop_num_lst[class_id]  # 此class需要drop的数量
            group_class_data = []  # 此group，此class的所有数据
            for data_idx in group_data:
                if labels[data_idx] == class_id:
                    group_class_data.append(data_idx)

            seed_all(args.seed)
            drop_data = drop_data.union(set(np.random.choice(group_class_data, drop_num, replace=False)))
        temp['drop_data'] = drop_data
        group_drop[group_id] = temp

    # 按组遍历user,实行drop data
    for group_id in range(len(partition_lst)):
        drop_data = group_drop[group_id]['drop_data']
        for user in partition_lst[group_id]:
            dict_users[user] = dict_users[user] - drop_data

    return dict_users


# 返回按照block分好的iid的测试集
def semi_dataset_test(dataset, partition_lst, args):
    seed_all(args.seed)
    num_items = int(len(dataset) / len(partition_lst))
    group_dataset_test = {}
    all_idxs = [i for i in range(len(dataset))]
    for i in range(len(partition_lst)):
        group_dataset_test[i] = set(np.random.choice(all_idxs, num_items, replace=False))
        all_idxs = list(set(all_idxs) - group_dataset_test[i])
    return group_dataset_test


def semi_dataset_test_adjust(partition_lst, group_dataset_test, labels, args):
    # 统计每组内，每类的个数
    # group_sums: {group_id: [类0的数量， 类1的数量 ,..., 类9的数量]， 。。。 ，}
    group_sums = {}
    for group_id, group_data in group_dataset_test.items():
        group_sum = [0 for i in range(10)]
        for data in group_data:
            group_sum[int(labels[data])] += 1
        group_sums[group_id] = group_sum

        # 确定drop的比例
        ratio_step = int(round(1 / len(partition_lst), 2) * 100)
        ratio_lst = list(range(0, 100, ratio_step))

    # 设置每组，每类应该drop的比例、数量和应该drop的数据
    # group_drop: { group_id: { 'ratio_lst':[ 10, 20, ...], 'drop_num_lst': [234, 345, ...], 'drop_data': {34, 43656, 565, ...}},
    #                     group_id2: { 'ratio_lst':[ 10, 20, ...], 'drop_num_lst': [234, 345, ...], 'drop_data': {34, 43656, 565, ...}}, ...}
    group_drop = {}
    for group_id in range(len(partition_lst)):
        temp = {}
        # 循环右移一位
        ratio_lst.insert(0, ratio_lst.pop())
        temp['ration_lst'] = copy.deepcopy(ratio_lst)

        drop_num_lst = []
        group_sum = group_sums[group_id]
        for i in range(10):
            drop_num_lst.append(int(group_sum[i] * ratio_lst[i] / 100))
        temp['drop_num_lst'] = drop_num_lst

        drop_data = set()
        group_data = group_dataset_test[group_id]  # 此group内所有数据序号组成的集合、
        for class_id in range(10):
            drop_num = drop_num_lst[class_id]  # 此class需要drop的数量
            group_class_data = []  # 此group，此class的所有数据
            for data_idx in group_data:
                if labels[data_idx] == class_id:
                    group_class_data.append(data_idx)

            seed_all(args.seed)
            drop_data = drop_data.union(set(np.random.choice(group_class_data, drop_num, replace=False)))
        temp['drop_data'] = drop_data
        group_drop[group_id] = temp

    for group_id in range(len(partition_lst)):
        drop_data = group_drop[group_id]['drop_data']
        group_dataset_test[group_id] = group_dataset_test[group_id] - drop_data

    return group_dataset_test

# 给定数据序号构成的集合 和当前是第几天day, 总天数semi_K, 返回指定段的集合
def get_day_k_train(dataset, day, semi_K):
    data_lst = list(dataset)
    frac = max(int(len(data_lst)/semi_K), 1)
    return set(data_lst[day*frac:(day+1)*frac])









