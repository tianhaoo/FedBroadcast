#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import copy
import torch
from torch import nn




def FedAvg(w, w_weights):
    w_avg = copy.deepcopy(w[0])
    for k in w_avg.keys():
        w_avg[k] *= w_weights[0]  # 先乘以第一个权重
    for k in w_avg.keys():
        for i in range(1, len(w)):
            w_avg[k] += w_weights[i] * w[i][k]  # 依次将后面的w乘权重累加起来
        w_avg[k] = torch.div(w_avg[k], sum(w_weights))  # 将总加和除以权值之和
    return w_avg


def get_w_avg(w_lst):
    w_avg = copy.deepcopy(w_lst[0])
    for k in w_avg.keys():
        for i in range(1, len(w_lst)):
            w_avg[k] += w_lst[i][k]
        w_avg[k] = torch.div(w_avg[k], len(w_lst))
    return w_avg