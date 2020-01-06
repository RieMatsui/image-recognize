import cv2

img = cv2.imread("../img/img01.jpg")
#
# height = img.shape[0]
# width = img.shape[1]
#
height, width = img.shape[:2]
print("image width: " + str(width))
print("image height: " + str(height))

# resize image
resized_img = cv2.resize(img, (width // 2, height // 2))
# show image
cv2.imshow("img", resized_img)
cv2.waitKey(0)