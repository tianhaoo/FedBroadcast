import matplotlib.pyplot as plt
from scipy import signal

def show_four_img(file_path, smooth=False):
    with open(file_path) as f:
        lst = f.readlines()
        count = 0
        acc_train_lst = []
        loss_train_lst = []
        acc_test_lst = []
        loss_test_lst = []
        for s in lst:
            a = s.replace("Round", " ").replace(", Train Accuracy", " ").replace(", Test Accuracy", " ").replace(", Train Loss", " ").replace(", Test Loss", " ")
            b = a.split()
            if count %2 == 0:
                acc_train_lst.append(float(b[1]))
                loss_train_lst.append(float(b[2]))
            else:
                acc_test_lst.append(float(b[1]))
                loss_test_lst.append(float(b[2]))
            count += 1

        if smooth:
            plt.title("loss_train_lst")
            plt.plot(range(len(loss_train_lst)), signal.savgol_filter(loss_train_lst, 19, 3))
            plt.show()

            plt.title("acc_test_lst")
            plt.plot(range(len(acc_test_lst)), signal.savgol_filter(acc_test_lst, 19, 3))
            plt.show()

            plt.title("loss_test_lst")
            plt.plot(range(len(loss_test_lst)), signal.savgol_filter(loss_test_lst, 19, 3))
            plt.show()

            plt.title("acc_train_lst")
            plt.plot(range(len(acc_train_lst)), signal.savgol_filter(acc_train_lst, 19, 3))
            plt.show()
        else:
            plt.title("loss_train_lst")
            plt.plot(range(len(loss_train_lst)), loss_train_lst)
            plt.show()

            plt.title("acc_test_lst")
            plt.plot(range(len(acc_test_lst)), acc_test_lst)
            plt.show()

            plt.title("loss_test_lst")
            plt.plot(range(len(loss_test_lst)), loss_test_lst)
            plt.show()

            plt.title("acc_train_lst")
            plt.plot(range(len(acc_train_lst)), acc_train_lst)
            plt.show()



show_four_img("./cifar_mlp_noniid.txt", smooth=False)