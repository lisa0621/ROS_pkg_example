#!/usr/bin/env python
import rospy
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
pwm_led=gpio.PWM(18,60)
pwm_led.start(0)
print('pwm start')

    pwm_led.ChangeDutyCycle(50)
    pwm_led.ChangeFrequncy(1)
    time.sleep(0.5)
    pwm_led.ChangeFrequncy(1*2)
    time.sleep(1.5)
    pwm_led.ChangeFrequncy(1)
    time.sleep(0.5)
pwm_led.stop()
gpio.cleanup()