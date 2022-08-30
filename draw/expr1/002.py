import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
from matplotlib.ticker import MaxNLocator
from tqdm import tqdm
import pickle

from utils import seed_all
from utils.options import args_parser
from utils.show import show_devices_partition
from utils.simulation import get_partition_lst, get_devices_locations, get_devices_download_latencies, get_devices_computation_latencies, \
    get_rate, opt_group_scheduled_devices, t_cp_k, t_up_k_no_broadcast, t_bc_k, t_bc_k_no_broadcast, get_round_k_time, \
    random_choice_scheduled_devices, random_choice_scheduled_devices_csame, random_group_scheduled_devices, \
    random_group_scheduled_devices_csame
from scipy import signal
from draw.options import *

args = args_parser()

# # mnist mlp
# args.dataset = 'mnist'
# args.data_num = 60000
# args.model_size = 5088320.0
# args.macs = 1588000.0
# args.num_users = 100
# args.C_path_loss = 100

# cifar mlp
args.dataset = 'cifar'
args.data_num = 50000
args.model_size = 19731520.0
args.macs = 6164000.0
args.num_users = 100
args.C_path_loss = 100

args.R = 600

args.epochs = 1500

args.seed = 1
seed_all(args.seed)

# 坐标(x, y) 设备位置
devices_locations = get_devices_locations(args)
# print("devices_locations", devices_locations)
# ms 设备下载时间
devices_download_latencies = get_devices_download_latencies(devices_locations, args)
# print("devices_download_latencies", devices_download_latencies)
# 设备计算时间
devices_computation_latencies = get_devices_computation_latencies(args)
# print("devices_computation_latencies", devices_computation_latencies)

# ms 设备上传给BS的时间
devices_upload_BS_latencies = [args.model_size / get_rate(args.P_device,
                                                          math.sqrt((devices_locations[i][0] ** 2) +
                                                                    (devices_locations[i][1] ** 2)), args) / 1000
                               for i in range(args.num_users)]  # s 基站给设备下发模型的延时

# s 设备上传给其他设备的时间，一个n*n的矩阵
devices_upload_device_latencies = [[0] * args.num_users for i in range(args.num_users)]
for from_ in range(args.num_users):
    for to_ in range(args.num_users):
        if from_ == to_:
            devices_upload_device_latencies[from_][to_] = 0
        else:
            devices_upload_device_latencies[from_][to_] = \
                args.model_size / get_rate(args.P_device,
                                           math.sqrt(
                                               ((devices_locations[from_][0] - devices_locations[to_][0]) ** 2) +
                                               ((devices_locations[from_][1] - devices_locations[to_][1]) ** 2)),
                                           args) / 1000

partition_lst = get_partition_lst(args, devices_download_latencies)
opt_order = list(range(len(partition_lst)))  # 由于只考虑广播下发，所以顺序不重要

opt_group_scheduled_devices_lst = opt_group_scheduled_devices(args, devices_download_latencies, opt_order)
random_choice_scheduled_devices_lst_c01 = random_choice_scheduled_devices(args, c=0.1)
random_group_scheduled_devices_lst_csame = random_group_scheduled_devices_csame(args, partition_lst)


group_number = 8


scheduled_devices_lst = opt_group_scheduled_devices_lst
partition_lst = scheduled_devices_lst[:group_number]
opt_group_lst = []
for sub_set in partition_lst:
    for i in sub_set:
        opt_group_lst.append(devices_download_latencies[i] * 1000)
    opt_group_lst.append(0)

x_lst = range(0, sum([len(group) for group in partition_lst]) + len(partition_lst))
loc_lst = []
count = 0
for group in partition_lst:
    loc_lst.append(count)
    count += len(group)
    count += 1


scheduled_devices_lst = random_group_scheduled_devices_lst_csame
partition_lst = scheduled_devices_lst[:group_number]
random_group_lst = []
for sub_set in partition_lst:
    for i in sub_set:
        random_group_lst.append(devices_download_latencies[i] * 1000)
    random_group_lst.append(0)

scheduled_devices_lst = random_choice_scheduled_devices_lst_c01
partition_lst = scheduled_devices_lst[:group_number]
fedavg_y_lst = []
fedavg_x_lst = []
count = 0
for sub_set_idx in range(len(partition_lst)):
    sub_set = partition_lst[sub_set_idx]
    for i in sub_set:
        fedavg_y_lst.append(devices_download_latencies[i] * 1000)
        fedavg_x_lst.append(count)
        count += 1

    # for i in range(len(opt_group_scheduled_devices_lst[sub_set_idx]) - len(sub_set) + 1):
    fedavg_y_lst.append(0)
    fedavg_x_lst.append(count)
    count += 1


fig = plt.figure(dpi=800)

ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

label_lst = list(range(1, group_number+1))

ax1.vlines(x_lst, [0], opt_group_lst)
ax1.set_ylabel('OptGroup', fontsize=draw_args.fontsize)
ax1.set_xticks(loc_lst)
ax1.set_xticklabels(label_lst)


ax2.vlines(x_lst, [0], random_group_lst)
ax2.set_ylabel('RandGoup', fontsize=draw_args.fontsize)
ax2.set_xticks(loc_lst)
ax2.set_xticklabels(label_lst)


ax3.vlines(fedavg_x_lst, [0], fedavg_y_lst)
ax3.set_ylabel('Unicast', fontsize=draw_args.fontsize)
loc_lst = list(range(0, (group_number)*11, 11))
ax3.set_xticks(loc_lst)
ax3.set_xticklabels(label_lst)
ax3.set_xlabel('Round', fontsize=draw_args.fontsize)


plt.savefig("C:\\Users\\tian\\Desktop\\figs\\{}_{}_3.pdf".format(args.dataset, args.R))



# 三张图分开画
figsize = (10, 3)

fig, ax1 = plt.subplots(dpi=800, figsize=figsize)
label_lst = list(range(1, group_number+1))

ax1.vlines(x_lst, [0], opt_group_lst, linewidth=3)
ax1.set_ylabel('Downloading Latency (ms)', fontsize=draw_args.fontsize2)
ax1.set_xticks(loc_lst)
ax1.set_xticklabels(label_lst)
ax1.set_xlabel('Round', fontsize=draw_args.fontsize)
fig.tight_layout()
plt.savefig("C:\\Users\\tian\\Desktop\\figs\\round_opt_group.pdf".format(args.dataset, args.R))


fig, ax2 = plt.subplots(dpi=800, figsize=figsize)
ax2.vlines(x_lst, [0], random_group_lst, linewidth=3)
ax2.set_ylabel('Downloading Latency (ms)', fontsize=draw_args.fontsize2)
ax2.set_xticks(loc_lst)
ax2.set_xticklabels(label_lst)
ax2.set_xlabel('Round', fontsize=draw_args.fontsize)
fig.tight_layout()
plt.savefig("C:\\Users\\tian\\Desktop\\figs\\round_random_group.pdf".format(args.dataset, args.R))


fig, ax3 = plt.subplots(dpi=800, figsize=figsize)
ax3.vlines(fedavg_x_lst, [0], fedavg_y_lst, linewidth=3)
ax3.set_ylabel('Downloading Latency (ms)', fontsize=draw_args.fontsize2)
loc_lst = list(range(0, (group_number)*11, 11))
ax3.set_xticks(loc_lst)
ax3.set_xticklabels(label_lst)
ax3.set_xlabel('Round', fontsize=draw_args.fontsize)
fig.tight_layout()
plt.savefig("C:\\Users\\tian\\Desktop\\figs\\round_fedavg.pdf".format(args.dataset, args.R))
