#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import torch
from torch import nn, autograd
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset
import copy
import numpy as np
import random
from sklearn import metrics
from thop import profile


class DatasetSplit(Dataset):
    def __init__(self, dataset, idxs):
        self.dataset = dataset
        self.idxs = list(idxs)

    def __len__(self):
        return len(self.idxs)

    def __getitem__(self, item):
        image, label = self.dataset[self.idxs[item]]
        return image, label


class LocalUpdate(object):
    def __init__(self, args, net_glob, dataset=None, idxs=None):
        self.args = args
        self.net_glob = net_glob
        self.loss_func = nn.CrossEntropyLoss()
        self.selected_clients = []
        self.ldr_train = DataLoader(DatasetSplit(dataset, idxs), batch_size=self.args.local_bs, shuffle=True)

    def reg_value(self, net):
        local_state_dict = net.state_dict()
        glob_state_dict = self.net_glob.state_dict()
        delta_state_dict = dict()
        for k in local_state_dict.keys():
            delta_state_dict[k] = local_state_dict[k] - glob_state_dict[k]

        delta_net = copy.deepcopy(self.net_glob).to(self.args.device)
        delta_net.load_state_dict(delta_state_dict)

        l2_reg = None
        for W in delta_net.parameters():
            if l2_reg is None:
                l2_reg = W.norm(2)
            else:
                l2_reg = l2_reg + W.norm(2)
        # l2_reg = Variable(torch.FloatTensor(1), requires_grad=True).to(self.args.device)
        # for W in delta_net.parameters():
        #     l2_reg = l2_reg + W.norm(2)
        return 0.5 * self.args.rho * l2_reg

    def train(self, net):
        net.train()
        # train and update
        # optimizer = torch.optim.SGD(net.parameters(), lr=self.args.lr, momentum=self.args.momentum, weight_decay=0.1)
        optimizer = torch.optim.SGD(net.parameters(), lr=self.args.lr, momentum=self.args.momentum)
        # optimizer = torch.optim.SGD(net.parameters(), lr=self.args.lr)

        epoch_loss = []
        if self.args.semi:
            local_ep = self.args.semi_local_ep
        else:
            local_ep = self.args.local_ep
        for iter in range(local_ep):
            batch_loss = []
            for batch_idx, (images, labels) in enumerate(self.ldr_train):
                images, labels = images.to(self.args.device), labels.to(self.args.device)
                net.zero_grad()
                log_probs = net(images)
                # a = self.loss_func(log_probs, labels)
                # b = self.reg_value(net)
                # print(a, b)
                # loss = a + b  # 可以打印出来，注意两者的绝对值差距，可以用rho调整
                loss = self.loss_func(log_probs, labels)
                loss.backward()
                optimizer.step()

                if self.args.verbose and batch_idx % 10 == 0:
                    print('Update Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                        iter, batch_idx * len(images), len(self.ldr_train.dataset),
                               100. * batch_idx / len(self.ldr_train), loss.item()))
                batch_loss.append(loss.item())
            epoch_loss.append(sum(batch_loss)/len(batch_loss))
        return net.state_dict(), sum(epoch_loss) / len(epoch_loss)

# semi用到的本地更新
class SemiLocalUpdate(object):
    def __init__(self, args, net_glob, dataset=None, idxs=None, day=None):
        self.args = args
        self.net_glob = net_glob
        self.loss_func = nn.CrossEntropyLoss()
        self.selected_clients = []
        self.ldr_train = DataLoader(DatasetSplit(dataset, idxs), batch_size=self.args.local_bs, shuffle=True)

    def train(self, net):
        net.train()
        # train and update
        # optimizer = torch.optim.SGD(net.parameters(), lr=self.args.lr, momentum=self.args.momentum, weight_decay=0.1)
        optimizer = torch.optim.SGD(net.parameters(), lr=self.args.lr, momentum=self.args.momentum)
        # optimizer = torch.optim.SGD(net.parameters(), lr=self.args.lr)

        epoch_loss = []
        for iter in range(self.args.semi_local_ep):
            batch_loss = []
            for batch_idx, (images, labels) in enumerate(self.ldr_train):
                images, labels = images.to(self.args.device), labels.to(self.args.device)
                net.zero_grad()
                log_probs = net(images)
                # a = self.loss_func(log_probs, labels)
                # b = self.reg_value(net)
                # print(a, b)
                # loss = a + b  # 可以打印出来，注意两者的绝对值差距，可以用rho调整
                loss = self.loss_func(log_probs, labels)
                loss.backward()
                optimizer.step()

                if self.args.verbose and batch_idx % 10 == 0:
                    print('Update Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                        iter, batch_idx * len(images), len(self.ldr_train.dataset),
                               100. * batch_idx / len(self.ldr_train), loss.item()))
                batch_loss.append(loss.item())
            epoch_loss.append(sum(batch_loss)/len(batch_loss))
        return net.state_dict(), sum(epoch_loss) / len(epoch_loss)
