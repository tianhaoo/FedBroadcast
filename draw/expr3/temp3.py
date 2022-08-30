import math

import matplotlib.pyplot as plt
import pickle

from utils import seed_all
from utils.options import args_parser
from scipy import signal
import os
from tqdm import tqdm
from draw.options import *

from utils.simulation import get_devices_download_latencies, get_devices_locations, \
    get_devices_computation_latencies, get_rate, get_partition_lst, opt_group_scheduled_devices, \
    random_choice_scheduled_devices, random_choice_scheduled_devices_csame, random_group_scheduled_devices, \
    random_group_scheduled_devices_csame, get_round_k_time


def get_min_average_max(root_path, record_path_lst):

    acc_test_lst_min_lst = []
    acc_test_lst_average_lst = []
    acc_test_lst_max_lst = []

    record_lst = [pickle.load(open(os.path.join(root_path, record_path), 'rb')) for record_path in record_path_lst]

    for i in range(1000):
        acc_lst = []
        for record in record_lst:
            acc_test_lst = record["acc_test_lst"]
            acc_lst.append(acc_test_lst[i])

        acc_test_lst_min_lst.append(min(acc_lst))
        acc_test_lst_average_lst.append(sum(acc_lst)/len(acc_lst))
        acc_test_lst_max_lst.append(max(acc_lst))

    return acc_test_lst_min_lst, acc_test_lst_average_lst, acc_test_lst_max_lst







if __name__ == "__main__":
    # mnist iid 2 张 acc loss
    fedavg_record_path_lst = [
        "fed_seed1_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed2_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed3_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed4_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed5_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed6_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed7_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed8_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed9_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
        "fed_seed10_cifar_mlp_1000_C0.1_iidTrue.fedAvg.record",
    ]
    group_record_path_lst = [
        "fed_seed1_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed2_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed3_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed4_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed5_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed6_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed7_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed8_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed9_cifar_mlp_1000_C0.1_iidTrue.group.record",
        "fed_seed10_cifar_mlp_1000_C0.1_iidTrue.group.record",
    ]
    root_path = "C:\\Users\\tiana\\PycharmProjects\\FedBroadcast\\main_fed_save"
    fedavg_acc_test_lst_min_lst, fedavg_acc_test_lst_average_lst, fedavg_acc_test_lst_max_lst = \
    get_min_average_max(root_path, fedavg_record_path_lst)
    group_acc_test_lst_min_lst, group_acc_test_lst_average_lst, group_acc_test_lst_max_lst = \
    get_min_average_max(root_path, group_record_path_lst)





    # 开始计算时间
    opt_group_time_lst_lst = []  # 最优分组 广播下发
    random_choice_time_lst_lst = []  # 每轮10个，真随机抽 不广播下发
    random_group_time_lst_lst = []  # 每轮10个，真随机分组 不广播下发
    for seed in tqdm(range(100)):

        # 1. mnist mlp  model_size=5088320.0, macs=1588000.0
        # 2. cifar mlp  model_size=19731520.0, macs=6164000.0

        args = args_parser()
        args.seed = seed
        seed_all(args.seed)

        # # mnist mlp
        # args.dataset = 'mnist'
        # args.data_num = 60000
        # args.model_size = 5088320.0
        # args.macs = 1588000.0
        # args.C_path_loss = 100

        # cifar mlp
        args.dataset = 'cifar'
        args.data_num = 50000
        args.model_size = 19731520.0
        args.macs = 6164000.0
        args.num_users = 100
        args.C_path_loss = 100

        args.iid = True
        args.R = 600
        args.num_users = 100
        args.epochs = 1000

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
        random_choice_scheduled_devices_lst = random_choice_scheduled_devices_csame(args, partition_lst)
        random_group_scheduled_devices_lst = random_group_scheduled_devices_csame(args, partition_lst)

        opt_group_time_lst = []  # 最优分组 广播下发
        random_choice_time_lst = []  # 每轮10个，真随机抽 不广播下发
        random_group_time_lst = []  # 每轮10个，真随机分组 不广播下发

        for k in range(1, args.epochs):
            # 最优分组
            scheduled_devices = opt_group_scheduled_devices_lst
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])


            # 最优分组，广播下发
            t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                         devices_upload_BS_latencies, devices_upload_device_latencies,
                                         broadcast_download=True, broadcast_upload=False, add_computation_latency=True)
            opt_group_time_lst.append(t_round_k)


            # 随机抽取
            scheduled_devices = random_choice_scheduled_devices_lst
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])

            # 随机抽取 不广播下发
            t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                         devices_upload_BS_latencies, devices_upload_device_latencies,
                                         broadcast_download=False, broadcast_upload=False, add_computation_latency=True)
            random_choice_time_lst.append(t_round_k)


            # 随机分组1
            scheduled_devices = random_group_scheduled_devices_lst
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])

            # 随机分组1 不广播下发
            t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                         devices_upload_BS_latencies, devices_upload_device_latencies,
                                         broadcast_download=False, broadcast_upload=False, add_computation_latency=True)
            random_group_time_lst.append(t_round_k)

        opt_group_time_lst_lst.append(opt_group_time_lst)
        random_choice_time_lst_lst.append(random_choice_time_lst)
        random_group_time_lst_lst.append(random_group_time_lst)

    opt_group_average_time_lst = []
    for i in range(len(opt_group_time_lst_lst[0])):
        temp = []
        for opt_group_time_lst in opt_group_time_lst_lst:
            temp.append(opt_group_time_lst[i])
        opt_group_average_time_lst.append(sum(temp)/len(temp))

    random_choice_average_time_lst = []
    for i in range(len(random_choice_time_lst_lst[0])):
        temp = []
        for random_choice_time_lst in random_choice_time_lst_lst:
            temp.append(random_choice_time_lst[i])
        random_choice_average_time_lst.append(sum(temp)/len(temp))

    random_group_average_time_lst = []
    for i in range(len(random_group_time_lst_lst[0])):
        temp = []
        for random_group_time_lst in random_group_time_lst_lst:
            temp.append(random_group_time_lst[i])
        random_group_average_time_lst.append(sum(temp)/len(temp))



    print(sum(opt_group_average_time_lst))
    print(sum(random_choice_average_time_lst))
    print(sum(random_group_average_time_lst))

    print(opt_group_average_time_lst)
    print(random_choice_average_time_lst)
    print(random_group_average_time_lst)

    opt_group_average_time_lst.append(opt_group_average_time_lst[-1])
    s = 0
    opt_group_x_lst = []
    for i in opt_group_average_time_lst:
        s += i
        opt_group_x_lst.append(s)

    random_choice_average_time_lst.append(random_choice_average_time_lst[-1])
    s = 0
    random_choice_x_lst = []
    for i in random_choice_average_time_lst:
        s += i
        random_choice_x_lst.append(s)

    random_group_average_time_lst.append(random_group_average_time_lst[-1])
    s = 0
    random_group_x_lst = []
    for i in random_group_average_time_lst:
        s += i
        random_group_x_lst.append(s)


    # 画图
    fig, ax = plt.subplots(dpi=800)

    ax.fill_between(random_choice_x_lst, fedavg_acc_test_lst_min_lst, fedavg_acc_test_lst_max_lst, alpha=0.3, linewidth=1)
    ax.plot(random_choice_x_lst, signal.savgol_filter(fedavg_acc_test_lst_average_lst, 47, 3), label="Unicast", linewidth=2)

    ax.fill_between(random_group_x_lst, group_acc_test_lst_min_lst, group_acc_test_lst_max_lst, alpha=0.3, linewidth=1)
    ax.plot(random_group_x_lst, signal.savgol_filter(group_acc_test_lst_average_lst, 47, 3), label="Broadcast-RandGroup", linewidth=2)

    ax.fill_between(opt_group_x_lst, group_acc_test_lst_min_lst, group_acc_test_lst_max_lst, alpha=0.3, linewidth=1)
    ax.plot(opt_group_x_lst, signal.savgol_filter(group_acc_test_lst_average_lst, 47, 3), label="Broadcast-OptGroup", linewidth=2)




    ax.set_ylabel('Test Accuracy (%)', label_font)
    ax.set_xlabel("Time (s)", label_font)
    ax.set_xlim(0, 3500)
    ax.set_ylim(53, 55.1)
    ax.legend(loc='lower right', prop=legend_font)
    fig.tight_layout()
    plt.savefig("C:\\Users\\tiana\\Desktop\\figs3\\{}_{}_iid{}_test_acc.pdf".format(args.dataset, args.R, args.iid))
    plt.show()