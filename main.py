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

# Main movement functions

def calibrate():
    arm_motor.run_until_stalled(400, then=Stop.HOLD, duty_limit=15)
    arm_motor.run_angle(300,-415, then=Stop.HOLD, wait=True)
    while touch_sensor.pressed() == False:
        turning_motor.run_angle(300, 20, then=Stop.HOLD, wait=True)
        turning_motor.reset_angle(0)
    claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_angle(50,85, then=Stop.HOLD, wait=True)
    arm_motor.run_until_stalled(300, then=Stop.HOLD, duty_limit=5)
    return

def turn_angle(given_angle):
    desiered_angle = given_angle
    turning_motor.run_target(200,(desiered_angle*-3.5))
    return

def pick_up(height):
    ## Chose a height 1-5
    chosen_height = (370)-(height*74)
    if  height < 0:
        pass
    elif height > 5:
        pass
    else:
        arm_motor.run_angle(300, chosen_height, then=Stop.HOLD, wait = True)
        claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)
        item_found = False
        if claw_motor.angle() > 10:
            item_found = True
        else:
            item_found = False
            claw_motor.run_angle(50,85, then=Stop.HOLD, wait=True)
        arm_motor.run_angle(300,-1*chosen_height, then=Stop.HOLD, wait=True)
        print(item_found)
        return item_found
    
def put_down(pos):
    turn_angle(pos)
    arm_motor.run_angle(300,370, then=Stop.COAST, wait = True)
    claw_motor.run_angle(50, 85, then=Stop.HOLD, wait=True)
    arm_motor.run_angle(300,-370, then=Stop.COAST, wait = True)
    return

def check_color():
    arm_motor.run_angle(300, 150, then=Stop.HOLD, wait= True)
    time.sleep(3)
    current_color = color_sensor.color()
    print(current_color)
    arm_motor.run_angle(300, -150, then=Stop.HOLD, wait = True)
    return

def run_until_found(given_angle):
    item_found = False
    while item_found == False:
        turn_angle(90)
        turn_angle(given_angle)
        item_found = pick_up(0)
        turn_angle(90)
        time.sleep(5)
    return

# Complicated functions

def check_color_pos(pos):
    turn_angle(pos)
    pick_up(0)
    check_color()



calibrate()
check_color_pos(90)
put_down(180)
turn_angle(90)