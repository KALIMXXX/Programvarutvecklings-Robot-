# PA1473 - Software Development: Agile Project (Template)

## Introduction

This code is designed to guide and control a lego ev3bricks robot to accomplish designated tasks that were ordered by the user.

## Getting started

Connect your robot to a USB Micro cable and connect the cable to an USB port in your computer. Start the robot by holding in the big middle button. After the robot has booted up, open the code in VSS and click on "Click here to connect a device" located under the "EV3DEV DEVICE BROWSER" tab in the bottom right corner of the screen. Click on the corresponding port to connect the robot. The robot should now be connected and a green dot with the name of the robot should be listed under "EV3DEV DEVICE BROWSER".

## Building and running

To operate the robot, pick one or more of the listed Functions and insert the parameters (if there are any) and then press F5 on your keyboard to upload and execute the code to the robot.
Use the pre-made functions to make the robot do the desired tasks by putting functions in the desired order.

The parameters "given_angle", "pos" and "pick_up_zone" are in degrees (0°-180°) and tells the robot in what position the action should take place. The parameter "heigt" tells the robot on which height (0-5) an obejct is located (Mainly used in the "pick_up" and "put_down" functions)

## Features

- [x] US01 : As a customer, I want the robot to pick up items
- [x] US01B: As a customer, I want the robot to pick up items from a designated position
- [x] US02 : As a customer, I want the robot to drop off items
- [x] US02B: As a customer, I want the robot to drop off items at a designated position
- [x] US03 : As a customer, I want the robot to be able to determine if an item is present at a given location
- [x] US04 : As a customer, I want the robot to tell me the color of an item
- [x] US04B: As a customer, I want the robot to tell me the color of an item at a designated position
- [x] US05 : As a customer, I want the robot to drop items off at different locations based on the color of the item
- [x] US06 : As a customer, I want the robot to be able to pick up items from elevated positions
- [x] US08 : As a customer, I want to be able to calibrate maximum of three different colors and assign them to specific drop-off zones.
- [x] US08B: As a customer, I want to be able to calibrate maximum of three different colors and assign them to specific drop-off zones, based on color
- [x] US09 : As a customer, I want the robot to check the pick up location periodically to see if a new item has arrived
- [x] US10 : As a customer, I want the robot to sort items at a specific time
- [ ] US11 : As a customer, I want two robots to communicate and work together on items sorting without colliding with each other (40)
- [x] US12 : As a customer, I want to be able to manually set the locations and heights of one pick up zone and two drop off zones (13)