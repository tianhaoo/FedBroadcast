import argparse


def draw_args_parser():
    parser = argparse.ArgumentParser()

    # 颜色参数
    parser.add_argument('--unicast_color', type=str, default='r', help='随机抽取不广播颜色')
    parser.add_argument('--randsel_color', type=str, default='g', help='随机抽取广播颜色')
    parser.add_argument('--randgroup_color', type=str, default='b', help='随机分组广播颜色')
    parser.add_argument('--optgroup_color', type=str, default='gold', help='最优分组广播颜色')
    parser.add_argument('--class_color', type=list, default=['r', 'g', 'b', 'gold', 'pink', 'magenta', 'yellow', 'darkcyan', 'orange', 'dodgerblue'], help='类颜色列表')

    # 字体参数
    parser.add_argument('--family', type=str, default='Times New Roman', help='字体类型')
    parser.add_argument('--label_size', type=int, default='28', help='字体大小')
    parser.add_argument('--label_size2', type=int, default='26', help='字体大小')
    parser.add_argument('--legend_size', type=int, default='18', help='字体大小')
    parser.add_argument('--weight', type=str, default='normal', help='字体权重')
    parser.add_argument('--fontsize', type=int, default='16', help='两张较大图的label font size')
    parser.add_argument('--fontsize2', type=int, default='13', help='label font size')

    args = parser.parse_args()

    return args


draw_args = draw_args_parser()
legend_font = {
    'family': draw_args.family,
    'size': draw_args.legend_size,
    'weight': draw_args.weight,
}
label_font = {
    'family': draw_args.family,
    'size': draw_args.label_size,
    'weight': draw_args.weight,
}
label_font2 = {
    'family': draw_args.family,
    'size': draw_args.label_size2,
    'weight': draw_args.weight,
}
