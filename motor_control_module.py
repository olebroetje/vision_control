class MotorController:

    def __init__(self, speed: int):
        self.speed = speed
        self.MotorLeft = 1
        self.MotorRight = 2

    def setSpeed(self, speed: int):
        self.speed = speed

    def turnRight(self):
        # TODO: add Arduino communication
        pass

    def turnLeft(self):
        # TODO: add Arduino communication
        pass

    def driveForward(self):
        pass

    def fullTurnLeft(self):
        pass

    def fullTurnRight(self):
        pass
