from modules.read_image import ReadImage


class MainHumanFace:

    READ_PATH = "../../img/img02.jpg"
    RES_PATH = "../../tmp/temp.jpg"
    TITLE = "human faces"

    human_face_image = ReadImage(READ_PATH, TITLE)
    human_face_image.mark_detected_face(RES_PATH)
    res_face_image = ReadImage(RES_PATH, TITLE)
    resize_face_image = res_face_image.resize_image()
    res_face_image.show_image(resize_face_image)
