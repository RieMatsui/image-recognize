import cv2


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

    def get_human_obj(self):
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        hog_params = {'winStride': (8, 8),
                      'padding': (32, 32),
                      'scale': 1.05,
                      'hitThreshold': 0,
                      'finalThreshold': 5
                      }
        human, r = hog.detectMultiScale(self.gray, **hog_params)
        return human

