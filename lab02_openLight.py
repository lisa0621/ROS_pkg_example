#!/usr/bin/env python
import time
import RPi.GPIO as gpio
import rospy

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)  # button
gpio.setup(18, gpio.OUT)  # led
print('pwm start')
gpio.output(18, gpio.HIGH)
try:
    while True:
        #print('light off')
        #gpio.output(18, gpio.LOW)

        if gpio.input(17) == gpio.LOW:
            time.sleep(0.1)
            gpio.output(18, gpio.HIGH)
        else:
            gpio.output(18, gpio.LOW)
except KeyboardInterrupt:
    print('close')
finally:
    gpio.cleanup()
