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

    while touch_sensor.pressed() == False:
        turning_motor.run_angle(300, 20, then=Stop.HOLD, wait=True)
        turning_motor.reset_angle(0)
    claw_motor.run_until_stalled(-50, then=Stop.HOLD, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_angle(50,85, then=Stop.HOLD, wait=True)
    arm_motor.run_until_stalled(-300, then=Stop.HOLD, duty_limit=5)

    arm_motor.run_until_stalled(400, then=Stop.HOLD, duty_limit=15)
    arm_motor.run_angle(300,-415, then=Stop.HOLD, wait=True)
    return

def turn_angle(given_angle):
    arm_motor.hold()
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
    
def put_down(pos,height):
    turn_angle(pos)
    height1 = (370/5)*height
    height2 = (-1)*((370/5)*height) 
    arm_motor.run_angle(300,height1, then=Stop.HOLD, wait = True)
    claw_motor.run_angle(50, 85, then=Stop.HOLD, wait=True)
    arm_motor.run_angle(300,height2, then=Stop.HOLD, wait = True)
    return

def check_color():
    arm_motor.run_angle(300, 150, then=Stop.HOLD, wait= True)
    time.sleep(1)
    current_color = color_sensor.color()
    arm_motor.run_angle(300, -150, then=Stop.HOLD, wait = True)
    print(current_color)
    return current_color

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
    pick_up(1)
    turn_angle(pos)
    
    
    color = check_color()
    return color


#US05
def drop_based_on_color(pickupzone):
    calibrate()
    turn_angle(pickupzone)
    pick_up(0)
    color = check_color()
    print(color)
    if color == Color.BLUE:
        put_down(0, 5)
    elif color == Color.RED:
        put_down(90), 5
    elif color == Color.GREEN:
        put_down(180, 5)

    
#US08 and US12
def sort_based_on_color(pickupzone):
    height1 = 5
    height2 = 3
    height3 = 0
    calibrate()
    turn_angle(pickupzone)
    pick_up(0)
    color = check_color()
    while color not in [Color.BLUE, Color.RED, Color.GREEN]:
        color = check_color()
    print(color)
    if color == Color.BLUE:
        put_down(0, height1)
    elif color == Color.RED:
        put_down(90, height1)
    elif color == Color.GREEN:
        put_down(180, height1)

    turn_angle(pickupzone)
    pick_up(1)
    color = check_color()
    while color not in [Color.BLUE, Color.RED, Color.GREEN]:
        color = check_color()
    print(color)
    if color == Color.BLUE:
        put_down(0, height2)
    elif color == Color.RED:
        put_down(90, height2)
    elif color == Color.GREEN:
        put_down(180, height2)

    turn_angle(pickupzone)
    pick_up(1)
    color = check_color()
    while color not in [Color.BLUE, Color.RED, Color.GREEN]:
        color = check_color()
    print(color)
    if color == Color.BLUE:
        put_down(0, height3)
    elif color == Color.RED:
        put_down(90, height3)
    elif color == Color.GREEN:
        put_down(180, height3)


def sort_based_on_color_wait(pickupzone):
    time.sleep(10)
    height1 = 5
    height2 = 5
    height3 = 5
    calibrate()
    turn_angle(pickupzone)
    pick_up(0)
    color = check_color()
    while color not in [Color.BLUE, Color.RED, Color.GREEN]:
        color = check_color()
    print(color)
    if color == Color.BLUE:
        put_down(0, height1)
    elif color == Color.RED:
        put_down(90, height1)
    elif color == Color.GREEN:
        put_down(180, height1)

    turn_angle(pickupzone)
    pick_up(1)
    color = check_color()
    while color not in [Color.BLUE, Color.RED, Color.GREEN]:
        color = check_color()
    print(color)
    if color == Color.BLUE:
        put_down(0, height2)
    elif color == Color.RED:
        put_down(90, height2)
    elif color == Color.GREEN:
        put_down(180, height2)

    turn_angle(pickupzone)
    pick_up(1)
    color = check_color()
    while color not in [Color.BLUE, Color.RED, Color.GREEN]:
        color = check_color()
    print(color)
    if color == Color.BLUE:
        put_down(0, height3)
    elif color == Color.RED:
        put_down(90, height3)
    elif color == Color.GREEN:
        put_down(180, height3)    

drop_based_on_color(45)

