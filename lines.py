import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def draw_lines(img, lines, color=None, thickness=1):
    if color is None:
        color = [0, 0, 255]
    if lines is None:
        return
    line_img = np.zeros(
        (
            img.shape[0],
            img.shape[1],
            3
        ),
        dtype=np.uint8,
    )
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    img_return = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    return img_return


while True:
    success, image = cap.read()

    # greyscale
    image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # create lines
    image_lines = cv2.Canny(image_greyscale, 50, 300)

    # plt.figure()
    # plt.imshow(image_lines)
    # plt.show()

    lines = cv2.HoughLinesP(
        image_lines,
        rho=5,
        theta=np.pi / 60,
        threshold=180,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25
    )

    line_image = draw_lines(image, lines)
    if line_image is not None:
        cv2.imshow('line_detection', line_image)
    print(f"fps: {cap.get(cv2.CAP_PROP_FPS)}")
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow('line_detection')
