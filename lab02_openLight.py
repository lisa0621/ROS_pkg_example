#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import rospy

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(18, GPIO.OUT)  # led

try:
    while True:
        if GPIO.input(17) == GPIO.LOW:
            GPIO.output(18, GPIO.HIGH)
            print('Button Pressed...')
            time.sleep(0.2)
        else:
            GPIO.output(18, GPIO.LOW)
except:
    GPIO.cleanup()
