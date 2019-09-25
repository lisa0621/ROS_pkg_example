#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import rospy

BUTTON_PIN = 17
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('botton')
        time.sleep(0.1)
        else:
            GPIO.output(LED_PIN, GPIO.HIGH)
except KeyboardInterrupt:
    print('close')
finally:
    GPIO.cleanup()
