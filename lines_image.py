import cv2

image_input = cv2.imread("test_image.jpg")
scale = 0.25
image = cv2.resize(image_input, (1000, 1000))
image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_lines = cv2.Canny(image_greyscale, 100, 200)
cv2.imshow('test', image_lines)
cv2.waitKey(-1)
cv2.destroyAllWindows()
