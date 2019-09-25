#!/usr/bin/env python
import rospy
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
pwm_led=gpio.PWM(18,60)
pwm_led.start(0)
print('pwm start')
chgval=1
addval=1
while(True):
    chgval=chgval+addval
    pwm_led.ChangeDutyCycle(chgval)

    time.sleep(0.02)
    if(chgval==1):
        addval=1
    elif(chgval==100):
        addval=-1