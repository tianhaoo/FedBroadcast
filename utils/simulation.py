# 给训练计时用到的相关函数
import os

from utils import seed_all
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import pickle
import functools
from concurrent import futures

# 生成设备的位置
from utils.options import args_parser
from utils.show import show_devices_info, show_devices_partition


def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            executor = futures.ThreadPoolExecutor(1)
            future = executor.submit(func, *args, **kw)
            return future.result(timeout=seconds)

        return wrapper

    return decorator


def get_devices_locations(args):
    r, num_users, seed = args.R, args.num_users, args.seed
    devices_locations = []
    for i in range(num_users):
        seed *= 2
        random.seed(seed)
        x = random.uniform(-r, r)
        random.seed(seed + 1)
        y = random.uniform(-r, r)
        t = math.sqrt((x ** 2) + (y ** 2))
        while t > r or t < 1:
            seed += 1
            random.seed(seed)
            x = random.uniform(-r, r)
            random.seed(seed + 2)
            y = random.uniform(-r, r)
            t = math.sqrt((x ** 2) + (y ** 2))
        devices_locations.append((x, y))
    return devices_locations


# 传输速率取决于发送者的功率和期望到达的距离
def get_rate(power, distance, args):
    P_mw = math.pow(10, power / 10)  # mW
    N0_mw = math.pow(10, args.N0 / 10)  # mW/MHz
    path_loss = 10 * args.alpha * math.log(distance, 10) + args.C_path_loss  # dB
    channel_variance = math.pow(10, -0.1 * path_loss)
    sigma = math.sqrt((2 / (4 - math.pi)) * math.sqrt(channel_variance))
    h = sigma / (distance * distance)
    c = args.B * 1000 * math.log(1 + (P_mw * h) / (args.B * N0_mw), 2)  # bit/ms
    return c  # bit/ms


def get_devices_download_latencies(devices_locations, args):
    return [args.model_size / get_rate(args.P_base_station,
                                       math.sqrt((devices_locations[i][0] ** 2) + (devices_locations[i][1] ** 2)),
                                       args) / 1000
            for i in range(args.num_users)]  # s 基站给设备下发模型的延时


def get_devices_computation_latencies(args):
    # ms，设备计算一轮花费的最短时间
    # 本地epoch数 * 一个epoch里的batch数 * 模型更新一次的计算量 / cpu频率
    min_time = args.local_ep * (args.data_num / args.num_users / args.local_bs) * args.macs / args.cpu_frequency / 1000
    np.random.seed(args.seed)
    return list(np.random.exponential(min_time, size=args.num_users) + min_time)  # s 设备的本地计算延时


# 返回最优的划分
def get_partition_lst(args, devices_download_latencies):
    all_devices = list(range(args.num_users))
    # 按照下发时间给设备降序排序
    all_devices.sort(key=lambda x: devices_download_latencies[x], reverse=True)

    # 初始化不分组的差值数组
    no_partition = [[0 for i in range(args.num_users + 1)] for j in range(args.num_users + 1)]
    for i in range(1, args.num_users + 1):
        for j in range(1, args.num_users + 1):
            no_partition[i][j] = devices_download_latencies[i - 1] - devices_download_latencies[j - 1]

    # 初始化dp数组
    dp = [[0 for i in range(args.num_users + 1)] for j in range(args.num_users + 1)]
    # 初始化path数组
    path = [[(None, None) for i in range(args.num_users + 1)] for j in range(args.num_users + 1)]

    # 更新dp数组和path数组
    for k in range(args.num_users, 0, -1):
        t = 0
        while k - t >= 1:
            i, j = k - t, args.num_users - t
            if args.num_users - k < args.num_users * args.frac - 1:
                dp[i][j] = float("inf")
            else:
                temp_left, temp_right = None, None
                min_value = no_partition[i][j]
                for m in range(j - i - 1):
                    temp = dp[i][i + m] + dp[i + m + 1][j]
                    if temp < min_value:
                        min_value = temp
                        temp_left, temp_right = (i, i + m), (i + m + 1, j)
                dp[i][j] = min_value
                path[i][j] = (temp_left, temp_right)
            t += 1

    partition_points = []

    # 寻找所有的分割点
    def find_all_partition_point(T, partition_points):
        if T[0] is not None and T[1] is not None:
            partition_points.append(T[0][1])  # 根
            find_all_partition_point(path[T[0][0]][T[0][1]], partition_points)  # 左
            find_all_partition_point(path[T[1][0]][T[1][1]], partition_points)  # 右

    find_all_partition_point(path[1][args.num_users], partition_points)
    partition_points.sort()
    # print(partition_points)

    # 根据分割点生成划分
    devices_partition_lst = []
    pre = 0
    for i in partition_points:
        devices_partition_lst.append(all_devices[pre:i])
        pre = i
    devices_partition_lst.append(all_devices[pre:])
    # print("devices_partition_lst ", devices_partition_lst)  # 返回的是动态规划找到的一种最优划分

    return devices_partition_lst


# 返回长度为n的序列的全排列
def get_all_possible_order(n):
    # 参数是分组数
    def permutations(res, arr, position, end):
        if position == end:
            # print(arr)
            res.append(arr.copy())

        else:
            for index in range(position, end):
                arr[index], arr[position] = arr[position], arr[index]
                permutations(res, arr, position + 1, end)
                arr[index], arr[position] = arr[position], arr[index]

    all_order = []
    permutations(all_order, list(range(n)), 0, n)
    return all_order


# 第k轮的广播下发时间
def t_bc_k(pi_k, pi_k_save, devices_download_latencies):
    # pi_k_save \in pi_k
    assert isinstance(pi_k, set)
    assert isinstance(pi_k_save, set)
    assert pi_k_save.issubset(pi_k)
    s = pi_k - pi_k_save
    time_lst = []
    for device in s:
        time_lst.append(devices_download_latencies[device])
    if time_lst:
        return max(time_lst)
    else:
        return 0


# 第k轮的下发时间, 不广播
def t_bc_k_no_broadcast(pi_k, devices_download_latencies):
    # pi_k_save \in pi_k
    assert isinstance(pi_k, set)
    time_lst = []
    for device in pi_k:
        time_lst.append(devices_download_latencies[device])
    return sum(time_lst)


# 第k轮的计算时间
def t_cp_k(pi_k, devices_computation_latencies):
    assert isinstance(pi_k, set)
    temp_lst = []
    for device in pi_k:
        temp_lst.append(devices_computation_latencies[device])
    return max(temp_lst)


# 第k轮的广播上传时间
def t_up_k(pi_k, pi_k_target, devices_upload_BS_latencies, devices_upload_device_latencies):
    assert isinstance(pi_k, set)
    assert isinstance(pi_k_target, set)
    # target_set 里面有可能有 BS 也有可能没有BS
    time_lst = []
    for device in pi_k:
        f = device
        upload_time_lst = []  # f 上传给这个target所用时间
        for t in pi_k_target:
            if t == 'BS':
                upload_time_lst.append(devices_upload_BS_latencies[f])
            else:
                upload_time_lst.append(devices_upload_device_latencies[f][t])
        time_lst.append(max(upload_time_lst))  # 设备以最慢的速率广播上传

    if time_lst:
        return sum(time_lst)
    else:
        return 0


# 第k轮的上传时间，不广播
def t_up_k_no_broadcast(pi_k, devices_upload_BS_latencies):
    assert isinstance(pi_k, set)
    time_lst = []
    for device in pi_k:
        time_lst.append(devices_upload_BS_latencies[device])

    if time_lst:
        return sum(time_lst)
    else:
        return 0


def random_choice_scheduled_devices(args, m_times_c=None, c=None):
    # 每轮随机抽取的设备数量固定为m
    all_devices = list(range(args.num_users))  # all devices' index
    if m_times_c is not None:
        m = min(args.num_users, m_times_c)  # 防止每轮要取的设备大于总的设备数量
    elif c is not None:
        m = max(int(c * args.num_users), 1)  # 向下取整
    else:
        m = max(int(args.frac * args.num_users), 1)  # 向下取整
    # print("random_choice K x C = ", m)
    scheduled_devices = []
    seed_all(args.seed)
    for i in range(args.epochs):
        scheduled_devices.append(np.random.choice(all_devices, size=m, replace=False).tolist())

    return scheduled_devices


def random_choice_scheduled_devices_csame(args, opt_partition_lst):
    # 每轮抽取的设备数量和opt_group的相同
    all_devices = list(range(args.num_users))  # all devices' index

    # print("random_choice K x C = ", [len(i) for i in opt_partition_lst])
    # 生成schedule devices
    scheduled_devices = []
    # 把每个group按照顺序opt_order, append进去
    opt_order = list(range(len(opt_partition_lst)))
    p = 0  # 记录当前指针的位置
    seed_all(args.seed)
    for i in range(args.epochs):
        p_next = (p + 1) % len(opt_order)
        m = len(opt_partition_lst[opt_order[p]])
        scheduled_devices.append(np.random.choice(all_devices, size=m, replace=False).tolist())
        p = p_next

    return scheduled_devices


def random_group_scheduled_devices(args, m_times_c=None, c=None):
    # 每轮设备数量固定
    all_devices = list(range(args.num_users))  # all devices' index
    if m_times_c is not None:
        m = min(args.num_users, m_times_c)  # 防止每轮要取的设备大于总的设备数量
    elif c is not None:
        m = max(int(c * args.num_users), 1)  # 向下取整
    else:
        m = max(int(args.frac * args.num_users), 1)  # 向下取整
    # print("random_group K x C = ", m)

    seed_all(args.seed)
    np.random.shuffle(all_devices)
    devices_group_lst = []
    p = 0
    while (p + 1) * m <= len(all_devices):
        devices_group_lst.append(all_devices[p * m:(p + 1) * m])
        p += 1
    if p * m < len(all_devices):
        devices_group_lst.append(all_devices[p * m:])

    # print("scheduled_devices devices_partition_lst ", devices_group_lst)

    scheduled_devices = []
    # 把每个group 直接 append进去
    cnt = 0
    while cnt < args.epochs:
        for group in devices_group_lst:
            scheduled_devices.append(group)
            cnt += 1
            if cnt >= args.epochs:
                break
    return scheduled_devices


def random_group_scheduled_devices_csame(args, opt_partition_lst):
    # 每轮设备数量不固定，和opt_group一样
    all_devices = list(range(args.num_users))  # all devices' index
    seed_all(args.seed)
    np.random.shuffle(all_devices)
    # 先按照opt_partition_lst做一个random_partition_lst
    random_partition_lst = []
    p = 0
    for group in opt_partition_lst:
        random_partition_lst.append(all_devices[p:p + len(group)])
        p += len(group)

    # print("random_group devices_partition_lst", random_partition_lst)
    # print("random_group K x C = ", [len(i) for i in random_partition_lst])
    # 生成schedule devices
    scheduled_devices = []
    # 把每个group按照顺序opt_order, append进去
    opt_order = list(range(len(random_partition_lst)))
    p = 0  # 记录当前指针的位置
    for i in range(args.epochs):
        p_next = (p + 1) % len(opt_order)
        scheduled_devices.append(random_partition_lst[opt_order[p]])
        p = p_next

    return scheduled_devices


def opt_group_scheduled_devices(args, devices_download_latencies, opt_order):
    # 如果只用广播下发，那么opt_order不影响结果，直接随机一个就行
    # 如果使用广播上传，那么应该找到最优的order

    # 获取设备分组信息
    devices_partition_lst = get_partition_lst(args, devices_download_latencies)
    # print("opt_group devices_partition_lst", devices_partition_lst)
    # print("opt_group K x C = ", [len(i) for i in devices_partition_lst])
    # 生成schedule devices
    scheduled_devices = []
    # 把每个group按照顺序opt_order, append进去
    p = 0  # 记录当前指针的位置
    for i in range(args.epochs):
        p_next = (p + 1) % len(opt_order)
        scheduled_devices.append(devices_partition_lst[opt_order[p]])
        p = p_next

    return scheduled_devices


def powersets(lst):
    x = len(lst)
    res = []
    for i in range(1 << x):
        res.append([lst[j] for j in range(x) if (i & (1 << j))])
    return res  # 子集+BS


def opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                  devices_upload_device_latencies):
    # 获取第k轮被节省的设备
    # k=1时，pi_k_save=空集
    assert isinstance(pi_k_minus_1, set)
    assert isinstance(pi_k, set)

    powerset_lst = powersets(list(pi_k))
    min_time = float('inf')
    pi_k_save = set()
    for subset in powerset_lst:
        temp = set(subset)
        if temp != pi_k:
            pi_k_minus_1_target = temp.union({'BS'})
        else:
            pi_k_minus_1_target = temp

        # pi_k-1 上传给pi_k的时间
        t1 = t_up_k(pi_k_minus_1, pi_k_minus_1_target, devices_upload_BS_latencies, devices_upload_device_latencies)
        # BS下发给pi_k的时间
        t2 = t_bc_k(pi_k, set(subset), devices_download_latencies)
        if min_time > t1 + t2:
            min_time = t1 + t2
            pi_k_save = temp

    normal_time = t_up_k(pi_k_minus_1, {'BS'}, devices_upload_BS_latencies, devices_upload_device_latencies) + \
                  t_bc_k(pi_k, set(), devices_download_latencies)
    if normal_time > min_time:
        # print("成功减少了时间", normal_time, min_time, pi_k, pi_k_save)
        return pi_k_save
    else:
        # print("未能减少时间", normal_time, min_time, pi_k, set())
        return set()


# 获取最优的顺序
def get_opt_order(devices_partition_lst, devices_download_latencies, devices_computation_latencies,
                  devices_upload_BS_latencies, devices_upload_device_latencies):
    all_order = get_all_possible_order(len(devices_partition_lst))
    res_dic = {}
    memo = {}
    for order in all_order:
        sum_t_round_k = 0
        for i in range(len(order)):
            f = order[i]
            if i + 1 <= len(order) - 1:
                t = order[i + 1]
            else:
                t = order[0]
            # print("@", f, "->", t)
            memo_key = str(f) + "->" + str(t)

            if memo_key not in memo.keys():
                # 计算pi_k=f给pi_k+1=t所花费的时间
                # 具体就是 pi_k 计算、pi_k上传、pi_k+1下发
                t_round_k = 0
                t_round_k += t_cp_k(set(devices_partition_lst[f]), devices_computation_latencies)
                # 计算pi_save
                pi_k_save = opt_pi_k_save(set(devices_partition_lst[f]), set(devices_partition_lst[t]), devices_download_latencies, devices_upload_BS_latencies,
                                          devices_upload_device_latencies)
                if pi_k_save != set(devices_partition_lst[t]):
                    pi_k_target = pi_k_save.union({'BS'})
                else:
                    pi_k_target = pi_k_save
                t_round_k += t_up_k(set(devices_partition_lst[f]), pi_k_target, devices_upload_BS_latencies, devices_upload_device_latencies)
                t_round_k += t_bc_k(set(devices_partition_lst[t]), pi_k_save, devices_download_latencies)

                memo[memo_key] = t_round_k
            else:
                t_round_k = memo[memo_key]

            sum_t_round_k += t_round_k

        res_dic[tuple(order)] = sum_t_round_k
    lst = sorted(res_dic.keys(), key=lambda x: res_dic[x])
    temp = sorted(res_dic.values())
    # print("different order time lst:", temp)
    opt_order = lst[0]
    # print("opt_order:", opt_order, res_dic[opt_order])
    return opt_order


def get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
                     devices_upload_BS_latencies, devices_upload_device_latencies,
                     broadcast_download=False, broadcast_upload=False, add_computation_latency=True):
    if not broadcast_upload:
        # 不广播上传
        if not broadcast_download:
            # 不广播下发
            t_round_k = 0
            if add_computation_latency:
                t_round_k += t_cp_k(pi_k_minus_1, devices_computation_latencies)  # k-1轮的计算时间
            t_round_k += t_up_k_no_broadcast(pi_k_minus_1, devices_upload_BS_latencies)  # k-1轮的上传时间
            t_round_k += t_bc_k_no_broadcast(pi_k, devices_download_latencies)  # 第k轮的下发时间
            return t_round_k
        else:
            # 广播下发
            t_round_k = 0
            if add_computation_latency:
                t_round_k += t_cp_k(pi_k_minus_1, devices_computation_latencies)  # k-1轮的计算时间
            t_round_k += t_up_k_no_broadcast(pi_k_minus_1, devices_upload_BS_latencies)  # k-1轮的上传时间
            pi_k_save = set()  # 因为没有广播上传，所以下发时没有节省的设备
            t_round_k += t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
            return t_round_k
    else:
        # 一定是广播下发的了，要不然没意义
        assert broadcast_download is True
        # 广播上传
        t_round_k = 0
        if add_computation_latency:
            t_round_k += t_cp_k(pi_k_minus_1, devices_computation_latencies)  # k-1轮的计算时间
        pi_k_save = opt_pi_k_save(pi_k_minus_1, pi_k, devices_download_latencies, devices_upload_BS_latencies,
                                  devices_upload_device_latencies)
        # if pi_k_save != pi_k:
        #     pi_k_minus_1_target = pi_k_save.union({'BS'})
        # else:
        #     pi_k_minus_1_target = pi_k_save

        # 修改成总要上传给BS
        pi_k_minus_1_target = pi_k_save.union({'BS'})
        t_round_k += t_up_k(pi_k_minus_1, pi_k_minus_1_target, devices_upload_BS_latencies,
                            devices_upload_device_latencies)  # k-1轮的上传时间
        t_round_k += t_bc_k(pi_k, pi_k_save, devices_download_latencies)  # 第k轮的下发时间
        return t_round_k

#
# def get_round_time(args):
#     # time_type = FedAvg / RoundRobin / FedBroadcast
#     seed_all(args.seed)
#
#     # 坐标(x, y) 设备位置
#     devices_locations = get_devices_locations(args)
#     print("devices_locations", devices_locations)
#     # ms 设备下载时间
#     devices_download_latencies = get_devices_download_latencies(devices_locations, args)
#     print("devices_download_latencies", devices_download_latencies)
#     # 设备计算时间
#     devices_computation_latencies = get_devices_computation_latencies(args)
#     print("devices_computation_latencies", devices_computation_latencies)
#
#     # ms 设备上传给BS的时间
#     devices_upload_BS_latencies = [args.model_size / get_rate(args.P_device,
#                                                               math.sqrt((devices_locations[i][0] ** 2) +
#                                                                         (devices_locations[i][1] ** 2)), args)
#                                    for i in range(args.num_users)]  # ms 基站给设备下发模型的延时
#
#     # ms 设备上传给其他设备的时间，一个n*n的矩阵
#     devices_upload_device_latencies = [[0] * args.num_users for i in range(args.num_users)]
#     for from_ in range(args.num_users):
#         for to_ in range(args.num_users):
#             if from_ == to_:
#                 devices_upload_device_latencies[from_][to_] = 0
#             else:
#                 devices_upload_device_latencies[from_][to_] = \
#                     args.model_size / get_rate(args.P_device,
#                                                math.sqrt(
#                                                    ((devices_locations[from_][0] - devices_locations[to_][0]) ** 2) +
#                                                    ((devices_locations[from_][1] - devices_locations[to_][1]) ** 2)),
#                                                args)
#
#     # 一次生成三种训练方式的round_time 列表  FedBroadcast / FedAvg  / RoundRobin
#     #############################################
#     # FedAvg #####################################
#     ##############################################
#     all_devices = list(range(args.num_users))  # all devices' index
#     m = max(int(args.frac * args.num_users), 1)  # 向下取整
#     print("FedAvg K x C = ", m)
#     FedAvg_scheduled_devices = []
#     seed_all(args.seed)
#     for i in range(args.epochs):
#         FedAvg_scheduled_devices.append(np.random.choice(all_devices, size=m, replace=False).tolist())
#
#     FedAvg_round_time = []
#     t = 0
#     for k in range(1, args.epochs):
#         # 最优分组
#         pi_k_minus_1 = set(FedAvg_scheduled_devices[k - 1])
#         pi_k = set(FedAvg_scheduled_devices[k])
#         t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
#                                      devices_upload_BS_latencies, devices_upload_device_latencies,
#                                      broadcast_download=False, broadcast_upload=False, add_computation_latency=True)
#         t += t_round_k
#         FedAvg_round_time.append(t)
#     # 补上少了的一轮
#     t += t_round_k
#     FedAvg_round_time.append(t)
#
#
#     # FedAvg_round_time = []
#     # t = 0  # 第i轮的累计时间
#     # for round_devices in FedAvg_scheduled_devices:
#     #     # 基站下发 （一个一个下发）
#     #     for device in round_devices:  # device是设备的索引号
#     #         t += devices_download_latencies[device]
#     #     # 设备计算阶段  （计算可以是并行的，取最大值）
#     #     t += max([devices_computation_latencies[device] for device in round_devices])
#     #     # 设备上传阶段 (一个一个上传）
#     #     for device in round_devices:  # device是设备的索引号
#     #         t += devices_upload_BS_latencies[device]
#     #     FedAvg_round_time.append(t)
#
#
#     ##############################################
#     # RoundRobin ################################
#     ##############################################
#     all_devices = list(range(args.num_users))  # all devices' index
#     m = max(int(args.frac * args.num_users), 1)
#     print("RoundRobin K x C = ", m)
#     RoundRobin_scheduled_devices = []
#     seed_all(args.seed)
#     np.random.shuffle(all_devices)
#     devices_group_lst = []
#     p = 0
#     while (p + 1) * m <= len(all_devices):
#         devices_group_lst.append(all_devices[p * m:(p + 1) * m])
#         p += 1
#     if p * m < len(all_devices):
#         devices_group_lst.append(all_devices[p * m:])
#
#     print("RoundRobin_devices_partition_lst ", devices_group_lst)
#
#     # 把每个group 直接 append进去
#     cnt = 0
#     while cnt < args.epochs:
#         for group in devices_group_lst:
#             RoundRobin_scheduled_devices.append(group)
#             cnt += 1
#             if cnt >= args.epochs:
#                 break
#
#     RoundRobin_round_time = []
#     t = 0
#     for k in range(1, args.epochs):
#         # 最优分组
#         pi_k_minus_1 = set(RoundRobin_scheduled_devices[k - 1])
#         pi_k = set(RoundRobin_scheduled_devices[k])
#         t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
#                                      devices_upload_BS_latencies, devices_upload_device_latencies,
#                                      broadcast_download=False, broadcast_upload=False, add_computation_latency=True)
#         t += t_round_k
#         RoundRobin_round_time.append(t)
#     # 补上少了的一轮
#     t += t_round_k
#     RoundRobin_round_time.append(t)
#
#     # RoundRobin_round_time = []
#     # t = 0  # 第i轮的累计时间
#     # for round_devices in RoundRobin_scheduled_devices:
#     #     # 基站下发阶段 （一个一个下发）
#     #     for device in round_devices:  # device是设备的索引号
#     #         t += devices_download_latencies[device]
#     #     # 设备计算阶段  （计算可以是并行的，取最大值）
#     #     t += max([devices_computation_latencies[device] for device in round_devices])
#     #     # 设备上传阶段 (一个一个上传）
#     #     for device in round_devices:  # device是设备的索引号
#     #         t += devices_upload_BS_latencies[device]
#     #     RoundRobin_round_time.append(t)
#
#     ##############################################
#     # FedBroadcast ###############################
#     ##############################################
#     FedBroadcast_scheduled_devices = []
#     # 获取设备分组信息
#     devices_partition_lst = get_partition_lst(args, devices_download_latencies)
#     print("fb devices_partition_lst", devices_partition_lst)
#
#     opt_order = list(range(len(devices_partition_lst)))
#     # 生成schedule devices
#     # 把每个group按照顺序opt_order, append进去
#     p = 0  # 记录当前指针的位置
#     for i in range(args.epochs):
#         p_next = (p + 1) % len(opt_order)
#         FedBroadcast_scheduled_devices.append(devices_partition_lst[opt_order[p]])
#         p = p_next
#
#     # 统计每轮所用时间round_time
#     FedBroadcast_round_time = []
#     t = 0
#     for k in range(1, args.epochs):
#         # 最优分组
#         pi_k_minus_1 = set(FedBroadcast_scheduled_devices[k - 1])
#         pi_k = set(FedBroadcast_scheduled_devices[k])
#         t_round_k = get_round_k_time(pi_k_minus_1, pi_k, devices_download_latencies, devices_computation_latencies,
#                                      devices_upload_BS_latencies, devices_upload_device_latencies,
#                                      broadcast_download=True, broadcast_upload=False, add_computation_latency=True)
#         t += t_round_k
#         FedBroadcast_round_time.append(t)
#     # 补上少了的一轮
#     t += t_round_k
#     FedBroadcast_round_time.append(t)
#
#     return FedAvg_round_time, RoundRobin_round_time, FedBroadcast_round_time

if __name__ == "__main__":
    pass