#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @python: 3.6
import random

import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

from models.Fed import get_w_avg
from models.Update import DatasetSplit
from utils import seed_all


def test_img(net_g, datatest, args):
    net_g.eval()
    # testing
    test_loss = 0
    correct = 0
    data_loader = DataLoader(datatest, batch_size=args.bs)
    for idx, (data, target) in enumerate(data_loader):
        if args.gpu != -1:
            data, target = data.cuda(), target.cuda()
        log_probs = net_g(data)
        # sum up batch loss
        test_loss += F.cross_entropy(log_probs, target, reduction='sum').item()
        # get the index of the max log-probability
        y_pred = log_probs.data.max(1, keepdim=True)[1]
        correct += y_pred.eq(target.data.view_as(y_pred)).long().cpu().sum()

    test_loss /= len(data_loader.dataset)
    accuracy = 100.00 * correct / len(data_loader.dataset)
    if args.verbose:
        print('\nTest set: Average loss: {:.4f} \nAccuracy: {}/{} ({:.2f}%)\n'.format(
            test_loss, correct, len(data_loader.dataset), accuracy))
    return accuracy, test_loss


def test_semi_iid(net_g, datatest, idxs, args):
    net_g.eval()
    # testing
    test_loss = 0
    correct = 0
    data_loader = DataLoader(DatasetSplit(datatest, idxs), batch_size=args.bs, shuffle=True)
    for idx, (data, target) in enumerate(data_loader):
        if args.gpu != -1:
            data, target = data.cuda(), target.cuda()
        log_probs = net_g(data)
        # sum up batch loss
        test_loss += F.cross_entropy(log_probs, target, reduction='sum').item()
        # get the index of the max log-probability
        y_pred = log_probs.data.max(1, keepdim=True)[1]
        correct += y_pred.eq(target.data.view_as(y_pred)).long().cpu().sum()

    test_loss /= len(data_loader.dataset)
    accuracy = 100.00 * correct / len(data_loader.dataset)
    if args.verbose:
        print('\nTest set: Average loss: {:.4f} \nAccuracy: {}/{} ({:.2f}%)\n'.format(
            test_loss, correct, len(data_loader.dataset), accuracy))
    return accuracy, test_loss


def test_semi_fedavg(net_g, w_all_k, dataset, group_dataset_test, args):
    # 先从w_all_k 中m个w对应m个测试集的mxm个准确率都测一遍
    seed_all(args.seed)
    acc_test_lst_lst = []
    loss_test_lst_lst =[]
    for i in range(len(w_all_k)):
        w = w_all_k[i]
        net_g.load_state_dict(w)
        # 然后针对每一块的数据集，都用这个w进行测试
        acc_test_lst = []
        loss_test_lst = []
        for group_id, idxs in group_dataset_test.items():
            net_g.eval()
            # testing
            test_loss = 0
            correct = 0
            data_loader = DataLoader(DatasetSplit(dataset, idxs), batch_size=args.bs, shuffle=True)
            for idx, (data, target) in enumerate(data_loader):
                if args.gpu != -1:
                    data, target = data.cuda(), target.cuda()
                log_probs = net_g(data)
                # sum up batch loss
                test_loss += F.cross_entropy(log_probs, target, reduction='sum').item()
                # get the index of the max log-probability
                y_pred = log_probs.data.max(1, keepdim=True)[1]
                correct += y_pred.eq(target.data.view_as(y_pred)).long().cpu().sum()

            test_loss /= len(data_loader.dataset)
            accuracy = 100.00 * correct / len(data_loader.dataset)
            acc_test_lst.append(accuracy)
            loss_test_lst.append(test_loss)
        acc_test_lst_lst.append(acc_test_lst)
        loss_test_lst_lst.append(loss_test_lst)
    print("test_semi_fedavg",  "acc_test_lst_lst", acc_test_lst_lst)

    # 返回这m个块测试的准确率的平均值
    average_test_acc_lst = [sum(acc_test_lst)/len(acc_test_lst) for acc_test_lst in acc_test_lst_lst]
    average_test_loss_lst = [sum(loss_test_lst)/len(loss_test_lst) for loss_test_lst in loss_test_lst_lst]
    return sum(average_test_acc_lst) / len(average_test_acc_lst), sum(average_test_loss_lst) / len(average_test_loss_lst)


def test_semi_fb(net_g, w_all_k, dataset, group_dataset_test, args):
    # 先从w_all_k中随机选一个w，用于测试
    seed_all(args.seed)
    w = w_all_k[random.randint(0, len(w_all_k))]
    net_g.load_state_dict(w)
    # 然后针对每一块的数据集，都用这个w进行测试
    acc_test_lst = []
    loss_test_lst = []
    for group_id, idxs in group_dataset_test.items():
        net_g.eval()
        # testing
        test_loss = 0
        correct = 0
        data_loader = DataLoader(DatasetSplit(dataset, idxs), batch_size=args.bs, shuffle=True)
        for idx, (data, target) in enumerate(data_loader):
            if args.gpu != -1:
                data, target = data.cuda(), target.cuda()
            log_probs = net_g(data)
            # sum up batch loss
            test_loss += F.cross_entropy(log_probs, target, reduction='sum').item()
            # get the index of the max log-probability
            y_pred = log_probs.data.max(1, keepdim=True)[1]
            correct += y_pred.eq(target.data.view_as(y_pred)).long().cpu().sum()

        test_loss /= len(data_loader.dataset)
        accuracy = 100.00 * correct / len(data_loader.dataset)
        acc_test_lst.append(accuracy)
        loss_test_lst.append(test_loss)
    print("test_semi_fb",  "acc_test_lst", acc_test_lst)
    # 返回这m个块测试的准确率的平均值
    return sum(acc_test_lst) / len(acc_test_lst), sum(loss_test_lst) / len(loss_test_lst)



def test_semi_pla(net_g, w_all, dataset, group_dataset_test, args):
    acc_test_lst = []
    loss_test_lst = []
    for group_id, idxs in group_dataset_test.items():
        # 测试之前先把每一个block对应的w赋值好
        # 平均第1到k天的所有w
        w_lst = []
        for day, group_w in w_all.items():
            w_lst.append(group_w[group_id])
        w_avg = get_w_avg(w_lst)
        net_g.load_state_dict(w_avg)
        net_g.eval()
        # testing
        test_loss = 0
        correct = 0
        data_loader = DataLoader(DatasetSplit(dataset, idxs), batch_size=args.bs, shuffle=True)
        for idx, (data, target) in enumerate(data_loader):
            if args.gpu != -1:
                data, target = data.cuda(), target.cuda()
            log_probs = net_g(data)
            # sum up batch loss
            test_loss += F.cross_entropy(log_probs, target, reduction='sum').item()
            # get the index of the max log-probability
            y_pred = log_probs.data.max(1, keepdim=True)[1]
            correct += y_pred.eq(target.data.view_as(y_pred)).long().cpu().sum()

        test_loss /= len(data_loader.dataset)
        accuracy = 100.00 * correct / len(data_loader.dataset)
        acc_test_lst.append(accuracy)
        loss_test_lst.append(test_loss)
    print("test_semi_pla", "acc_test_lst", acc_test_lst)
    # 返回这m个块测试的准确率的平均值
    return sum(acc_test_lst) / len(acc_test_lst), sum(loss_test_lst) / len(loss_test_lst)




def test_semi_sep(net_g, w_all_k, dataset, group_dataset_test, args):
    acc_test_lst = []
    loss_test_lst = []
    for group_id, idxs in group_dataset_test.items():
        net_g.eval()
        # 每个block选择自己对应的w
        w = w_all_k[group_id]
        net_g.load_state_dict(w)
        # testing
        test_loss = 0
        correct = 0
        data_loader = DataLoader(DatasetSplit(dataset, idxs), batch_size=args.bs, shuffle=True)
        for idx, (data, target) in enumerate(data_loader):
            if args.gpu != -1:
                data, target = data.cuda(), target.cuda()
            log_probs = net_g(data)
            # sum up batch loss
            test_loss += F.cross_entropy(log_probs, target, reduction='sum').item()
            # get the index of the max log-probability
            y_pred = log_probs.data.max(1, keepdim=True)[1]
            correct += y_pred.eq(target.data.view_as(y_pred)).long().cpu().sum()

        test_loss /= len(data_loader.dataset)
        accuracy = 100.00 * correct / len(data_loader.dataset)
        acc_test_lst.append(accuracy)
        loss_test_lst.append(test_loss)
    print("sep, group_id", group_id, "acc_test_lst", acc_test_lst)
    # 返回这m个块测试的准确率的平均值
    return sum(acc_test_lst) / len(acc_test_lst), sum(loss_test_lst) / len(loss_test_lst)