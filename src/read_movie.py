import cv2

# get information

cap = cv2.VideoCapture("../mov/mov01.avi")
num = 0
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
print("image width : " + str(width))
print("image height : " + str(height))
print("total frame count : " + str(count))
print("FPS : " + str(fps))

# show movie
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
        # divide avi
        filePath = "../snapshot/snapshot_" + str(num) + ".jpeg"
        cv2.imwrite(filePath, frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print(str(num) + ": image was output.")
            break
    num = num + 1
cap.release()
cv2.destroyAllWindows()