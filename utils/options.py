#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import argparse

def args_parser():
    parser = argparse.ArgumentParser()
    # torch参数
    parser.add_argument('--gpu', type=int, default=0, help="GPU ID, -1 for CPU")
    parser.add_argument('--seed', type=int, default=1, help='随即发生器种子 (default: 1)')
    parser.add_argument('--verbose', action='store_true', help='verbose print')

    # 联邦学习参数
    parser.add_argument('--type', type=str, default='fedAvg', help="每轮选取客户端的方式：fedAvg/group")
    parser.add_argument('--epochs', type=int, default=50, help="训练轮数")
    parser.add_argument('--num_users', type=int, default=100, help="设备数量：K")
    parser.add_argument('--frac', type=float, default=0.1, help="每轮选取的设备比例: C")
    parser.add_argument('--local_ep', type=int, default=5, help="本地训练轮数: E")
    parser.add_argument('--local_bs', type=int, default=10, help="本地训练 batch size: B")
    parser.add_argument('--dataset', type=str, default='mnist', help="数据集名称")
    parser.add_argument('--data_num', type=int, default=0, help="训练集的数据数量")
    parser.add_argument('--iid', action='store_true', help='是否是 i.i.d')

    # semi参数
    parser.add_argument('--semi', action='store_true', help="是否是semi-non-iid")
    parser.add_argument('--semi_local_ep', type=int, default=1, help="本地epoch数量")
    parser.add_argument('--semi_type', type=str, default='fb', help="fb/sep/pla/fedavg/rr ")
    parser.add_argument('--semi_K', type=int, default=10, help="天数，k in [1,k] cycle数量")
    parser.add_argument('--semi_m', type=int, default=0, help="块数，i in [1, m] block数量")
    parser.add_argument('--semi_n', type=int, default=0, help="块里的数据样本个数，j in [1, n] 每个block的数据数量")

    # 训练参数
    parser.add_argument('--model', type=str, default='mlp', help='模型名称 mlp / cnn')
    parser.add_argument('--bs', type=int, default=128, help="测试 batch size")
    parser.add_argument('--lr', type=float, default=0.01, help="学习率")
    parser.add_argument('--decay', type=float, default=0.99, help="learning rate decay (default: 0.99)")
    parser.add_argument('--momentum', type=float, default=0.5, help="SGD momentum (default: 0.5)")
    parser.add_argument('--rho', type=float, default=0.2, help="L2 regularization param (default: 0.1)")

    # 物理环境模拟参数
    parser.add_argument('--R', type=int, default=600, help="半径 m")
    parser.add_argument('--alpha', type=int, default=3.76, help="代表path loss指数，可用于求path loss")
    parser.add_argument('--N0', type=int, default=-114, help="噪声  dBm/MHz")
    parser.add_argument('--C_path_loss', type=int, default=100, help="path loss要加上这个常数，数字越大，传输速度越慢")
    parser.add_argument('--B', type=int, default=20, help="总带宽  MHz")
    parser.add_argument('--cpu_frequency', type=int, default=1e9, help="设备的计算能力 1GHz/s")
    parser.add_argument('--P_base_station', type=int, default=20, help="基站的传输功率 dBm")
    parser.add_argument('--P_device', type=int, default=10, help="设备的传输功率 dBm")
    parser.add_argument('--model_size', type=int, default=0, help="模型大小 bit")
    parser.add_argument('--macs', type=int, default=0, help="计算量 多少次mac操作")

    args = parser.parse_args()


    return args
