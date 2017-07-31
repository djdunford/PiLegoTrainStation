#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  onesignal.py
#  
#  Copyright 2017  Darren Dunford
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
# import GPIO library
import RPi.GPIO as GPIO

# import time library
import time

# Set the GPIO PIN naming mode
GPIO.setmode(GPIO.BCM)

# Suppress warnings for GPIO usage clashes
GPIO.setwarnings(False)

# Set BCM lines for buttons and lights
ButtonRed=19
ButtonAmber=20
ButtonGreen=21
LightRed=7
LightAmber=8
LightGreen=25

# Set the light pins as outputs and switch them on
# all 3 lights on is a one-time condition that
# indicates a successful startup
GPIO.setup(LightRed, GPIO.OUT)
GPIO.output(LightRed, GPIO.HIGH)
GPIO.setup(LightAmber, GPIO.OUT)
GPIO.output(LightAmber, GPIO.HIGH)
GPIO.setup(LightGreen, GPIO.OUT)
GPIO.output(LightGreen, GPIO.HIGH)

# Set all button pins as an input pins, and enable
# the internal pull-up resistors
GPIO.setup(ButtonRed, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ButtonAmber, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ButtonGreen, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# loop forever
while True:

	# if a button is pressed, turn on the appropriate light
	# and turn the other lights off
	if GPIO.input(ButtonRed)==GPIO.LOW:
		GPIO.output(LightRed, GPIO.HIGH)
		GPIO.output(LightAmber, GPIO.LOW)
		GPIO.output(LightGreen, GPIO.LOW)
	if GPIO.input(ButtonAmber)==GPIO.LOW:
		GPIO.output(LightRed, GPIO.LOW)
		GPIO.output(LightAmber, GPIO.HIGH)
		GPIO.output(LightGreen, GPIO.LOW)
	if GPIO.input(ButtonGreen)==GPIO.LOW:
		GPIO.output(LightRed, GPIO.LOW)
		GPIO.output(LightAmber, GPIO.LOW)
		GPIO.output(LightGreen, GPIO.HIGH)

	time.sleep(0.1)
