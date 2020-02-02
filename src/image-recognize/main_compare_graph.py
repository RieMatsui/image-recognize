import matplotlib.pyplot as plt
from modules.read_movie import ReadMovie
from modules.make_graph import MakeGraph


class MainCompareGraph:
    read_movie_1 = ReadMovie("../../mov/mov01.avi")
    people_graph_1 = MakeGraph("time", "people", "1st", "time(sec.)", "people")
    read_movie_1.analysis_people_traffic(people_graph_1)
    people_graph_1.moving_average()

    read_movie_2 = ReadMovie("../../mov/mov02.avi")
    people_graph_2 = MakeGraph("time", "people", "2st", "time(sec.)", "people")
    read_movie_2.analysis_people_traffic(people_graph_2)
    people_graph_2.moving_average()

    plt.plot(people_graph_1.average_x, people_graph_1.average_y, label=people_graph_1.label)
    plt.plot(people_graph_2.average_x, people_graph_2.average_y, label=people_graph_2.label)
    plt.xlabel(people_graph_1.x_label)
    plt.ylabel(people_graph_1.y_label)
    plt.ylim(0, 15)
    plt.legend()
    plt.show()

