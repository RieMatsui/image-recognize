import cv2

import modules.read_image as read_image


class HumanFace(object):

    def __init__(self, image_file):
        self.image = cv2.imread(image_file)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def get_face_list(self):
        cv2.CascadeClassifier("../resources/haarcascade_frontalface_alt.xml")
        face_list = self.cascade.detectMultiScale(self.gray, minSize=(50, 50))
        return face_list

    def mark_detected_face(self, write_image_path):

        face_list = self.get_face_list()

        for (x, y, w, h) in face_list:
            color = (0, 0, 225)
            pen_w = 3
            cv2.rectangle(self.image, (x, y), (x + w, y + h), color, thickness=pen_w)

        cv2.imwrite(write_image_path, self.image)
        cv2.waitKey(0)

    def resize_image(self):
        # resize image
        resized_image = cv2.resize(self.image, (self.width // 2, self.height // 2))
        return resized_image


class MainHumanFace:

    human_face = HumanFace("../img/img02.jpg")
    human_face.mark_detected_face("img", "../tmp/temp.jpg")
    human_face_image = read_image.ReadImage("../tmp/temp.jpg", "human faces")
    human_face_image.show_image()

