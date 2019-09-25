#!/usr/bin/env python
import time
import RPi.GPIO as gpio
import rospy

BUTTON_PIN = 17

gpio.setmode(gpio.BCM)
gpio.setup(BUTTON_PIN, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(18, gpio.OUT)
pwm_led = gpio.PWM(18, 60)
pwm_led.start(0)
print('pwm start')

try:
    while True:
        if gpio.input(BUTTON_PIN) == gpio.LOW:
            pwm_led.ChangeDutyCycle(100)
            print('botton')
        else:
            pwm_led.ChangeDutyCycle(0)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('close')
finally:
    gpio.cleanup()
