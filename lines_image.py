import cv2

image_input = cv2.imread("test_image.jpg")
scale = 0.25
image = cv2.resize(image_input, (int(image_input.shape[1] * scale), int(image_input.shape[0] * scale)))
image_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_lines = cv2.Canny(image_greyscale, 100, 200)


while True:
    cv2.imshow('test', image_lines)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
