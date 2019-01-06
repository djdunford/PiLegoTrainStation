#!/usr/bin/env python3
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

# import LCD controller library
from RPLCD.i2c import CharLCD

# import time library
import time

# Set the GPIO PIN naming mode
GPIO.setmode(GPIO.BCM)

# set up display
lcd = CharLCD(i2c_expander='PCF8574',address=0x27,port=1,cols=20,rows=4,dotsize=8,charmap='A02',auto_linebreaks=False,backlight_enabled=True)

# set up station list and initial departures
stations = ['Petersfield','King\'s Cross','Worcester','Royston','Hitchin','Letchworth','Bristol','Oxford','Cardiff','Baldock','Stevenage','Welwyn','Finsbury Pk','Blackfriars','Brighton','St. Pancras','Knebworth']
departures = [{'Name':'Petersfield','Time':15},{'Name':'Worcester','Time':30}]

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

# timer for redrawing LCD (every 'interval' seconds)
interval = 5.0
starttime = time.time()-interval-1.0

# loop forever
while True:

	# if interval expired, redraw LCD
	if time.time()>starttime+interval:
		lcd.home()
		for departure in departures:
			lcd.write_string(departure['Name'] + '\n\r')
		starttime=time.time()

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
		
	# 

	time.sleep(0.1)
