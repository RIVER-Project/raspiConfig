
servo180_1 = 535
servo180_2 = 2590

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

front_right360 = 0
front_right180 =



for i in range(6,12):
  kit.servo[i].set_pulse_width_range(servo180_1, servo180_2)

while True:
  kit.continuous_servo[0].throttle = 1
