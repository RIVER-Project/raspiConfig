
servo180_1 = 535
servo180_2 = 2590

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def controlM(a):
 kit.servo[a].angle = 0
 time.sleep(0.5)
 kit.servo[a].angle = 90
 time.sleep(0.5)
 kit.servo[a].angle = 180
 time.sleep(0.5)
 kit.servo[a].angle = 90
 time.sleep(0.5)

###360
##right -1
front_right360 = 0
front_left360 = 1
middle_right360 = 2
middle_left360 = 3
rear_right360 = 4
rear_left360 = 5


###180

front_right180 = 6
front_left180 = 7
middle_right180 = 8
middle_left180 = 9
k = 0

for i in range(6,12):
  kit.servo[i].set_pulse_width_range(servo180_1, servo180_2)


while k:
  kit.continuous_servo[front_right360].throttle = -1
  kit.continuous_servo[front_left360].throttle = 1
  kit.continuous_servo[middle_right360].throttle = -1
  kit.continuous_servo[middle_left360].throttle = 1
  kit.continuous_servo[rear_right360].throttle = -1
  kit.continuous_servo[rear_left360].throttle = 1
  #k = int(input("Enter an integer: "))

while True:
 #controlM(front_right180)
 #controlM(front_left180)
 controlM(middle_right180)
 controlM(middle_left180)

for i in range(6):
 kit.continuous_servo[i].throttle = 0.03


