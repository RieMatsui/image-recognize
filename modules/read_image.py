import cv2


class ReadImage(object):

    def __init__(self, file_name, title):
        image = cv2.imread(file_name)
        height, width = image.shape[:2]
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        self.image = image
        self.height = height
        self.width = width
        self.title = title
        self.gray = gray

    def print_value(self):
        print("image width: " + str(self.width))
        print("image height: " + str(self.height))

    def resize_image(self):
        # resize image
        resized_image = cv2.resize(self.image, (self.width // 2, self.height // 2))
        return resized_image

    def show_image(self, image):
        # show image
        cv2.imshow(self.title, image)
        cv2.waitKey(0)

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

    def human_rectangle(self):
        human = self.get_human_obj()
        if len(human) > 0:
            for (x, y, w, h) in human:
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 255, 255), 3)
