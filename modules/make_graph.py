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
        self.max_x = 0
        self.max_y = 0
        self.average_x = 0
        self.average_y = 0

    def show_graph(self, row_frag, average_flag):
        if row_frag:
            plt.plot(self.list_df[self.x_column], self.list_df[self.y_column], label=self.label)
        if average_flag:
            self.moving_average()
            plt.plot(self.average_x, self.average_y, label="average")
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

    def moving_average(self):
        x, y = self.list_df[self.x_column], self.list_df[self.y_column]
        self.average_y = np.convolve(y, np.ones(5)/float(5), mode="valid")
        self.average_x = np.linspace(np.min(x), np.max(x), np.size(self.average_y))
