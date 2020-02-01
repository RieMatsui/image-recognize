import cv2

from modules.frontal_face_detector import FrontalFaceDetector
from modules.read_image import ReadImage


class MainFrontalFaceDetector:

    RES_PATH = "../tmp/temp.jpg"
    READ_PATH = "../img/img02.jpg"
    SHAPE_PREDICTOR_DATA = "../resources/shape_predictor_68_face_landmarks.dat",
    TITLE = "human face"

    frontal_face_detector = FrontalFaceDetector(SHAPE_PREDICTOR_DATA, READ_PATH)
    frontal_face_detector.detect_frontal_face()

    read_image = ReadImage(frontal_face_detector.image, TITLE)
    res_image = frontal_face_detector.image

    cv2.imwrite(RES_PATH, res_image)

    resize_image = read_image.resize_image()
    read_image.show_image(resize_image)











