#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
touch_sensor = TouchSensor(Port.S1)

def calibrate():

        while touch_sensor.pressed() == False:
        turning_motor.run_angle(300, 20, then=Stop.HOLD, wait=True)
        turning_motor.reset_angle(0)

    claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_angle(50,70, then=Stop.HOLD, wait=True)

    print(turning_motor.angle())
    print(claw_motor.angle())

    return

def turn_angle(given_angle):

    arm_motor.run_angle(300,-400, then=Stop.HOLD, wait=True)

    while touch_sensor.pressed() == False:
        turning_motor.run_angle(300, 20, then=Stop.HOLD, wait=True)

    turning_motor.reset_angle(0)

    desiered_angle = given_angle

    turning_motor.run_target(200,(desiered_angle*-3.5))

    """Turning motor to right angle"""
    return

def pick_up():
    
    claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)
    claw_motor.reset_angle(0)

    claw_motor.run_angle(50,70, then=Stop.HOLD, wait=True)

    arm_motor.run_angle(300,400, then=Stop.COAST, wait = True)
    

    claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)

    item_found = False

    if claw_motor.angle() > 10:
        item_found = True
    else:
        item_found = False
    
    arm_motor.run_angle(300,-400, then=Stop.HOLD, wait=True)
    
    return item_found




def pick_up_angle(given_angle):

    # ev3.speaker.beep()
    arm_motor.run_angle(300,-400, then=Stop.HOLD, wait=True)

    while touch_sensor.pressed() == False:
        turning_motor.run_angle(300, 20, then=Stop.HOLD, wait=True)

    turning_motor.reset_angle(0)

    desiered_angle = given_angle

    turning_motor.run_target(200,(desiered_angle*-3.5))

    """Turning motor to right angle"""

    claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)
    claw_motor.reset_angle()

    claw_motor.run_angle(50,70, then=Stop.HOLD, wait=True)


    arm_motor.run_angle(300,400, then=Stop.COAST, wait = True)
    

    claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)

    item_found = False

    if claw_motor.angle() > 10:
        item_found = True
    else:
        item_found = False
    
    arm_motor.run_angle(300,-400, then=Stop.HOLD, wait=True)
    return item_found

   

def put_down():
    arm_motor.run_angle(300,400, then=Stop.COAST, wait = True)

    claw_motor.run_angle(50, 70, then=Stop.HOLD, wait=True)
    
    return

def check_color():
    arm_motor.run_angle(300, 200, then=Stop.HOLD, wait= True)
    time.sleep(1)
    current_color = color_sensor.color()
    print(current_color)
    arm_motor.run_angle(300, -200, then=Stop.HOLD, wait = True)
    return

def run_until_found(given_angle):
    
    item_found = False
    while item_found == False:
      turn_angle(given_angle):  

    time.sleep(5)
    return


check_color()
