import matplotlib.pyplot as plt
import pandas
import numpy as np


class MakeGraph:

    def __init__(self, x_column, y_column, label, x_label, y_label):
        self.x_column = x_column
        self.y_column = y_column
        self.list_df = pandas.DataFrame(columns=[x_column, y_column])
        self.label = label
        self.x_label = x_label
        self.y_label = y_label

    def show_graph(self, average_flag):
        plt.plot(self.list_df[self.x_column], self.list_df[self.y_column], label=self.label)
        if average_flag:
            max_x, max_y = self.moving_average(self.list_df[self.x_column], self.list_df[self.y_column])
            plt.plot(max_x, max_y, label="average")
        plt.legend()
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()

    def print_max_and_min_num(self):
        print("max num " + self.x_label + " : " + str(self.list_df[self.x_column].max()))
        print("min num " + self.y_label + " : " + str(self.list_df[self.y_column].max()))

    def append_value(self, x_num, pfs, y_num):
        tmp_se = pandas.Series([x_num / pfs, y_num], index=self.list_df.columns)
        self.list_df = self.list_df.append(tmp_se, ignore_index=True)

    @staticmethod
    def moving_average(x, y):
        y_convolve = np.convolve(y, np.ones(5)/float(5), mode="valid")
        x_dat = np.linspace(np.min(x), np.max(x), np.size(y_convolve))
        return x_dat, y_convolve
