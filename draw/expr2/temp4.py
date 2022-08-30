import math

import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle

from utils import seed_all
from utils.options import args_parser
from utils.show import show_devices_partition
from utils.simulation import get_partition_lst, get_devices_locations, get_devices_download_latencies, \
    get_devices_computation_latencies, \
    get_rate, opt_group_scheduled_devices, t_cp_k, t_up_k_no_broadcast, t_bc_k, t_bc_k_no_broadcast, get_round_k_time, \
    get_opt_order, opt_pi_k_save, random_choice_scheduled_devices, random_group_scheduled_devices
from scipy import signal
import os
from draw.options import *

# 随机抽取、随机分组和最优分组、 使用广播下发和不使用广播下发、 在每轮设备数量相同的情况下，求每轮的平均时间



x_lst = list(range(11, 41))
opt_group_x_lst = x_lst
random_choice_x_lst_c1 = x_lst
random_choice_x_lst_c2 = x_lst
random_choice_x_lst_c3 = x_lst
random_group_x_lst_c1 = x_lst
random_group_x_lst_c2 = [i for i in x_lst if i % 2 == 0]
random_group_x_lst_c3 = [i for i in x_lst if i % 3 == 0]

print(x_lst)
print(random_group_x_lst_c2)



opt_group_broadcast_download_y_lst = []
opt_group_broadcast_upload_y_lst = []
random_choice_broadcast_download_y_lst_c1 = []
random_choice_broadcast_upload_y_lst_c1 = []
random_choice_broadcast_download_y_lst_c2 = []
random_choice_broadcast_upload_y_lst_c2 = []
random_choice_broadcast_download_y_lst_c3 = []
random_choice_broadcast_upload_y_lst_c3 = []
random_group_broadcast_download_y_lst_c1 = []
random_group_broadcast_upload_y_lst_c1 = []
random_group_broadcast_download_y_lst_c2 = []
random_group_broadcast_upload_y_lst_c2 = []
random_group_broadcast_download_y_lst_c3 = []
random_group_broadcast_upload_y_lst_c3 = []

for num_users in x_lst:
    print("num_users", num_users)

    opt_group_broadcast_average_lst = []
    opt_group_broadcast_upload_average_lst = []
    random_choice_broadcast_average_lst_c1 = []
    random_choice_broadcast_upload_average_lst_c1 = []
    random_choice_broadcast_average_lst_c2 = []
    random_choice_broadcast_upload_average_lst_c2 = []
    random_choice_broadcast_average_lst_c3 = []
    random_choice_broadcast_upload_average_lst_c3 = []
    random_group_broadcast_average_lst_c1 = []
    random_group_broadcast_upload_average_lst_c1 = []
    random_group_broadcast_average_lst_c2 = []
    random_group_broadcast_upload_average_lst_c2 = []
    random_group_broadcast_average_lst_c3 = []
    random_group_broadcast_upload_average_lst_c3 = []

    for seed in tqdm(range(3)):
        pass

        # 1. mnist mlp  model_size=5088320.0, macs=1588000.0
        # 2. cifar mlp  model_size=19731520.0, macs=6164000.0

        args = args_parser()

        # # mnist mlp
        # args.dataset = 'mnist'
        # args.data_num = 60000
        # args.model_size = 5088320.0
        # args.macs = 1588000.0
        # args.frac = 0.1
        # args.C_path_loss = 100

        # cifar mlp
        args.dataset = 'cifar'
        args.data_num = 50000
        args.model_size = 19731520.0
        args.macs = 6164000.0
        args.frac = 0.1
        args.C_path_loss = 100


        args.R = 600
        args.epochs = 1000
        args.num_users = num_users
        args.seed = seed
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
        # 只广播下发的pi
        opt_order = list(range(len(partition_lst)))  # 由于只考虑广播下发，所以顺序不重要
        opt_group_scheduled_devices_lst = opt_group_scheduled_devices(args, devices_download_latencies, opt_order)
        # 还要广播上传的pi
        # print(partition_lst)
        # opt_order = get_opt_order(partition_lst, devices_download_latencies, devices_computation_latencies,
        #               devices_upload_BS_latencies, devices_upload_device_latencies)
        # TODO:// 用下发时间，而不是整轮时间 考虑顺序

        random_choice_scheduled_devices_lst_c1 = random_choice_scheduled_devices(args, m_times_c=1)
        random_choice_scheduled_devices_lst_c2 = random_choice_scheduled_devices(args, m_times_c=2)
        random_choice_scheduled_devices_lst_c3 = random_choice_scheduled_devices(args, m_times_c=3)
        random_group_scheduled_devices_lst_c1 = random_group_scheduled_devices(args, m_times_c=1)
        random_group_scheduled_devices_lst_c2 = random_group_scheduled_devices(args, m_times_c=2)
        random_group_scheduled_devices_lst_c3 = random_group_scheduled_devices(args, m_times_c=3)

        round_lst = []
        opt_group_broadcast_time = 0
        opt_group_broadcast_upload_time = 0
        random_choice_broadcast_time_c1 = 0
        random_choice_broadcast_upload_time_c1 = 0
        random_choice_broadcast_time_c2 = 0
        random_choice_broadcast_upload_time_c2 = 0
        random_choice_broadcast_time_c3 = 0
        random_choice_broadcast_upload_time_c3 = 0
        random_group_broadcast_time_c1 = 0
        random_group_broadcast_upload_time_c1 = 0
        random_group_broadcast_time_c2 = 0
        random_group_broadcast_upload_time_c2 = 0
        random_group_broadcast_time_c3 = 0
        random_group_broadcast_upload_time_c3 = 0

        opt_group_broadcast_time_lst = []  # 最优分组 广播下发
        opt_group_broadcast_upload_time_lst = []  # 最优分组 广播上传
        random_choice_broadcast_time_lst_c1 = []  # 每轮=10个， 广播下发
        random_choice_broadcast_upload_time_lst_c1 = []  # 每轮=10个， 广播上传
        random_choice_broadcast_time_lst_c2 = []  # 每轮>=10个，每轮个数和opt_group一样 广播下发
        random_choice_broadcast_upload_time_lst_c2 = []  # 每轮>=10个，每轮个数和opt_group一样 广播上传
        random_choice_broadcast_time_lst_c3 = []  #
        random_choice_broadcast_upload_time_lst_c3 = []  #
        random_group_broadcast_time_lst_c1 = []  # 每轮=10个， 广播下发
        random_group_broadcast_upload_time_lst_c1 = []  # 每轮=10个， 广播上传
        random_group_broadcast_time_lst_c2 = []  # 每轮>=10个，每轮个数和opt_group一样 广播下发
        random_group_broadcast_upload_time_lst_c2 = []  # 每轮>=10个，每轮个数和opt_group一样 广播上传
        random_group_broadcast_time_lst_c3 = []  #
        random_group_broadcast_upload_time_lst_c3 = []  #

        for k in range(1, args.epochs):
            round_lst.append(k)

            ###########################
            # 最优分组
            if num_users in opt_group_x_lst:
                scheduled_devices = opt_group_scheduled_devices_lst
                pi_k_minus_1 = set(scheduled_devices[k - 1])
                pi_k = set(scheduled_devices[k])

                # 最优分组，广播下发
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=False, add_computation_latency=False)
                # t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
                opt_group_broadcast_time += t_round_k
                opt_group_broadcast_time_lst.append(t_round_k)


                # 最优分组，广播上传
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=True, add_computation_latency=False)
                # pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                #                           devices_upload_device_latencies)
                # t_round_k = t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
                opt_group_broadcast_upload_time += t_round_k
                opt_group_broadcast_upload_time_lst.append(t_round_k)
            ###########################

            ###########################
            # 随机抽取1
            if num_users in random_choice_x_lst_c1:
                scheduled_devices = random_choice_scheduled_devices_lst_c1
                pi_k_minus_1 = set(scheduled_devices[k - 1])
                pi_k = set(scheduled_devices[k])

                # 随机抽取1，广播下发
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=False, add_computation_latency=False)
                # t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
                random_choice_broadcast_time_c1 += t_round_k
                random_choice_broadcast_time_lst_c1.append(t_round_k)

                # 随机抽取1，广播上传
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=True, add_computation_latency=False)
                # pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                #                           devices_upload_device_latencies)
                # t_round_k = t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
                random_choice_broadcast_upload_time_c1 += t_round_k
                random_choice_broadcast_upload_time_lst_c1.append(t_round_k)
            ###########################


            ###########################
            # 随机抽取2
            if num_users in random_choice_x_lst_c2:
                scheduled_devices = random_choice_scheduled_devices_lst_c2
                pi_k_minus_1 = set(scheduled_devices[k - 1])
                pi_k = set(scheduled_devices[k])

                # 随机抽取2，广播下发
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=False, add_computation_latency=False)
                # t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
                random_choice_broadcast_time_c2 += t_round_k
                random_choice_broadcast_time_lst_c2.append(t_round_k)

                # 随机抽取2，广播上传
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=True, add_computation_latency=False)
                # pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                #                           devices_upload_device_latencies)
                # t_round_k = t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
                random_choice_broadcast_upload_time_c2 += t_round_k
                random_choice_broadcast_upload_time_lst_c2.append(t_round_k)
            ###########################

            ###########################
            # 随机抽取3
            if num_users in random_choice_x_lst_c3:
                scheduled_devices = random_choice_scheduled_devices_lst_c3
                pi_k_minus_1 = set(scheduled_devices[k - 1])
                pi_k = set(scheduled_devices[k])

                # 随机抽取3，广播下发
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies,
                                             devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=False,
                                             add_computation_latency=False)
                # t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
                random_choice_broadcast_time_c3 += t_round_k
                random_choice_broadcast_time_lst_c3.append(t_round_k)

                # 随机抽取3，广播上传
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies,
                                             devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=True,
                                             add_computation_latency=False)
                # pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                #                           devices_upload_device_latencies)
                # t_round_k = t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
                random_choice_broadcast_upload_time_c3 += t_round_k
                random_choice_broadcast_upload_time_lst_c3.append(t_round_k)
            ###########################

            ###########################
            # 随机分组1
            if num_users in random_group_x_lst_c1:
                scheduled_devices = random_group_scheduled_devices_lst_c1
                pi_k_minus_1 = set(scheduled_devices[k - 1])
                pi_k = set(scheduled_devices[k])

                # # 随机分组1，广播下发
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=False, add_computation_latency=False)
                # t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
                random_group_broadcast_time_c1 += t_round_k
                random_group_broadcast_time_lst_c1.append(t_round_k)

                # 随机分组1，广播上传
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=True, add_computation_latency=False)
                # pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                #                           devices_upload_device_latencies)
                # t_round_k = t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
                random_group_broadcast_upload_time_c1 += t_round_k
                random_group_broadcast_upload_time_lst_c1.append(t_round_k)
            ###########################

            ###########################
            # 随机分组2
            if num_users in random_group_x_lst_c2:
                scheduled_devices = random_group_scheduled_devices_lst_c2
                pi_k_minus_1 = set(scheduled_devices[k - 1])
                pi_k = set(scheduled_devices[k])


                # 随机分组2，广播下发
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=False, add_computation_latency=False)
                # t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
                random_group_broadcast_time_c2 += t_round_k
                random_group_broadcast_time_lst_c2.append(t_round_k)

                # 随机分组2，广播上传
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=True, add_computation_latency=False)
                # pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                #                           devices_upload_device_latencies)
                # t_round_k = t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
                random_group_broadcast_upload_time_c2 += t_round_k
                random_group_broadcast_upload_time_lst_c2.append(t_round_k)
            ###########################

            ###########################
            # 随机分组3
            if num_users in random_group_x_lst_c3:
                scheduled_devices = random_group_scheduled_devices_lst_c3
                pi_k_minus_1 = set(scheduled_devices[k - 1])
                pi_k = set(scheduled_devices[k])


                # 随机分组3，广播下发
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=False, add_computation_latency=False)
                # t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
                random_group_broadcast_time_c3 += t_round_k
                random_group_broadcast_time_lst_c3.append(t_round_k)

                # 随机分组3，广播上传
                t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                                             devices_upload_BS_latencies, devices_upload_device_latencies,
                                             broadcast_download=True, broadcast_upload=True, add_computation_latency=False)
                # pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                #                           devices_upload_device_latencies)
                # t_round_k = t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
                random_group_broadcast_upload_time_c3 += t_round_k
                random_group_broadcast_upload_time_lst_c3.append(t_round_k)
            ###########################


        # print("最优分组，广播", sum(opt_group_broadcast_time_lst)/len(opt_group_broadcast_time_lst))
        if opt_group_broadcast_time_lst:
            opt_group_broadcast_average_lst.append(sum(opt_group_broadcast_time_lst)/len(opt_group_broadcast_time_lst))

        # print("最优分组，广播上传", sum(opt_group_broadcast_upload_time_lst)/len(opt_group_broadcast_upload_time_lst))
        if opt_group_broadcast_upload_time_lst:
            opt_group_broadcast_upload_average_lst.append(sum(opt_group_broadcast_upload_time_lst)/len(opt_group_broadcast_upload_time_lst))

        # print("随机抽取1，广播", sum(random_choice_broadcast_time_lst1)/len(random_choice_broadcast_time_lst1))
        if random_choice_broadcast_time_lst_c1:
            random_choice_broadcast_average_lst_c1.append(sum(random_choice_broadcast_time_lst_c1) / len(random_choice_broadcast_time_lst_c1))

        # print("随机抽取1，广播上传", sum(random_choice_broadcast_upload_time_lst1)/len(random_choice_broadcast_upload_time_lst1))
        if random_choice_broadcast_upload_time_lst_c1:
            random_choice_broadcast_upload_average_lst_c1.append(sum(random_choice_broadcast_upload_time_lst_c1) / len(random_choice_broadcast_upload_time_lst_c1))


        # print("随机抽取2，广播", sum(random_choice_broadcast_time_lst2)/len(random_choice_broadcast_time_lst2))
        if random_choice_broadcast_time_lst_c2:
            random_choice_broadcast_average_lst_c2.append(sum(random_choice_broadcast_time_lst_c2) / len(random_choice_broadcast_time_lst_c2))

        # print("随机抽取2，广播上传", sum(random_choice_broadcast_upload_time_lst2)/len(random_choice_broadcast_upload_time_lst2))
        if random_choice_broadcast_upload_time_lst_c2:
            random_choice_broadcast_upload_average_lst_c2.append(sum(random_choice_broadcast_upload_time_lst_c2) / len(random_choice_broadcast_upload_time_lst_c2))



        if random_choice_broadcast_time_lst_c3:
            random_choice_broadcast_average_lst_c3.append(sum(random_choice_broadcast_time_lst_c3) / len(random_choice_broadcast_time_lst_c3))

        if random_choice_broadcast_upload_time_lst_c3:
            random_choice_broadcast_upload_average_lst_c3.append(sum(random_choice_broadcast_upload_time_lst_c3) / len(random_choice_broadcast_upload_time_lst_c3))




        # print("随机分组1，广播", sum(random_group_broadcast_time_lst1)/len(random_group_broadcast_time_lst1))
        if random_group_broadcast_time_lst_c1:
            random_group_broadcast_average_lst_c1.append(sum(random_group_broadcast_time_lst_c1) / len(random_group_broadcast_time_lst_c1))

        # print("随机分组1，广播上传", sum(random_group_broadcast_upload_time_lst1)/len(random_group_broadcast_upload_time_lst1))
        if random_group_broadcast_upload_time_lst_c1:
            random_group_broadcast_upload_average_lst_c1.append(sum(random_group_broadcast_upload_time_lst_c1) / len(random_group_broadcast_upload_time_lst_c1))

        # print("随机分组2，广播", sum(random_group_broadcast_time_lst2)/len(random_group_broadcast_time_lst2))
        if random_group_broadcast_time_lst_c2:
            random_group_broadcast_average_lst_c2.append(sum(random_group_broadcast_time_lst_c2) / len(random_group_broadcast_time_lst_c2))

        # print("随机分组2，广播上传", sum(random_group_broadcast_upload_time_lst2)/len(random_group_broadcast_upload_time_lst2))
        if random_group_broadcast_upload_time_lst_c2:
            random_group_broadcast_upload_average_lst_c2.append(sum(random_group_broadcast_upload_time_lst_c2) / len(random_group_broadcast_upload_time_lst_c2))


        if random_group_broadcast_time_lst_c3:
            random_group_broadcast_average_lst_c3.append(sum(random_group_broadcast_time_lst_c3) / len(random_group_broadcast_time_lst_c3))

        if random_group_broadcast_upload_time_lst_c3:
            random_group_broadcast_upload_average_lst_c3.append(sum(random_group_broadcast_upload_time_lst_c3) / len(random_group_broadcast_upload_time_lst_c3))



    # 毫秒
    if opt_group_broadcast_average_lst:
        opt_group_broadcast_download_y_lst.append(sum(opt_group_broadcast_average_lst) / len(opt_group_broadcast_average_lst) * 1000)
    if opt_group_broadcast_upload_average_lst:
        opt_group_broadcast_upload_y_lst.append(sum(opt_group_broadcast_upload_average_lst) / len(opt_group_broadcast_upload_average_lst) * 1000)
    if random_choice_broadcast_average_lst_c1:
        random_choice_broadcast_download_y_lst_c1.append(sum(random_choice_broadcast_average_lst_c1) / len(random_choice_broadcast_average_lst_c1) * 1000)
    if random_choice_broadcast_upload_average_lst_c1:
        random_choice_broadcast_upload_y_lst_c1.append(sum(random_choice_broadcast_upload_average_lst_c1) / len(random_choice_broadcast_upload_average_lst_c1) * 1000)
    if random_choice_broadcast_average_lst_c2:
        random_choice_broadcast_download_y_lst_c2.append(sum(random_choice_broadcast_average_lst_c2) / len(random_choice_broadcast_average_lst_c2) * 1000)
    if random_choice_broadcast_upload_average_lst_c2:
        random_choice_broadcast_upload_y_lst_c2.append(sum(random_choice_broadcast_upload_average_lst_c2) / len(random_choice_broadcast_upload_average_lst_c2) * 1000)
    if random_choice_broadcast_average_lst_c3:
        random_choice_broadcast_download_y_lst_c3.append(sum(random_choice_broadcast_average_lst_c3) / len(random_choice_broadcast_average_lst_c3) * 1000)
    if random_choice_broadcast_upload_average_lst_c3:
        random_choice_broadcast_upload_y_lst_c3.append(sum(random_choice_broadcast_upload_average_lst_c3) / len(random_choice_broadcast_upload_average_lst_c3) * 1000)

    if random_group_broadcast_average_lst_c1:
        random_group_broadcast_download_y_lst_c1.append(sum(random_group_broadcast_average_lst_c1) / len(random_group_broadcast_average_lst_c1) * 1000)
    if random_group_broadcast_upload_average_lst_c1:
        random_group_broadcast_upload_y_lst_c1.append(sum(random_group_broadcast_upload_average_lst_c1) / len(random_group_broadcast_upload_average_lst_c1) * 1000)
    if random_group_broadcast_average_lst_c2:
        random_group_broadcast_download_y_lst_c2.append(sum(random_group_broadcast_average_lst_c2) / len(random_group_broadcast_average_lst_c2) * 1000)
    if random_group_broadcast_upload_average_lst_c2:
        random_group_broadcast_upload_y_lst_c2.append(sum(random_group_broadcast_upload_average_lst_c2) / len(random_group_broadcast_upload_average_lst_c2) * 1000)
    if random_group_broadcast_average_lst_c3:
        random_group_broadcast_download_y_lst_c3.append(sum(random_group_broadcast_average_lst_c3) / len(random_group_broadcast_average_lst_c3) * 1000)
    if random_group_broadcast_upload_average_lst_c3:
        random_group_broadcast_upload_y_lst_c3.append(sum(random_group_broadcast_upload_average_lst_c3) / len(random_group_broadcast_upload_average_lst_c3) * 1000)


# 五种调度通过上传节省的百分比比较

# 五种调度放在一起
fig, ax = plt.subplots(dpi=800)
ax.plot(opt_group_x_lst, [(1-opt_group_broadcast_upload_y_lst[i]/opt_group_broadcast_download_y_lst[i])*100
                for i in range(len(opt_group_x_lst))], label="Broadcast-OptGroup")

ax.plot(random_choice_x_lst_c1, [(1 - random_choice_broadcast_upload_y_lst_c1[i] / random_choice_broadcast_download_y_lst_c1[i]) * 100
                for i in range(len(random_choice_x_lst_c1))], label="Unicast n=1")

ax.plot(random_choice_x_lst_c2, [(1 - random_choice_broadcast_upload_y_lst_c2[i] / random_choice_broadcast_download_y_lst_c2[i]) * 100
                for i in range(len(random_choice_x_lst_c2))], label="Unicast n=2")

ax.plot(random_choice_x_lst_c3, [(1 - random_choice_broadcast_upload_y_lst_c3[i] / random_choice_broadcast_download_y_lst_c3[i]) * 100
                for i in range(len(random_choice_x_lst_c3))], label="Unicast n=3")


ax.plot(random_group_x_lst_c1, [(1 - random_group_broadcast_upload_y_lst_c1[i] / random_group_broadcast_download_y_lst_c1[i]) * 100
                for i in range(len(random_group_x_lst_c1))], label="Broadcast-RandGroup n=1")

ax.plot(random_group_x_lst_c2, [(1 - random_group_broadcast_upload_y_lst_c2[i] / random_group_broadcast_download_y_lst_c2[i]) * 100
                for i in range(len(random_group_x_lst_c2))], label="Broadcast-RandGroup n=2")

ax.plot(random_group_x_lst_c3, [(1 - random_group_broadcast_upload_y_lst_c3[i] / random_group_broadcast_download_y_lst_c3[i]) * 100
                for i in range(len(random_group_x_lst_c3))], label="Broadcast-RandGroup n=3")

ax.set_ylabel('Time Saved (%)', label_font)
ax.set_xlabel("Number of Total Devices", label_font)
ax.legend(prop=legend_font)
fig.tight_layout()
plt.savefig("C:\\Users\\tiana\\Desktop\\figs2\\{}_{}_time_saved.pdf".format(args.dataset, args.R))