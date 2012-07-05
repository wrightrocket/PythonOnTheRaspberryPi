#!/usr/bin/python
# Blink an LED connected to GPIO18

import time

# RPi.GPIO method
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
for TIMES in range(10):
    GPIO.output(18, True)
    time.sleep(1)
    GPIO.output(18, False)
    time.sleep(1)

# WiringPython method
OUTPUT=1
import wiringpi
wiringpi.wiringPiSetup()
wiringpi.wiringPiGpioMode(True)
wiringpi.pinMode(18, OUTPUT)
for TIMES in range(10):
    wiringpi.digitalWrite(18, True)
    time.sleep(1)
    wiringpi.digitalWrite(18, False)
    time.sleep(1)
