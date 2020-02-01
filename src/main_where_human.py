from modules.read_image import ReadImage


class MainWhereHuman:
    read_image = ReadImage("../img/img01.jpg", "img")
    read_image.get_human_obj()
    read_image.human_rectangle()
    resize_image = read_image.resize_image()
    read_image.show_image(resize_image)
