#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import rospy

BUTTON_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print('button')
        time.sleep(0.2)
except KeyboardInterrupt:
    print('close')
finally:
    GPIO.cleanup()
