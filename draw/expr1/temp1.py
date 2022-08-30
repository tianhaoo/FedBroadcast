import math

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pickle

from utils import seed_all
from utils.simulation import get_partition_lst, get_devices_locations, get_devices_download_latencies, get_devices_computation_latencies, \
    get_rate, opt_group_scheduled_devices, t_cp_k, t_up_k_no_broadcast, t_bc_k, t_bc_k_no_broadcast, get_round_k_time, \
    random_choice_scheduled_devices, random_choice_scheduled_devices_csame, random_group_scheduled_devices, \
    random_group_scheduled_devices_csame

from utils.options import args_parser
from draw.options import *

# 随机抽取、随机分组和最优分组、 使用广播下发和不使用广播下发、 在每轮设备数量相同的情况下，求每轮的平均时间




x_lst = [20, 30, 50, 80, 120, 160, 210, 300]
opt_group_no_broadcast_y_lst = []
opt_group_y_lst = []
random_choice_no_broadcast_y_lst_c5 = []
random_choice_y_lst_c5 = []
random_choice_no_broadcast_y_lst_c10 = []
random_choice_y_lst_c10 = []
random_choice_no_broadcast_y_lst_csame = []
random_choice_y_lst_csame = []
random_group_no_broadcast_y_lst_c5 = []
random_group_y_lst_c5 = []
random_group_no_broadcast_y_lst_c10 = []
random_group_y_lst_c10 = []
random_group_no_broadcast_y_lst_csame = []
random_group_y_lst_csame = []

for num_users in x_lst:
    print("num_users", num_users)
    opt_group_average_lst = []
    opt_group_broadcast_average_lst = []
    random_choice_average_lst_c5 = []
    random_choice_broadcast_average_lst_c5 = []
    random_choice_average_lst_c10 = []
    random_choice_broadcast_average_lst_c10 = []
    random_choice_average_lst_csame = []
    random_choice_broadcast_average_lst_csame = []
    random_group_average_lst_c5 = []
    random_group_broadcast_average_lst_c5 = []
    random_group_average_lst_c10 = []
    random_group_broadcast_average_lst_c10 = []
    random_group_average_lst_csame = []
    random_group_broadcast_average_lst_csame = []
    for seed in tqdm(range(2)):
        pass

        # 1. mnist mlp  model_size=5088320.0, macs=1588000.0
        # 2. cifar mlp  model_size=19731520.0, macs=6164000.0

        args = args_parser()

        # # mnist mlp
        # args.dataset = 'mnist'
        # args.data_num = 60000
        # args.model_size = 5088320.0
        # args.macs = 1588000.0
        # args.num_users = num_users
        # args.C_path_loss = 100

        # cifar mlp
        args.dataset = 'cifar'
        args.data_num = 50000
        args.model_size = 19731520.0
        args.macs = 6164000.0
        args.num_users = 100
        args.C_path_loss = 100
        args.num_users = num_users

        args.R = 1000

        args.epochs = 1500

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

        opt_group_time_lst = []  # 最优分组 不广播下发
        opt_group_broadcast_time_lst = []  # 最优分组 广播下发
        random_choice_time_lst_c5 = []  # 每轮10个，真随机抽 不广播下发
        random_choice_broadcast_time_lst_c5 = []  # 每轮10个，真随机抽 广播下发
        random_choice_time_lst_c10 = []
        random_choice_broadcast_time_lst_c10 = []
        random_choice_time_lst_csame = []  # 每轮>=10个，每轮个数和opt_group一样 不广播下发
        random_choice_broadcast_time_lst_csame = []  # 每轮>=10个，每轮个数和opt_group一样 广播下发
        random_group_time_lst_c5 = []  # 每轮10个，真随机分组 不广播下发
        random_group_broadcast_time_lst_c5 = []  # 每轮10个，真随机分组 广播下发
        random_group_time_lst_c10 = []
        random_group_broadcast_time_lst_c10 = []
        random_group_time_lst_csame = []  # 每轮>=10个，每轮个数和opt_group一样 不广播下发
        random_group_broadcast_time_lst_csame = []  # 每轮>=10个，每轮个数和opt_group一样 广播下发

        partition_lst = get_partition_lst(args, devices_download_latencies)
        opt_order = list(range(len(partition_lst)))  # 由于只考虑广播下发，所以顺序不重要

        opt_group_scheduled_devices_lst = opt_group_scheduled_devices(args, devices_download_latencies, opt_order)
        # show_devices_partition(devices_locations, devices_download_latencies, devices_computation_latencies,
        #                        partition_lst, args)

        random_choice_scheduled_devices_lst_c5 = random_choice_scheduled_devices(args, c=0.1)
        random_choice_scheduled_devices_lst_c10 = random_choice_scheduled_devices(args, c=0.2)

        random_choice_scheduled_devices_lst_csame = random_choice_scheduled_devices_csame(args, partition_lst)
        # show_devices_partition(devices_locations, devices_download_latencies, devices_computation_latencies,
        #                        random_choice_scheduled_devices2[:8], args)
        random_group_scheduled_devices_lst_c5 = random_group_scheduled_devices(args, c=0.1)
        random_group_scheduled_devices_lst_c10 = random_group_scheduled_devices(args, c=0.2)

        random_group_scheduled_devices_lst_csame = random_group_scheduled_devices_csame(args, partition_lst)
        # show_devices_partition(devices_locations, devices_download_latencies, devices_computation_latencies,
        #                        random_group_scheduled_devices2[:8], args)
        round_lst = []
        opt_group_time = 0
        opt_group_broadcast_time = 0
        random_choice_time_c5 = 0
        random_choice_broadcast_time_c5 = 0
        random_choice_time_c10 = 0
        random_choice_broadcast_time_c10 = 0
        random_choice_time_csame = 0
        random_choice_broadcast_time_csame = 0
        random_group_time_c5 = 0
        random_group_broadcast_time_c5 = 0
        random_group_time_c10 = 0
        random_group_broadcast_time_c10 = 0
        random_group_time_csame = 0
        random_group_broadcast_time_csame = 0




        for k in range(1, args.epochs):
            round_lst.append(k)

            # 最优分组
            scheduled_devices = opt_group_scheduled_devices_lst
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])


            # 最优分组，不广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=False, broadcast_upload=False)
            t_round_k = t_bc_k_no_broadcast(pi_k, devices_download_latencies)
            opt_group_time += t_round_k
            opt_group_time_lst.append(t_round_k)  # 每个设备的平均下发时间

            # 最优分组，广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=True, broadcast_upload=False)
            t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
            opt_group_broadcast_time += t_round_k
            opt_group_broadcast_time_lst.append(t_round_k)

            # 随机抽取1
            scheduled_devices = random_choice_scheduled_devices_lst_c5
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])

            # 随机抽取1 不广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=False, broadcast_upload=False)
            t_round_k = t_bc_k_no_broadcast(pi_k, devices_download_latencies)
            random_choice_time_c5 += t_round_k
            random_choice_time_lst_c5.append(t_round_k)

            # 随机抽取1，广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=True, broadcast_upload=False)
            t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
            random_choice_broadcast_time_c5 += t_round_k
            random_choice_broadcast_time_lst_c5.append(t_round_k)


            # 随机抽取2
            scheduled_devices = random_choice_scheduled_devices_lst_csame
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])


            # 随机抽取2 不广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=False, broadcast_upload=False)
            t_round_k = t_bc_k_no_broadcast(pi_k, devices_download_latencies)
            random_choice_time_csame += t_round_k
            random_choice_time_lst_csame.append(t_round_k)

            # 随机抽取2，广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=True, broadcast_upload=False)
            t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
            random_choice_broadcast_time_csame += t_round_k
            random_choice_broadcast_time_lst_csame.append(t_round_k)

            # 随机抽取3
            scheduled_devices = random_choice_scheduled_devices_lst_c10
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])

            # 随机抽取3 不广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=False, broadcast_upload=False)
            t_round_k = t_bc_k_no_broadcast(pi_k, devices_download_latencies)
            random_choice_time_c10 += t_round_k
            random_choice_time_lst_c10.append(t_round_k)

            # 随机抽取3，广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=True, broadcast_upload=False)
            t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
            random_choice_broadcast_time_c10 += t_round_k
            random_choice_broadcast_time_lst_c10.append(t_round_k)

            # 随机分组1
            scheduled_devices = random_group_scheduled_devices_lst_c5
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])

            # 随机分组1 不广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=False, broadcast_upload=False)
            t_round_k = t_bc_k_no_broadcast(pi_k, devices_download_latencies)
            random_group_time_c5 += t_round_k
            random_group_time_lst_c5.append(t_round_k)

            # 随机分组1，广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=True, broadcast_upload=False)
            t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
            random_group_broadcast_time_c5 += t_round_k
            random_group_broadcast_time_lst_c5.append(t_round_k)

            # 随机分组2
            scheduled_devices = random_group_scheduled_devices_lst_csame
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])

            # 随机分组2 不广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=False, broadcast_upload=False)
            t_round_k = t_bc_k_no_broadcast(pi_k, devices_download_latencies)
            random_group_time_csame += t_round_k
            random_group_time_lst_csame.append(t_round_k)

            # 随机分组2，广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=True, broadcast_upload=False)
            t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
            random_group_broadcast_time_csame += t_round_k
            random_group_broadcast_time_lst_csame.append(t_round_k)

            # 随机分组3
            scheduled_devices = random_group_scheduled_devices_lst_c10
            pi_k_minus_1 = set(scheduled_devices[k - 1])
            pi_k = set(scheduled_devices[k])

            # 随机分组3 不广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=False, broadcast_upload=False)
            t_round_k = t_bc_k_no_broadcast(pi_k, devices_download_latencies)
            random_group_time_c10 += t_round_k
            random_group_time_lst_c10.append(t_round_k)

            # 随机分组3，广播下发
            # t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
            #                              devices_upload_BS_latencies, devices_upload_device_latencies,
            #                              broadcast_download=True, broadcast_upload=False)
            t_round_k = t_bc_k(pi_k, set(), devices_download_latencies)
            random_group_broadcast_time_c10 += t_round_k
            random_group_broadcast_time_lst_c10.append(t_round_k)


        # plt.plot(round_lst, opt_group_time_lst, label="opt_group", linestyle="-.")
        # print("最优分组，不广播", sum(opt_group_time_lst)/len(opt_group_time_lst))
        opt_group_average_lst.append(sum(opt_group_time_lst)/len(opt_group_time_lst))

        # plt.plot(round_lst, opt_group_broadcast_time_lst, label="opt_group_broadcast")
        # print("最优分组，广播", sum(opt_group_broadcast_time_lst)/len(opt_group_broadcast_time_lst))
        opt_group_broadcast_average_lst.append(sum(opt_group_broadcast_time_lst)/len(opt_group_broadcast_time_lst))

        # plt.plot(round_lst, random_choice_time_lst1, label="random_choice1", linestyle="-.")
        # print("随机抽取1，不广播", sum(random_choice_time_lst1)/len(random_choice_time_lst1))
        # plt.plot(round_lst, random_choice_broadcast_time_lst1, label="random_choice_broadcast1")
        # print("随机抽取1，广播", sum(random_choice_broadcast_time_lst1)/len(random_choice_broadcast_time_lst1))

        random_choice_average_lst_c5.append(sum(random_choice_time_lst_c5) / len(random_choice_time_lst_c5))
        random_choice_broadcast_average_lst_c5.append(sum(random_choice_broadcast_time_lst_c5) / len(random_choice_broadcast_time_lst_c5))

        random_choice_average_lst_c10.append(sum(random_choice_time_lst_c10) / len(random_choice_time_lst_c10))
        random_choice_broadcast_average_lst_c10.append(sum(random_choice_broadcast_time_lst_c10) / len(random_choice_broadcast_time_lst_c10))

        # plt.plot(round_lst, random_choice_time_lst2, label="random_choice2", linestyle="-.")
        # print("随机抽取2，不广播", sum(random_choice_time_lst2)/len(random_choice_time_lst2))
        random_choice_average_lst_csame.append(sum(random_choice_time_lst_csame) / len(random_choice_time_lst_csame))

        # plt.plot(round_lst, random_choice_broadcast_time_lst2, label="random_choice_broadcast2")
        # print("随机抽取2，广播", sum(random_choice_broadcast_time_lst2)/len(random_choice_broadcast_time_lst2))
        random_choice_broadcast_average_lst_csame.append(sum(random_choice_broadcast_time_lst_csame) / len(random_choice_broadcast_time_lst_csame))

        # plt.plot(round_lst, random_group_time_lst1, label="random_group1", linestyle="-.")
        # print("随机分组1，不广播", sum(random_group_time_lst1)/len(random_group_time_lst1))
        # plt.plot(round_lst, random_group_broadcast_time_lst1, label="random_group_broadcast1")
        # print("随机分组1，广播", sum(random_group_broadcast_time_lst1)/len(random_group_broadcast_time_lst1))

        random_group_average_lst_c5.append(sum(random_group_time_lst_c5) / len(random_group_time_lst_c5))
        random_group_broadcast_average_lst_c5.append(sum(random_group_broadcast_time_lst_c5) / len(random_group_broadcast_time_lst_c5))

        random_group_average_lst_c10.append(sum(random_group_time_lst_c10) / len(random_group_time_lst_c10))
        random_group_broadcast_average_lst_c10.append(sum(random_group_broadcast_time_lst_c10) / len(random_group_broadcast_time_lst_c10))

        # plt.plot(round_lst, random_group_time_lst2, label="random_group2", linestyle="-.")
        # print("随机分组2，不广播", sum(random_group_time_lst2)/len(random_group_time_lst2))
        random_group_average_lst_csame.append(sum(random_group_time_lst_csame) / len(random_group_time_lst_csame))

        # plt.plot(round_lst, random_group_broadcast_time_lst2, label="random_group_broadcast2")
        # print("随机分组2，广播", sum(random_group_broadcast_time_lst2)/len(random_group_broadcast_time_lst2))
        random_group_broadcast_average_lst_csame.append(sum(random_group_broadcast_time_lst_csame) / len(random_group_broadcast_time_lst_csame))

        # plt.legend()
        # plt.show()


    # 毫秒
    opt_group_no_broadcast_y_lst.append(sum(opt_group_average_lst) / len(opt_group_average_lst) * 1000)
    opt_group_y_lst.append(sum(opt_group_broadcast_average_lst) / len(opt_group_broadcast_average_lst) * 1000)
    random_choice_no_broadcast_y_lst_c5.append(sum(random_choice_average_lst_c5) / len(random_choice_average_lst_c5) * 1000)
    random_choice_y_lst_c5.append(sum(random_choice_broadcast_average_lst_c5) / len(random_choice_broadcast_average_lst_c5) * 1000)
    random_choice_no_broadcast_y_lst_c10.append(sum(random_choice_average_lst_c10) / len(random_choice_average_lst_c10) * 1000)
    random_choice_y_lst_c10.append(sum(random_choice_broadcast_average_lst_c10) / len(random_choice_broadcast_average_lst_c10) * 1000)
    random_choice_no_broadcast_y_lst_csame.append(sum(random_choice_average_lst_csame) / len(random_choice_average_lst_csame) * 1000)
    random_choice_y_lst_csame.append(sum(random_choice_broadcast_average_lst_csame) / len(random_choice_broadcast_average_lst_csame) * 1000)
    random_group_no_broadcast_y_lst_c5.append(sum(random_group_average_lst_c5) / len(random_group_average_lst_c5) * 1000)
    random_group_y_lst_c5.append(sum(random_group_broadcast_average_lst_c5) / len(random_group_broadcast_average_lst_c5) * 1000)
    random_group_no_broadcast_y_lst_c10.append(sum(random_group_average_lst_c10) / len(random_group_average_lst_c10) * 1000)
    random_group_y_lst_c10.append(sum(random_group_broadcast_average_lst_c10) / len(random_group_broadcast_average_lst_c10) * 1000)
    random_group_no_broadcast_y_lst_csame.append(sum(random_group_average_lst_csame) / len(random_group_average_lst_csame) * 1000)
    random_group_y_lst_csame.append(sum(random_group_broadcast_average_lst_csame) / len(random_group_broadcast_average_lst_csame) * 1000)



# plt.plot(x_lst, opt_group_no_broadcast_y_lst, label="opt_group_no_broadcast", marker="o")
# plt.plot(x_lst, random_choice_no_broadcast_y_lst1, label="random_choice_no_broadcast", marker="s")
# plt.plot(x_lst, random_choice_no_broadcast_y_lst2, label="random_choice_no_broadcast", marker="s")
# plt.plot(x_lst, random_group_no_broadcast_y_lst1, label="random_group_no_broadcast", marker="D")
# plt.plot(x_lst, random_group_no_broadcast_y_lst2, label="random_group_no_broadcast", marker="D")
# plt.plot(x_lst, opt_group_y_lst, label="opt_group")
# plt.plot(x_lst, random_choice_y_lst1, label="random_choice", linestyle="-.")
# plt.plot(x_lst, random_choice_y_lst2, label="random_choice", linestyle="-.")
# plt.plot(x_lst, random_group_y_lst1, label="random_group", linestyle=":")
# plt.plot(x_lst, random_group_y_lst2, label="random_group", linestyle=":")
# plt.legend()
# plt.show()
#


labels = x_lst

x = np.arange(len(labels))  # the label locations
total_width = 1.5
n = len(labels)
width = total_width / n
fig, ax = plt.subplots(dpi=800)
rects1 = ax.bar(x - width*1, opt_group_no_broadcast_y_lst, width, label='Unicast', color=draw_args.unicast_color)
rects2 = ax.bar(x + width*0, random_choice_y_lst_csame, width, label='Broadcast-RandGroup', tick_label=x_lst, color=draw_args.randgroup_color)
rects3 = ax.bar(x + width*1, random_choice_y_lst_c5, width, label='Broadcast-RandSel', color=draw_args.randsel_color)
rects4 = ax.bar(x + width*2, opt_group_y_lst, width, label='Broadcast-OptGroup', color=draw_args.optgroup_color)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Downloading Latency (ms)', label_font2)
ax.set_xlabel("Number of Total Devices", label_font)
ax.legend(prop=legend_font)
fig.tight_layout()
plt.savefig("C:\\Users\\tiana\\Desktop\\figs\\{}_{}_1.pdf".format(args.dataset, args.R))





fig, ax = plt.subplots(dpi=800)
ax.plot(x_lst, opt_group_y_lst, label="Broadcast-OptGroup", color=draw_args.optgroup_color)
ax.plot(x_lst, random_choice_y_lst_c5, label="Broadcast-RandSel", color=draw_args.randsel_color)
ax.plot(x_lst, random_choice_y_lst_csame, label="Broadcast-RandGroup", color=draw_args.randgroup_color)
ax.set_ylabel('Downloading Latency (ms)', label_font2)
ax.set_xlabel("Number of Total Devices", label_font)
ax.legend(prop=legend_font)
fig.tight_layout()
plt.savefig("C:\\Users\\tiana\\Desktop\\figs\\{}_{}_2.pdf".format(args.dataset, args.R))




