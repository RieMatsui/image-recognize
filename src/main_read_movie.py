from modules.read_movie import ReadMovie


class MainReadMove:
    read_movie = ReadMovie("../mov/mov01.avi")
    read_movie.print_value()
    read_movie.show_movie()
