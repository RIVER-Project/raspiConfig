
servo180_1 = 535
servo180_2 = 2590

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

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
rear_right180 = 10
rear_left180 = 11

def controlM(a):
 kit.servo[a].angle = 0
 time.sleep(0.5)
 kit.servo[a].angle = 90
 time.sleep(0.5)
 kit.servo[a].angle = 180
 time.sleep(0.5)
 kit.servo[a].angle = 90
 time.sleep(0.5)

def forwardFull():
 kit.continuous_servo[front_right360].throttle = -1
 kit.continuous_servo[front_left360].throttle = 1
 kit.continuous_servo[middle_right360].throttle = -1
 kit.continuous_servo[middle_left360].throttle = 1
 kit.continuous_servo[rear_right360].throttle = -1
 kit.continuous_servo[rear_left360].throttle = 1

def forwardHalf():
 kit.continuous_servo[front_right360].throttle = -0.5
 kit.continuous_servo[front_left360].throttle = 0.5
 kit.continuous_servo[middle_right360].throttle = -0.5
 kit.continuous_servo[middle_left360].throttle = 0.5
 kit.continuous_servo[rear_right360].throttle = -0.5
 kit.continuous_servo[rear_left360].throttle = 0.5

def krabWalk():
  for i in (6,12):
   kit.servo[i].angle = 180
   time.sleep(1)
  time.sleep(2)
  kit.continuous_servo[front_right360].throttle = -0.5
  kit.continuous_servo[front_left360].throttle = 0.5
  kit.continuous_servo[middle_right360].throttle = -0.5
  kit.continuous_servo[middle_left360].throttle = 0.5
  kit.continuous_servo[rear_right360].throttle = -0.5
  kit.continuous_servo[rear_left360].throttle = 0.5

def backWard():
 kit.continuous_servo[front_right360].throttle = 1
 kit.continuous_servo[front_left360].throttle = -1
 kit.continuous_servo[middle_right360].throttle = 1
 kit.continuous_servo[middle_left360].throttle = -1
 kit.continuous_servo[rear_right360].throttle = 1
 kit.continuous_servo[rear_left360].throttle = -1

def stopRover():
 for i in range(6):
  kit.continuous_servo[i].throttle = 0.03


# def perform_operation(operator):
#  if operator in operations:
#   operations[operator]

# for i in range(6,12):
#   kit.servo[i].set_pulse_width_range(servo180_1, servo180_2)

operations = {
  '1': forwardFull(),
  '2': forwardHalf(),
  '3': krabWalk(),
  '4': backWard(),
  '0': stopRover()
 }
