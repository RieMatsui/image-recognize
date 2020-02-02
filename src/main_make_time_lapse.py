from modules.read_movie import ReadMovie


class MainMakeTimeLapse:

    MOVIE_PATH = "../mov/mov01.avi"
    SAVE_MOVIE_PATH = "../tmp/time_lapse.avi"
    print("Start generating time lapse.")
    read_movie = ReadMovie(MOVIE_PATH)
    video = read_movie.prepare_save_movie(SAVE_MOVIE_PATH)
    read_movie.make_time_lapse(video)
    print("Finish generating time lapse.")

