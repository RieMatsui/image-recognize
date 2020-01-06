import cv2

# prepare
cascade_file = "../resources/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

# detection
img = cv2.imread("../img/img02.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_list = cascade.detectMultiScale(gray, minSize=(50, 50))

# mark detected face
for (x, y, w, h) in face_list:
    color = (0, 0, 225)
    pen_w = 3
    cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness=pen_w)
cv2.imshow("img", img)
cv2.imwrite("../tmp/temp.jpg", img)
cv2.waitKey(0)