import cv2
import dlib
import math

# prepare
predictor = dlib.shape_predictor("../resources/shape_predictor_68_face_landmarks.dat")
detector = dlib.get_frontal_face_detector()

# detection
img = cv2.imread("../img/img02.jpg")
dets = detector(img, 1)

for k, d, in enumerate(dets):
    shape = predictor(img, d)
    # Display of face area
    color_f = (0, 0, 255)
    color_l_out = (0, 255, 0)
    color_l_in = (0, 255, 0)
    line_w = 3
    circle_r = 3
    font_type = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 1

    cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), color_f, line_w)
    cv2.putText(img, str(k), (d.left(), d.top()), font_type, font_size, color_f, line_w)

    # Prepare a box to guide the center of gravity
    num_points_out = 17
    num_points_in = shape.num_parts - num_points_out

    gx_out = 0
    gy_out = 0
    gx_in = 0
    gy_in = 0

    for shape_point_count in range(shape.num_parts):
        shape_point = shape.part(shape_point_count)

        if shape_point_count < num_points_out:
            cv2.circle(img, (shape_point.x, shape_point.y), circle_r, color_l_out, line_w)

            gx_out = gx_out + shape_point.x / num_points_out
            gy_out = gy_out + shape_point.x / num_points_out

        else:
            cv2.circle(img, (shape_point.x, shape_point.y), circle_r, color_l_in, line_w)

            gx_in = gx_in + shape_point.x / num_points_in
            gy_in = gy_in + shape_point.x / num_points_in

    # Draw the center of gravity position
    cv2.circle(img, (int(gx_in), int(gy_in)), circle_r, (0, 0, 0), line_w)
    cv2.circle(img, (int(gx_out), int(gy_out)), circle_r, (0, 0, 255), line_w)

    # Calculate face orientation
    theta = math.asin(2 * (gx_in - gx_out) / (d.right() - d.left()))
    radian = theta * 180 / math.pi
    print("face orientation:{} (angle: {} degrees)".format(theta, radian))

    # Show face orientation
    if radian < 0:
        text_prefix = "  letf "
    else:
        text_prefix = "  rigth "
    text_show = text_prefix + str(round(abs(radian), 1)) + "deg."
    cv2.putText(img, text_show, (d.left(), d.top()), font_type, font_size, color_f, line_w)

cv2.imshow("img", img)
cv2.imwrite("../tmp/temp.jpg", img)
cv2.waitKey(0)







