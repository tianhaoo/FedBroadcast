import numpy as np
lst =[1, 2, 3]
print(np.random.choice(lst, size=4, replace=False))

#
# fedavg_sum_time_lst = []  # 平均每个local epoch 要用的时间
# rr_sum_time_lst = []
# fb_sum_time_lst = []
# x_lst = []  # 横坐标用轮会比较吃亏，应该用local epochs
# while True:
#     frac += 0.01
#     current_m = int(args.num_users * frac)
#     if current_m <= 2 or current_m == last_m:
#         continue
#     if current_m >= int(args.num_users * 0.5) - 2 or current_m >= 29:
#         break
#     args.frac = frac
#     last_m = current_m
#     FedAvg_round_time, RoundRobin_round_time, FedBroadcast_round_time, \
#         FedAvg_scheduled_devices, RoundRobin_scheduled_devices, FedBroadcast_scheduled_devices = get_round_time(args)
#     fedavg_sum_time_lst.append(sum(FedAvg_round_time)/sum([len(round_devices)*args.local_ep for round_devices in FedAvg_scheduled_devices]))
#     rr_sum_time_lst.append(sum(RoundRobin_round_time)/sum([len(round_devices)*args.local_ep for round_devices in RoundRobin_scheduled_devices]))
#     fb_sum_time_lst.append(sum(FedBroadcast_round_time)/sum([len(round_devices)*args.local_ep for round_devices in FedBroadcast_scheduled_devices]))
#     x_lst.append(current_m)
#
# plt.plot(x_lst, fedavg_sum_time_lst, label="FedAvg")
# plt.plot(x_lst, rr_sum_time_lst, label="RoundRobin")
# plt.plot(x_lst, fb_sum_time_lst, label="FedBroadcast")
# plt.legend()
# plt.show()




# # 试试看让下一轮的那些设备接收到会比较节省时间，采用最省时间的方案
# @timeout(5)
# def broadcast_upload(a, b, broadcast_upload_memo, devices_locations, devices_download_latencies,
#                      devices_computation_latencies, devices_upload_BS_latencies, args):  # 本轮设备集合a，下轮设备集合b, 备忘录字典指针
#     a, b = list(a), list(b)  # a组广播到b组花费的时间，pi_k_save, 节省的时间
#     memo_key = tuple(a + b)
#     if memo_key not in broadcast_upload_memo:
#         def powerset_plus_BS(lst):
#             x = len(lst)
#             res = []
#             for i in range(1 << x):
#                 res.append([lst[j] for j in range(x) if (i & (1 << j))])
#             for subset in res:
#                 if len(subset) < len(lst) or len(subset) == 0:  # 如果下一轮的所有设备都有就不用广播给BS了
#                     subset.append('BS')
#             return res  # 子集+BS
#
#         def get_broadcast_time(x_lst, y_lst):  # x中设备都以确保y中设备都能收到的速率广播所花费的时间
#             s = 0
#             for x in x_lst:
#                 source_location = devices_locations[x]
#                 max_distance = -float('inf')
#                 for y in y_lst:  # 找到最远的目的地
#                     if y != 'BS':
#                         destination_location = devices_locations[y]
#                     else:
#                         destination_location = (0, 0)
#                     distance = math.sqrt(((source_location[0] - destination_location[0]) ** 2) +
#                                          ((source_location[1] -  [1]) ** 2))
#                     if max_distance < distance:
#                         max_distance = distance
#                 # x要以找到的最远目的地进行广播
#                 s += args.model_size / get_rate(args.P_device, max_distance, args)
#             return s  # x_lst中所有设备都广播给y_lst中设备所花费的时间
#
#         # 基本上传时间，即一个一个上传给BS, 再加上下一轮广播下发和计算的时间，目的是寻找比这个用时少的方案
#         time_lst = [devices_download_latencies[device] +
#                     devices_computation_latencies[device]
#                     for device in b]
#         if time_lst:
#             max_t = max(time_lst)
#         else:
#             max_t = 0
#         base_time = max_t
#         for device in a:
#             base_time += devices_upload_BS_latencies[device]
#         # b的幂集
#         powersets = powerset_plus_BS(b)
#         best_saved_devices = 'not found'
#         min_time = base_time
#         for proposed_i in range(len(powersets)):
#             saved_devices = powersets[proposed_i]
#             proposed_time = get_broadcast_time(a, saved_devices)  # 广播上传时间
#
#             temp = [] # 存放下一轮所有设备的计算时间
#             for device in b:
#                 temp.append(devices_computation_latencies[device])
#             proposed_time += max(temp)
#
#             temp = []  # 存放下一轮所有设备的下发时间
#             for device in b:
#                 if device not in saved_devices:
#                     temp.append(devices_download_latencies[device])
#                 else:
#                     temp.append(0)
#             if temp:
#                 proposed_time += max(temp)
#             # print("proposed_time, base_time", proposed_time, base_time)
#             if proposed_time < min_time:
#                 min_time = proposed_time
#                 best_saved_devices = saved_devices
#                 upload_time = get_broadcast_time(a, saved_devices)
#                 profit = base_time - proposed_time
#
#         # 如果没有比basetime更好的方案
#         if best_saved_devices == "not found":
#             upload_time = get_broadcast_time(a, ['BS'])
#             best_saved_devices = []
#             profit = 0
#
#         broadcast_upload_memo[memo_key] = (upload_time, best_saved_devices, profit)
#
#     else:
#         upload_time, best_saved_devices, profit = broadcast_upload_memo.get(memo_key)
#
#     return upload_time, best_saved_devices, profit
#     # 本轮上传时间，下轮被节省时间的设备，净节省时间
#
#
#
# def get_round_time(args, refresh=False, print_data=True, show_figure=False):
#     # return FedAvg_round_time, RoundRobin_round_time, FedBroadcast_round_time
#
#     # 算之前看看有没有缓存过
#     # 缓存的key：(seed, epochs, num_users, frac, local_ep, local_bs, data_num, R, alpha, N0, C_path_loss, B, cpu_frequency, P_base_station, P_device, model_size, macs)
#     if not refresh:
#         cache_file_path = "../cache"
#         cache_file_name = "get_round_time.cache"
#         cache = {}
#         cache_key = (
#             args.seed, args.epochs, args.num_users, args.frac, args.local_ep, args.local_bs, args.data_num, args.R, args.alpha, args.N0,
#             args.C_path_loss, args.B, args.cpu_frequency,
#             args.P_base_station, args.P_device, args.model_size, args.macs)
#         if os.path.exists(os.path.join(cache_file_path, cache_file_name)):
#             with open(os.path.join(cache_file_path, cache_file_name), "rb") as f:
#                 cache = pickle.load(f)
#                 if cache_key in cache.keys():
#                     print("命中cache", cache_key)
#                     return cache[cache_key]
#                 else:
#                     print("缓存未命中", cache_key)
#         else:
#             print("未找到缓存文件", cache_key)
#     else:
#         # 不去管有没有缓存过，直接重新计算
#         cache = {}
#         cache_key = (
#             args.seed, args.epochs, args.num_users, args.frac, args.local_ep, args.local_bs, args.data_num, args.R,
#             args.alpha, args.N0,
#             args.C_path_loss, args.B, args.cpu_frequency,
#             args.P_base_station, args.P_device, args.model_size, args.macs)
#
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
#
#     ##############################################
#     # FedAvg #####################################
#     ##############################################
#     FedAvg_round_time, FedAvg_scheduled_devices = \
#         get_FedAvg_round_time(args, devices_download_latencies, devices_computation_latencies, devices_upload_BS_latencies)
#     if print_data:
#         print("FedAvg_round_time", FedAvg_round_time)
#         print()
#
#     ##############################################
#     # RoundRobin ################################
#     ##############################################
#     RoundRobin_round_time, RoundRobin_scheduled_devices, RoundRobin_partition_lst = \
#         get_RoundRobin_round_time(args, devices_download_latencies, devices_computation_latencies, devices_upload_BS_latencies)
#
#
#
#     ##############################################
#     # FedBroadcast ###############################
#     ##############################################
#     all_devices = list(range(args.num_users))  # all devices' index
#     broadcast_upload_memo = {}  # 计算上传时间的备忘录
#     FedBroadcast_scheduled_devices = []
#     # 获取设备分组信息
#     devices_partition_lst = get_partition_lst(args, devices_download_latencies)
#     print("fb devices_partition_lst", devices_partition_lst)
#     if print_data:
#         print("FedBroadcast_devices_partition_lst ", devices_partition_lst)
#
#
#     # 寻找最有利于上传的一个顺序  opt_order
#     @timeout(5)
#     def get_opt_order(devices_partition_lst):
#         all_order = get_all_possible_order(len(devices_partition_lst))
#         res_dic = {}
#         broadcast_upload_memo = {}
#         for order in all_order:
#             sum_upload_time = 0
#             sum_profit = 0
#             for i in range(len(order)):
#                 f = order[i]
#                 if i + 1 <= len(order) - 1:
#                     t = order[i + 1]
#                 else:
#                     t = order[0]
#                 # print("@", f, "->", t)
#                 upload_time, saved_devices, profit = broadcast_upload(devices_partition_lst[f], devices_partition_lst[t],
#                                                                       broadcast_upload_memo, devices_locations,
#                                                                       devices_download_latencies,
#                                                                       devices_computation_latencies,
#                                                                       devices_upload_BS_latencies, args)
#                 sum_upload_time += upload_time
#                 sum_profit += profit
#             res_dic[tuple(order)] = (sum_upload_time, sum_profit)
#         lst = sorted(res_dic.items(), key=lambda item: item[1][1], reverse=True)
#         print("order profit lst:", lst)
#         opt_order = lst[0][0]
#         return opt_order
#     try:
#         opt_order = get_opt_order(devices_partition_lst)
#         is_timeout = False
#     except Exception as e:
#         print(e, "Error: get_opt_order 用时超过5秒")
#         opt_order = [i for i in range(len(devices_partition_lst))]
#         is_timeout = True
#     # print("sorted lst ", lst)
#     if print_data:
#         print("FedBroadcast_opt_order", opt_order)
#
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
#     t = 0  # 第i轮所用的累计时间
#     sum_upload_profit = 0
#     saved_devices = []
#     for i in range(args.epochs):
#         round_devices = FedBroadcast_scheduled_devices[i]  # 本轮设备
#         if i == args.epochs - 1:
#             next_round_devices = []  # 下轮设备
#         else:
#             next_round_devices = FedBroadcast_scheduled_devices[i + 1]  # 下轮设备
#
#         # 基站下发和计算 （广播下发，时间取决于最慢的那个设备，下发和计算可以是并行的，取两者之和的最大值）
#         temp = []  # 存放下一轮所有设备的下发+计算时间
#         for device in round_devices:
#             if device not in saved_devices:
#                 temp.append(devices_download_latencies[device] +
#                             devices_computation_latencies[device])
#             else:
#                 temp.append(devices_computation_latencies[device])
#         t += max(temp)
#         # print(1111)
#         # 设备上传阶段 (广播上传，选取最佳的上传方案，争取能节省下轮的下发时间）
#         if is_timeout:
#             upload_time = sum([devices_upload_BS_latencies[i] for i in round_devices])
#             saved_devices = []
#             profit = 0
#         else:
#             upload_time, saved_devices, profit = broadcast_upload(round_devices, next_round_devices,
#                                                                   broadcast_upload_memo,
#                                                                   devices_locations, devices_download_latencies,
#                                                                   devices_computation_latencies,
#                                                                   devices_upload_BS_latencies, args)
#
#         # print(2222)
#         t += upload_time
#         sum_upload_profit += profit
#         # print("upload profit", profit)
#         # print("saved devices", saved_devices)
#         FedBroadcast_round_time.append(t)
#
#     if print_data:
#         print("FedBroadcast_sum_upload_profit", sum_upload_profit)
#         print("FedBroadcast_round_time", FedBroadcast_round_time)
#         print()
#     if show_figure:
#         show_devices_info(devices_locations, devices_download_latencies, devices_computation_latencies, args)
#         show_devices_partition(devices_locations, devices_download_latencies, devices_computation_latencies,
#                                devices_partition_lst, args)
#
#     # return FedAvg_round_time, RoundRobin_round_time, FedBroadcast_round_time
#
#     # ms -> s
#     res = [i / 1000 for i in FedAvg_round_time], [i / 1000 for i in RoundRobin_round_time], [i / 1000 for i in
#                                                                                              FedBroadcast_round_time], \
#           FedAvg_scheduled_devices, RoundRobin_scheduled_devices, FedBroadcast_scheduled_devices
#
#     cache[cache_key] = res
#     # 将计算得到的结果缓存下来
#     if not os.path.exists(cache_file_path):
#         os.makedirs(cache_file_path)
#     with open(os.path.join(cache_file_path, cache_file_name), "wb") as f:
#         pickle.dump(cache, f)
#
#     return res
#
# # 随机抽取
# def get_FedAvg_round_time(args, devices_download_latencies, devices_computation_latencies,
#                           devices_upload_BS_latencies, broadcast=False):
#     ##############################################
#     # FedAvg #####################################
#     ##############################################
#     all_devices = list(range(args.num_users))  # all devices' index
#     m = max(int(args.frac * args.num_users), 1)  # 向下取整
#     print("FedAvg K x C = ", m)
#     FedAvg_scheduled_devices = []
#     seed_all(args.seed)
#     for i in range(args.epochs):
#         FedAvg_scheduled_devices.append(np.random.choice(all_devices, size=m, replace=False).tolist())
#     FedAvg_round_time = []
#     t = 0  # 第i轮的累计时间
#     for round_devices in FedAvg_scheduled_devices:
#         if broadcast:
#             # 基站广播下发
#             temp = []  # 存放下一轮所有设备的下发+计算时间
#             for device in round_devices:
#                 temp.append(devices_download_latencies[device])
#             t += max(temp)
#         else:
#             # 基站下发 （一个一个下发）
#             for device in round_devices:  # device是设备的索引号
#                 t += devices_download_latencies[device]
#         # 设备计算阶段  （计算可以是并行的，取最大值）
#         t += max([devices_computation_latencies[device] for device in round_devices])
#         # 设备上传阶段 (一个一个上传）
#         for device in round_devices:  # device是设备的索引号
#             t += devices_upload_BS_latencies[device]
#         FedAvg_round_time.append(t)
#     return FedAvg_round_time, FedAvg_scheduled_devices
#
#
# # 随机分组
# def get_RoundRobin_round_time(args, devices_download_latencies, devices_computation_latencies, devices_upload_BS_latencies):
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
#     t = 0  # 第i轮的累计时间
#     for round_devices in RoundRobin_scheduled_devices:
#         # 基站下发阶段 （一个一个下发）
#         for device in round_devices:  # device是设备的索引号
#             t += devices_download_latencies[device]
#         # 设备计算阶段  （计算可以是并行的，取最大值）
#         t += max([devices_computation_latencies[device] for device in round_devices])
#         # 设备上传阶段 (一个一个上传）
#         for device in round_devices:  # device是设备的索引号
#             t += devices_upload_BS_latencies[device]
#         RoundRobin_round_time.append(t)
#
#     return RoundRobin_round_time, RoundRobin_scheduled_devices, devices_group_lst
