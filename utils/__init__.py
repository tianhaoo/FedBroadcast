#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @python: 3.6

import random
import torch
import numpy as np
import os

from thop import profile


def seed_all(seed):
    #固定随机性
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    torch.manual_seed(seed)  # 为CPU设置随机种子
    torch.cuda.manual_seed(seed)  # 为当前GPU设置随机种子
    torch.cuda.manual_seed_all(seed)  # 为所有GPU设置随机种子`
    torch.backends.cudnn.deterministic = True  # 每次返回的卷积算法将是确定的，即默认算法。 可以保证每次运行网络的时候相同输入的输出是固定的
    torch.backends.cudnn.benchmark = False  # 牺牲速度，换取精度，True是为整个网络的每个卷积层搜索最适合它的卷积实现算法，进而实现网络的加速


def get_model_info(net, img_size, args):
    batch_image = torch.randn((args.local_bs,) + img_size).to(args.device)
    macs, params = profile(net, inputs=(batch_image,))
    return macs, params * 32  # Total params * 32 bit  , float32

if __name__ == "__main__":
    pass








