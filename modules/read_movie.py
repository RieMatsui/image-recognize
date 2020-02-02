import cv2
import pandas
import matplotlib.pyplot as plt


class ReadMovie(object):

    def __init__(self, movie_name):
        capture = cv2.VideoCapture(movie_name)
        self.capture = capture
        self.width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        self.frame_per_second = capture.get(cv2.CAP_PROP_FPS)

    def print_value(self):
        print("image width : " + str(self.width))
        print("image height : " + str(self.height))
        print("total frame count : " + str(self.count))
        print("FPS : " + str(self.frame_per_second))
        number = 0

    def show_movie(self):
        number = 0
        # show movie
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                cv2.imshow("frame", frame)
                # divide avi
                file_path = "../snapshot/snapshot_" + str(number) + ".jpeg"
                cv2.imwrite(file_path, frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    print(str(number) + ": image was output.")
                    break
            number = number + 1
        self.capture.release()
        cv2.destroyAllWindows()

    @staticmethod
    def get_human_hog():
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        return hog

    def get_human_obj(self, frame):
        hog = self.get_human_hog()
        hog_params = {'winStride': (8, 8),
                      'padding': (32, 32),
                      'scale': 1.05,
                      'hitThreshold': 0,
                      'finalThreshold': 5
                      }
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        human, r = hog.detectMultiScale(gray, **hog_params)
        return human

    def prepare_save_movie(self, save_file_path):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        video = cv2.VideoWriter(save_file_path, fourcc, 30, (int(self.width), int(self.height)))
        return video

    def analysis_people_traffic(self, people_traffic_graph):
        num = 0
        people_traffic_graph.list_df
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                if num % 10 == 0:
                    human = self.get_human_obj(frame)
                    if len(human) > 0:
                        for (x, y, w, h) in human:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)
                        people_traffic_graph.append_value(num, self.frame_per_second, len(human))
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
            else:
                break
            num = num + 1
        self.capture.release()
        cv2.destroyAllWindows()

    def make_time_lapse(self, video):
        num = 0
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                if num % 10 == 0:
                    human = self.get_human_obj(frame)
                    if len(human) > 0:
                        for (x, y, w, h) in human:
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)
                    video.write(frame)
            else:
                break
            num = num + 1

        video.release()
        self.capture.release()
        cv2.destroyAllWindows()
