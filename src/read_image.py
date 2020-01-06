import cv2


class ReadImage(object):

    def __init__(self, file_name):
        image = cv2.imread(file_name)
        height, width = image.shape[:2]
        self.image = image
        self.height = height
        self.width = width

    def print_value(self):
        print("image width: " + str(self.width))
        print("image height: " + str(self.height))

    def resize_image(self):
        # resize image
        resized_image = cv2.resize(self.image, (self.width // 2, self.height // 2))
        return resized_image

    def show_image(self):
        # show image
        cv2.imshow("img", self.resize_image())
        cv2.waitKey(0)


class MainShowImage:
    read_image = ReadImage("../img/img01.jpg")
    read_image.print_value()
    read_image.resize_image()
    read_image.show_image()