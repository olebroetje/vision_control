import cv2


class LineDetector:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.Right = 1
        self.Left = 2
        self.noMovementCommand = 0
        self.error = -1

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def getMotorControl(self):

        ret_cap, frame = self.cap.read()
        (w, h) = (frame.shape[1], frame.shape[0])
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        ret_thresh, thresh = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.line(frame, (cx, 0), (cx, 720), (255, 0, 0), 1)
                cv2.line(frame, (0, cy), (1280, cy), (255, 0, 0), 1)
                cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)
                border_left = (w / 2 - 20)
                border_right = (w / 2 + 20)
                if cx <= border_left:
                    print(f"Turn Left! cx = {cx} w = {w}")
                    return self.Left, frame, cx
                elif cx >= border_right:
                    print(f"Turn Right cx = {cx} w = {w}")
                    return self.Right, frame, cx
                else:
                    print(f"On Track! cx = {cx} w = {w}")
                    return self.noMovementCommand, frame, cx
            else:
                print("I don't see the line")
                return self.error, frame, 0
