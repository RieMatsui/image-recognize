import cv2
from modules.read_movie import ReadMovie

print("Start generating time lapse.")

# get movie
cap = cv2.VideoCapture("../mov/mov01.avi")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# prepare hog param
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hog_Params = {'winStride': (8, 8),
              'padding': (32, 32),
              'scale': 1.05,
              'hitThreshold': 0,
              'finalThreshold': 5
              }

movie_name = "../tmp/time_lapse.avi"
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
video = cv2.VideoWriter(movie_name, fourcc, 30, (int(width), int(height)))

num = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        if num % 10 == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            human, r = hog.detectMultiScale(gray, **hog_Params)
            if len(human) > 0:
                for(x, y, w, h) in human:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)
            video.write(frame)
    else:
        break

    num = num + 1
video.release()
cap.release()
cv2.destroyAllWindows()

print("Finish generating time lapse.")


