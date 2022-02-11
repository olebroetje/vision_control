import cv2
import matplotlib.pyplot as plt
import numpy as np

image_input = cv2.imread("test_image.jpg")
plt.imshow(image_input)
plt.show()
scale = 0.25
image = cv2.resize(image_input, (int(image_input.shape[1] * scale), int(image_input.shape[0] * scale)))
# greyscale
image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# create lines
image_lines = cv2.Canny(image_greyscale, 100, 200)

plt.figure()
plt.imshow(image_lines)
plt.show()

lines = cv2.HoughLinesP(
    image_lines,
    rho=6,
    theta=np.pi / 60,
    threshold=160,
    lines=np.array([]),
    minLineLength=40,
    maxLineGap=25
)


def draw_lines(img, _lines, color=None, thickness=3):
    if color is None:
        color = [0, 0, 255]
    if _lines is None:
        return img
    img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in _lines:
        for x1, y1, x2, y2 in line:
            img = cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    return img


# line_image = draw_lines(image, lines)
cv2.namedWindow('test', )
# plt.figure()
# plt.imshow(line_image)
# plt.show()
while True:
    cv2.imshow('test', image_lines)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
