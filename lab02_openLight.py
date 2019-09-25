#!/usr/bin/env python
import time
import RPi.GPIO as gpio
import rospy

BUTTON_PIN = 17

gpio.setmode(gpio.BCM)
gpio.setup(BUTTON_PIN, gpio.IN, pull_up_down=gpio.PUD_UP)  # button
gpio.setup(18, gpio.OUT)  # led
print('pwm start')

try:
    while True:
        print('light off')
        gpio.output(18, gpio.LOW)

        if gpio.input(BUTTON_PIN) == gpio.LOW:
            time.sleep(0.1)
            print('light on')
            gpio.output(18, gpio.HIGH)
except KeyboardInterrupt:
    print('close')
finally:
    gpio.cleanup()
