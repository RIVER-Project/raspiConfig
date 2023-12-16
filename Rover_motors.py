
servo180_1 = 535
servo180_2 = 2590

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

##right -1
front_right360 = 0
front_left360 = 1
middle_right360 = 2
middle_left360 = 3
rear_right360 = 4
rear_left360 = 5

k = 1


for i in range(6,12):
  kit.servo[i].set_pulse_width_range(servo180_1, servo180_2)


while k:
  kit.continuous_servo[front_right360].throttle = -1
  kit.continuous_servo[front_left360].throttle = 1
  kit.continuous_servo[middle_right360].throttle = -1
  kit.continuous_servo[middle_left360].throttle = 1
  kit.continuous_servo[rear_right360].throttle = -1
  kit.continuous_servo[rear_left360].throttle = 1
  k = int(input("Enter an integer: "))
for i in range(6):
 kit.continuous_servo[i].throttle = 0.03

  # kit.continuous_servo[front_left360].throttle = 1
  # kit.servo[front_right180].angle = 90
