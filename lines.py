import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


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
