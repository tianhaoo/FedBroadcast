#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pickle
import random
import numpy as np

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torch.optim as optim
from torchvision import datasets, transforms

from utils.options import args_parser
from models.Nets import MLP, CNNMnist, CNNCifar


def test(net_g, data_loader):
    # testing
    net_g.eval()
    test_loss = 0
    correct = 0
    l = len(data_loader)
    for idx, (data, target) in enumerate(data_loader):
        data, target = data.to(args.device), target.to(args.device)
        log_probs = net_g(data)
        test_loss += F.cross_entropy(log_probs, target).item()
        y_pred = log_probs.data.max(1, keepdim=True)[1]
        correct += y_pred.eq(target.data.view_as(y_pred)).long().cpu().sum()

    test_loss /= len(data_loader.dataset)
    print('\nTest set: Average loss: {:.4f} \nAccuracy: {}/{} ({:.2f}%)\n'.format(
        test_loss, correct, len(data_loader.dataset),
        100. * correct / len(data_loader.dataset)))

    return 100. * correct / len(data_loader.dataset), test_loss


if __name__ == '__main__':
    # parse args
    args = args_parser()
    args.device = torch.device('cuda:{}'.format(args.gpu) if torch.cuda.is_available() and args.gpu != -1 else 'cpu')

    torch.manual_seed(args.seed)

    #固定随机性
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    # cudnn.benchmark = True
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    # load dataset and split users
    if args.dataset == 'mnist':
        dataset_train = datasets.MNIST('./data/mnist/', train=True, download=True,
                                       transform=transforms.Compose([
                                           transforms.ToTensor(),   # ToTensor()能够把灰度范围从0-255变换到0-1之间
                                           transforms.Normalize(mean=(0.1307,), std=(0.3081,))  # image = (image - mean) / std
                                       ]))
        img_size = dataset_train[0][0].shape
    elif args.dataset == 'cifar':
        transform = transforms.Compose(
            [transforms.ToTensor(),   # ToTensor()能够把灰度范围从0-255变换到0-1之间
             transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))])  # transform.Normalize()则把0-1变换到(-1,1)
        dataset_train = datasets.CIFAR10('./data/cifar', train=True, transform=transform, target_transform=None,
                                         download=True)
        img_size = dataset_train[0][0].shape
    else:
        exit('Error: unrecognized dataset')
    print("img_size", img_size)

    # build model
    if args.model == 'cnn' and args.dataset == 'cifar':
        net_glob = CNNCifar(args=args).to(args.device)
    elif args.model == 'cnn' and args.dataset == 'mnist':
        net_glob = CNNMnist(args=args).to(args.device)
    elif args.model == 'mlp':
        len_in = 1
        for x in img_size:
            len_in *= x
        net_glob = MLP(dim_in=len_in, dim_hidden=64, dim_out=10).to(args.device)
    else:
        exit('Error: unrecognized model')
    print(net_glob)

    # training
    optimizer = optim.SGD(net_glob.parameters(), lr=args.lr, momentum=args.momentum)
    train_loader = DataLoader(dataset_train, batch_size=64, shuffle=True)

    list_loss = []
    list_acc = []
    record = {}
    net_glob.train()
    for epoch in range(args.epochs):
        print("epoch", epoch)
        batch_loss = []
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(args.device), target.to(args.device)
            optimizer.zero_grad()
            output = net_glob(data)
            loss = F.cross_entropy(output, target)
            loss.backward()  # 对损失函数求导
            optimizer.step()
            if args.verbose and batch_idx % 50 == 0:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(train_loader.dataset),
                           100. * batch_idx / len(train_loader), loss.item()))
            batch_loss.append(loss.item())
        loss_avg = sum(batch_loss) / len(batch_loss)
        print('\nTrain loss:', loss_avg)
        list_loss.append(loss_avg)

        # 动态减少学习率
        args.lr *= args.decay
        optimizer = optim.SGD(net_glob.parameters(), lr=args.lr, momentum=args.momentum)

        # testing
        if args.dataset == 'mnist':
            dataset_test = datasets.MNIST('./data/mnist/', train=False, download=True,
                                          transform=transforms.Compose([
                                              transforms.ToTensor(),
                                              transforms.Normalize((0.1307,), (0.3081,))
                                          ]))
            test_loader = DataLoader(dataset_test, batch_size=1000, shuffle=False)
        elif args.dataset == 'cifar':
            transform = transforms.Compose(
                [transforms.ToTensor(),
                 transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
            dataset_test = datasets.CIFAR10('./data/cifar', train=False, transform=transform, target_transform=None,
                                            download=True)
            test_loader = DataLoader(dataset_test, batch_size=1000, shuffle=False)
        else:
            exit('Error: unrecognized dataset')

        print('test on', len(dataset_test), 'samples')
        test_acc, test_loss = test(net_glob, test_loader)
        list_acc.append(test_acc)

    # plot loss
    plt.figure()
    plt.plot(range(len(list_loss)), list_loss)
    plt.xlabel('epochs')
    plt.ylabel('train loss')
    plt.savefig('./main_nn_save/nn_{}_{}_{}.loss.png'.format(args.dataset, args.model, args.epochs))

    # plot acc
    plt.figure()
    plt.plot(range(len(list_acc)), list_acc)
    plt.xlabel('epochs')
    plt.ylabel('test acc')
    plt.savefig('./main_nn_save/nn_{}_{}_{}.acc.png'.format(args.dataset, args.model, args.epochs))

    record["loss_train_lst"] = list_loss
    record["acc_test_lst"] = list_acc
    record["args"] = args
    pickle.dump(record, open(
        './main_nn_save/nn_{}_{}_{}.record'.format(args.dataset, args.model, args.epochs),
        'wb'))



