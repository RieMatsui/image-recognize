from modules.read_movie import ReadMovie
from modules.make_graph import MakeGraph


class MainCompareGraph:
    read_movie_1 = ReadMovie("../mov/mov01.avi")
    people_traffic_graph_1 = MakeGraph("time", "people", "1st", "time(sec.)", "people")
    read_movie_1.analysis_people_traffic(people_traffic_graph_1)

