#!/usr/bin/python 
import sys
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')

import RPi.GPIO as GPIO 
import time 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(22, GPIO.OUT) 
while True: 
   print("On")
   GPIO.output(22, True) 
   time.sleep(1) 
   print("Off")
   GPIO.output(22, False) 
   time.sleep(1)
