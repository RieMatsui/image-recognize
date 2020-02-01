import cv2
import dlib
import math


class FrontalFaceDetector(object):

    def __init__(self, predictor_data, image_path):

        self.predictor = dlib.shape_predictor(predictor_data)
        self.detector = dlib.get_frontal_face_detector()
        self.image = cv2.imread(image_path)

        # Display of face area
        self.color_f = (0, 0, 255)
        self.color_l_out = (0, 255, 0)
        self.color_l_in = (0, 255, 0)
        self.line_w = 3
        self.circle_r = 3
        self.font_type = cv2.FONT_HERSHEY_SIMPLEX
        self.font_size = 1

        self.gx_out = 0
        self.gy_out = 0
        self.gx_in = 0
        self.gy_in = 0

    def detect_frontal_face(self):
        res_detector = self.detector(self.image, 1)
        for k, d, in enumerate(res_detector):
            shape = self.predictor(self.image, d)

            cv2.rectangle(self.image, (d.left(), d.top()), (d.right(), d.bottom()), self.color_f, self.line_w)
            cv2.putText(self.image, str(k), (d.left(), d.top()), self.font_type, self.font_size,
                        self.color_f, self.line_w)

            self.draw_gravity_position(shape)
            self.calculate_orientation(d)

    def draw_gravity_position(self, shape):
        # contour of face point
        num_points_out = 17
        num_points_in = shape.num_parts - num_points_out

        for shape_point_count in range(shape.num_parts):
            shape_point = shape.part(shape_point_count)

            # When a part inside the contour is detected
            if shape_point_count < num_points_out:
                cv2.circle(self.image, (shape_point.x, shape_point.y), self.circle_r, self.color_l_out, self.line_w)

                self.gx_out = self.gx_out + shape_point.x / num_points_out
                self.gy_out = self.gy_out + shape_point.x / num_points_out

            # When a contour is detected
            else:
                cv2.circle(self.image, (shape_point.x, shape_point.y), self.circle_r, self.color_l_in, self.line_w)

                self.gx_in = self.gx_in + shape_point.x / num_points_in
                self.gy_in = self.gy_in + shape_point.x / num_points_in

        # Draw the center of gravity position
        self.draw_center_gravity_position()

    # Draw the center of gravity position
    def draw_center_gravity_position(self):
        cv2.circle(self.image, (int(self.gx_in), int(self.gy_in)), self.circle_r, (0, 0, 0), self.line_w)
        cv2.circle(self.image, (int(self.gx_out), int(self.gy_out)), self.circle_r, (0, 0, 255), self.line_w)

    # Calculate face orientation
    def calculate_orientation(self, d):
        theta = math.asin(2 * (self.gx_in - self.gx_out) / (d.right() - d.left()))
        radian = theta * 180 / math.pi
        print("face orientation:{} (angle: {} degrees)".format(theta, radian))

        # Show face orientation
        self.show_orientation(d, radian)

    # Show face orientation
    def show_orientation(self, d, radian):
        # Show face orientation
        if radian < 0:
            text_prefix = "  letf "
        else:
            text_prefix = "  rigth "
        text_show = text_prefix + str(round(abs(radian), 1)) + "deg."
        cv2.putText(self.image, text_show, (d.left(), d.top()), self.font_type, self.font_size,
                    self.color_f, self.line_w)


class MainFrontalFaceDetector:

    frontal_face_detector = FrontalFaceDetector("../resources/shape_predictor_68_face_landmarks.dat",
                                                "../img/img02.jpg")
    frontal_face_detector.detect_frontal_face()
    cv2.imshow("img", frontal_face_detector.image)
    cv2.imwrite("../tmp/temp.jpg", frontal_face_detector.image)
    cv2.waitKey(0)











