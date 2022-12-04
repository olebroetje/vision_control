#include <Adafruit_MotorShield.h>
#define SHOULD_DRIVE 1
#define MOTORCONTROL_RIGHT 2
#define MOTORCONTROL_LEFT 3
#define MOTORCONTROL_STRAIGHT 4
#define INPUT_CONTROL 6
#define OUTPUT_CONTROL 7

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *right = AFMS.getMotor(2);
Adafruit_DCMotor *left = AFMS.getMotor(1);



void setup() {
  // put your setup code here, to run once:
  pinMode(LINE_RIGHT, INPUT);
  pinMode(LINE_LEFT, INPUT);
  pinMode(INPUT_CONTROL, INPUT);
  pinMode(SHOULD_DRIVE, INPUT);
  pinMode(OUTPUT_CONTROL, OUTPUT);
  AFMS.begin(1900);
  right->setSpeed(150);
  left->setSpeed(150);
}

void loop() {
  while (digitalRead(SHOULD_DRIVE) == true) {
    if (digitalRead(MOTORCONTROL_STRAIGHT) == HIGH) {
      right->run(FORWARD)
      left->run(FORWARD)
    } else if (digitalRead(MOTORCONTROL_RIGHT == HIGH)) {
      right->run(BACKWARD)
      left->run(FORWARD)
    } else if (digitalRead(MOTORCONTROL_LEFT == HIGH) {
    right->run(FORWARD)
      left->run(BACKWARD)
    }
  }
}
