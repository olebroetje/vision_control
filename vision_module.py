import cv2


class GreenBoxDetector:

    def __init__(self):
        self.cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.noDetection = 1
        self.Detection = 2

    def detect(self, frame):
        detections = self.cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in detections:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            print(f'x = {x}, y = {y}, w = {w}, h = {h} location of faces')
        return detections, frame, self.Detection if len(detections) > 0 else self.noDetection


class EndZoneDetector:

    def __init__(self):
        self.BlackBoxCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.BallCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.noDetectionBall = 1
        self.DetectionBall = 2
        self.noDetectionBlackBox = 3
        self.DetectionBlackBox = 4

    def detect(self, frame):
        ballDetection = self.BallCascade.detectMultiScale(frame, 1.3, 5)
        blackBoxDetection = self.BlackBoxCascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in ballDetection:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        for (x, y, w, h) in blackBoxDetection:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            return ballDetection, blackBoxDetection, frame, self.DetectionBall if ballDetection[0] is not None else \
                self.noDetectionBall, self.DetectionBlackBox if blackBoxDetection[0] is not None \
                else self.noDetectionBlackBox
