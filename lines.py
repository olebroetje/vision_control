import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def draw_lines(img, _lines, color=None, thickness=1):
    if color is None:
        color = [0, 0, 255]
    if _lines is None:
        return
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in _lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    img_return = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    return img_return


while True:
    success, image = cap.read()

    image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_lines = cv2.Canny(image_greyscale, 50, 300)

    if image_lines is not None:
        cv2.imshow('line_detection', image_lines)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow('line_detection')
