from modules.read_movie import ReadMovie
from modules.make_graph import MakeGraph


class MainMakeGraph:

    print("Start analysis")
    read_movie = ReadMovie("../../mov/mov01.avi")
    people_traffic_graph = MakeGraph("time", "people", "row", "time(sec.)", "people")
    read_movie.analysis_people_traffic(people_traffic_graph, False)
    people_traffic_graph.print_max_and_min_num()
    print("Finish analysis")
