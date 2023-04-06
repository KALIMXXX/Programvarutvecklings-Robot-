#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)

# Write your program here.
ev3.speaker.beep()
arm_motor.run_angle(100,-300, then=Stop.HOLD, wait=False)

turning_motor.run_until_stalled(-100, then=Stop.HOLD, duty_limit=None)

current_color = None

while (current_color == None and turning_motor.stalled() == False):
    color = color_sensor.color()
    turning_motor.run_angle(300,-10, then=Stop.HOLD, wait=True)

claw_motor.run_until_stalled(300, then=stop.HOLD, duty_limit=None)

arm_motor.coast()

claw_motor.run_until_stalled(-300, then=stop.HOLD, duty_limit=None)

arm_motor.run_until_stalled(300, then=stop.HOLD, duty_limit=None)