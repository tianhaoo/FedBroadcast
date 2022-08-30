import pickle
import matplotlib.pyplot as plt
from scipy import signal
import math


def show_devices_info(devices_locations, devices_download_latencies, devices_computation_latencies, args):
    device_lst = list(range(args.num_users))
    device_lst.sort(key=lambda x: devices_download_latencies[x] + devices_computation_latencies[x], reverse=True)
    x_lst = []
    y_lst = []
    for d in device_lst:
        x_lst.append(devices_locations[d][0])
        y_lst.append(devices_locations[d][1])

    # print(x_lst, y_lst)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 设置坐标轴范围
    r = args.R
    ax.set_xlim((-r, r))
    ax.set_ylim((-r, r))
    circ = plt.Circle((0, 0), r, color='b', alpha=0.1)  # 圆心，半径，颜色，透明度
    ax.add_patch(circ)
    ax.scatter(x_lst, y_lst, s=50)
    plt.axis('equal')  # changes limits of x or y axis so that equal increments of x and y have the same length
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title(u"设备位置分布情况")

    # 显示文字
    for d in device_lst:
        plt.text(devices_locations[d][0], devices_locations[d][1], round(math.sqrt(devices_locations[d][0] ** 2 + devices_locations[d][1] ** 2 )))
    plt.show()



    x = [i for i in range(1, len(device_lst)+1)]
    y1 = [devices_computation_latencies[i] for i in device_lst]
    y2 = [devices_download_latencies[i] for i in device_lst]
    plt.bar(x, y2, color='green', label=u'BS广播给设备用时')
    plt.bar(x, y1, bottom=y2, color='red', label=u'计算用时')
    plt.legend()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title(u"广播时间和计算时间")
    plt.ylabel('Time (ms)')
    plt.xlabel('device')
    plt.show()


# 图表显示设备分组方案
def show_devices_partition(devices_locations, devices_download_latencies, devices_computation_latencies, partition_lst, args):
    # 展示设备分组情况
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 设置坐标轴范围
    r = args.R
    ax.set_xlim((-r, r))
    ax.set_ylim((-r, r))
    circ = plt.Circle((0, 0), r, color='b', alpha=0.05)  # 圆心，半径，颜色，透明度
    ax.add_patch(circ)
    ax.plot(0, 0, 'bv')

    for i in range(len(partition_lst)):
        x_lst = []
        y_lst = []
        for d in partition_lst[i]:
            x_lst.append(devices_locations[d][0])
            y_lst.append(devices_locations[d][1])
        # ax.scatter(x_lst, y_lst, s=100)

        for j in range(len(x_lst)):
            ax.text(x_lst[j], y_lst[j], i, size=15)

        # 用于画设备上传半径
        # if i == 6:
        #     for j in range(len(x_lst)):
        #         circ = plt.Circle((x_lst[j], y_lst[j]), math.sqrt((x_lst[j] ** 2) + (y_lst[j] ** 2)), color='y', alpha=0.1)  # 圆心，半径，颜色，透明度
        #         ax.add_patch(circ)
    plt.axis('equal')  # changes limits of x or y axis so that equal increments of x and y have the same length
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title(u"设备分组情况")
    plt.show()

    tbc_plt_lst = []
    tcp_plt_lst = []
    download_lst = []
    upload_lst = []
    for sub_set in partition_lst:
        download_lst.append(max([devices_download_latencies[i] for i in sub_set]))
        upload_lst.append(sum([devices_download_latencies[i] for i in sub_set]))
        for i in sub_set:
            tbc_plt_lst.append(devices_download_latencies[i])
            tcp_plt_lst.append(devices_computation_latencies[i])
        tbc_plt_lst.append(0)
        tcp_plt_lst.append(0)
    x = range(0, sum([len(group) for group in partition_lst]) + len(partition_lst))
    plt.bar(x, tbc_plt_lst, color='green', label=u'BS广播给设备用时')
    plt.bar(x, tcp_plt_lst, bottom=tbc_plt_lst, color='red', label=u'计算用时')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.title(u"设备分组情况2")
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

    print("download_lst", sum(download_lst), download_lst)
    print("upload_lst", sum(upload_lst), upload_lst)


def show_dict_users(partition_lst, dict_users, labels):
    x_lst = list(range(len(partition_lst)))
    # 先把一组的数据合并到一起
    group_datas = []
    for group in partition_lst:
        group_data = set()
        for user in group:
            group_data = group_data.union(dict_users[user])
        group_datas.append(group_data)
    # 统计每组内，每类的个数
    group_sums = []
    for group_data in group_datas:
        group_sum = [0 for i in range(10)]
        for data in group_data:
            group_sum[int(labels[data])] += 1
        group_sums.append(group_sum)

    y_lsts = []
    for i in range(10):
        y_lst = []
        for group_sum in group_sums:
            y_lst.append(group_sum[i])
        y_lsts.append(y_lst)

    for y_lst in y_lsts:
        # plt.ylim(0, 1000)
        print(y_lst)
        plt.plot(x_lst, y_lst, marker='o')
    print()
    plt.show()
    return y_lsts


def show_group_dataset_test(group_dataset_test, labels):
    x_lst = list(range(len(group_dataset_test)))
    # 统计每组内，每类的个数
    group_sums = []
    for group_id, group_data in group_dataset_test.items():
        group_sum = [0 for i in range(10)]
        for data in group_data:
            group_sum[int(labels[data])] += 1
        group_sums.append(group_sum)

    y_lsts = []
    for i in range(10):
        y_lst = []
        for group_sum in group_sums:
            y_lst.append(group_sum[i])
        y_lsts.append(y_lst)

    for y_lst in y_lsts:
        plt.ylim(0, 200)
        plt.plot(x_lst, y_lst, marker='o')
    plt.show()




if __name__ == "__main__":
    pass
