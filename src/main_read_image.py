from modules.read_image import ReadImage


class MainReadImage:
    read_image = ReadImage("../img/img01.jpg", "img")
    read_image.print_value()
    resize_image = read_image.resize_image()
    read_image.show_image(resize_image)
