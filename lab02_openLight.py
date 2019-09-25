#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import rospy

BUTTON_PIN = 17
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button
GPIO.setup(LED_PIN, GPIO.OUT)  # led

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == False:
            GPIO.output(LED_PIN, True)
            print('Button Pressed...')
            time.sleep(0.2)
        else:
            GPIO.output(LED_PIN, False)
except:
    GPIO.cleanup()
