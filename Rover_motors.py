
servo180_1 = 535
servo180_2 = 2590

import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

for i in range(6,12):
  kit.servo[i].set_pulse_width_range(servo180_1, servo180_2)

while True:
 for i in range(3):
  kit.continuous_servo[i].throttle = -0.3
 for i in range(3,6):
  kit.continuous_servo[i].throttle = 0.3
 for i in range(6,12):
  kit.servo[i].angle = 180