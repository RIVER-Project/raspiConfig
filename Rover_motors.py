
servo180_1 = 535
servo180_2 = 2590

import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

###360
##right -1

front_left360 = 0
front_right360 = 1
middle_left360 = 2
middle_right360 = 3
rear_left360 = 4
rear_right360 = 5

###180

front_left180 = 6
front_right180 = 7
middle_left180 = 8
middle_right180 = 9
rear_left180 = 10
rear_right180 = 11

for i in range(6, 12):
    kit.servo[i].set_pulse_width_range(servo180_1, servo180_2)

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
 kit.continuous_servo[front_right360].throttle = 1
 kit.continuous_servo[front_left360].throttle = -1
 kit.continuous_servo[middle_right360].throttle = 1
 kit.continuous_servo[middle_left360].throttle = -1
 kit.continuous_servo[rear_right360].throttle = 1
 kit.continuous_servo[rear_left360].throttle = -1


def forwardHalf():
 kit.continuous_servo[front_right360].throttle = 0.5
 kit.continuous_servo[front_left360].throttle = -0.5
 kit.continuous_servo[middle_right360].throttle = 0.5
 kit.continuous_servo[middle_left360].throttle = -0.5
 kit.continuous_servo[rear_right360].throttle = 0.5
 kit.continuous_servo[rear_left360].throttle = -0.5

def krabWalk():
  stopRover()
  time.sleep(1)
  for i in range(6,12):
   kit.servo[i].angle = 180
   # time.sleep(0.2)

def reverseKrab():
  stopRover()
  time.sleep(1)
  for i in range(6,12):
   kit.servo[i].angle = 90
   #time.sleep(0.2)
def backWard():
 kit.continuous_servo[front_right360].throttle = -1
 kit.continuous_servo[front_left360].throttle = 1
 kit.continuous_servo[middle_right360].throttle = -1
 kit.continuous_servo[middle_left360].throttle = 1
 kit.continuous_servo[rear_right360].throttle = -1
 kit.continuous_servo[rear_left360].throttle = 1

def stopRover():
 for i in range(6):
  kit.continuous_servo[i].throttle = 0.03

def circles():
 kit.servo[front_right360] = 125

def steer(angle):
     kit.servo[front_right180].angle = angle
     kit.servo[front_left180].angle = angle

def main():
 while True:
  try:
   choice = int(input("Option:\n1 Forward full\n2.Steer(angle)\n3.Forward Half\n4.Krab walk\n5.Reverse krab\n6.Backward\n7.Stop\n"))
   if choice == 1:
    forwardFull()
   elif choice == 2:
    angle = int(input("Choose angle: "))
    steer(angle)
   elif choice == 3:
    forwardHalf()
   elif choice == 4:
    krabWalk()
   elif choice == 5:
    reverseKrab()
   elif choice == 6:
    backWard()
   elif choice == 7:
    stopRover()
   else:
    print("Exiting the program.")
  except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

