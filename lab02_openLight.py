#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import rospy

BUTTON_PIN = 17
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

ledState = False
try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            ledState = not ledState
            GPIO.output(LED_PIN, ledState)
            print('Press')
        time.sleep(0.1)

except KeyboardInterrupt:
    print('close')
finally:
    GPIO.cleanup()
