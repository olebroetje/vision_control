import cv2
import time

from line_detection_module import LineDetector
from motor_control_module import MotorController
from vision_module import GreenBoxDetector

LDM = LineDetector()
MC = MotorController(speed=100)
GBD = GreenBoxDetector()
initial_end_time = time.time()
print(f"{time.process_time()} setup duration")

skipLineCheck = False

while True:
    move_command, frame, line_position = LDM.getMotorControl()
    objects, frame2, detection = GBD.detect(frame)  # Green Box
    if line_position is LDM.error:
        pass
    else:
        if detection is GBD.noDetection and skipLineCheck is False:
            if move_command == LDM.Right:
                MC.turnRight()
            elif move_command == LDM.Left:
                MC.turnLeft()
            else:
                MC.driveForward()
        else:
            print(len(objects))
            if len(objects) > 1:
                (x, y, w, h) = objects[0]
                (x2, y2, w2, h2) = objects[1]
                MC.driveForward()
                skipLineCheck = True
            else:
                skipLineCheck = False
                (x, y, w, h) = objects[0]
                if y < 80:
                    if line_position < x:
                        MC.fullTurnLeft()
                    else:
                        MC.fullTurnRight()
            cv2.imshow('camera_1', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

del LDM
del MC
