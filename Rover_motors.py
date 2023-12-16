
servo180_1 = 535
servo180_2 = 2590

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

front_right360 = 0

front_right180 = 5

front_left180 = 7


for i in range(6,12):
  kit.servo[i].set_pulse_width_range(servo180_1, servo180_2)

while True:
  kit.continuous_servo[front_right360].throttle = 1
  kit.servo[front_left180].angle = 90
