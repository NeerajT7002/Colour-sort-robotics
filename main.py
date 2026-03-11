from pyfirmata2 import Arduino
import cv2
import numpy as np
import time

board = Arduino('COM4')

base = board.get_pin('d:3:s')
shoulder = board.get_pin('d:5:s')
elbow = board.get_pin('d:6:s')
gripper = board.get_pin('d:9:s')

def safe_write(servo, angle):
    angle = max(0, min(180, int(angle)))
    servo.write(angle)

BASE_HOME = 90

SHOULDER_HOME = 60
ELBOW_HOME = 100

SHOULDER_PICK = 72
ELBOW_PICK = 85

SHOULDER_LIFT = 38

POST_DROP_SHOULDER = 50

GRIP_OPEN = 40
GRIP_CLOSE = 187

DROP_RED = 20
DROP_GREEN = 90
DROP_BLUE = 160

safe_write(base, BASE_HOME)
safe_write(shoulder, SHOULDER_HOME)
safe_write(elbow, ELBOW_HOME)
safe_write(gripper, GRIP_OPEN)

cap = cv2.VideoCapture("http://10.180.42.234:4747/video")

frame_center_tolerance = 40

picked = False

def move_servo_slow(servo,start,end,step=2,delay=0.02):

    start=int(start)
    end=int(end)

    if start < end:
        rng=range(start,end,step)
    else:
        rng=range(start,end,-step)

    for a in rng:
        safe_write(servo,a)
        time.sleep(delay)

    safe_write(servo,end)

def close_gripper():

    for a in range(GRIP_OPEN, GRIP_CLOSE, 3):
        safe_write(gripper,a)
        time.sleep(0.02)

    safe_write(gripper,GRIP_CLOSE)

def detect_colors(frame):

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    r1=cv2.inRange(hsv,(0,120,70),(10,255,255))
    r2=cv2.inRange(hsv,(170,120,70),(180,255,255))
    red=r1+r2

    green=cv2.inRange(hsv,(40,70,70),(80,255,255))
    blue=cv2.inRange(hsv,(100,150,50),(140,255,255))

    return red,green,blue

while True:

    ret,frame=cap.read()
    if not ret:
        break

    frame=cv2.flip(frame,1)
    frame_width=frame.shape[1]

    red,green,blue=detect_colors(frame)

    colors={
        "RED":(red,DROP_RED),
        "GREEN":(green,DROP_GREEN),
        "BLUE":(blue,DROP_BLUE)
    }

    for name,(mask,drop_angle) in colors.items():

        contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        if contours:

            largest=max(contours,key=cv2.contourArea)

            if cv2.contourArea(largest)>4000:

                x,y,w,h=cv2.boundingRect(largest)
                cx=x+w//2

                target_angle=int((cx/frame_width)*180)

                # BASE TRACKING ONLY WHEN NOT PICKING
                if not picked:
                    safe_write(base,target_angle)

                if abs(cx-frame_width/2)<frame_center_tolerance and not picked:

                    picked=True

                    print("Picking",name)

                    move_servo_slow(shoulder,SHOULDER_HOME,SHOULDER_PICK)
                    move_servo_slow(elbow,ELBOW_HOME,ELBOW_PICK)

                    close_gripper()

                    time.sleep(0.8)

                    # LIFT FIRST
                    move_servo_slow(shoulder,SHOULDER_PICK,SHOULDER_LIFT)

                    # NOW ROTATE
                    move_servo_slow(base,target_angle,drop_angle)

                    safe_write(gripper,GRIP_OPEN)

                    time.sleep(0.5)

                    move_servo_slow(shoulder,SHOULDER_LIFT,POST_DROP_SHOULDER)

                    move_servo_slow(base,drop_angle,BASE_HOME)
                    move_servo_slow(shoulder,POST_DROP_SHOULDER,SHOULDER_HOME)
                    move_servo_slow(elbow,ELBOW_PICK,ELBOW_HOME)

                    picked=False

                break

    cv2.imshow("Robot Vision",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()