#!/usr/bin/env python
import rospy
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.OUT)
p1=gpio.PWM(18,60)
p1.start(0)
print('pwm start')

while(True):

  p1.ChangeDutyCycle(50)
  p1.ChangeFrequency(1)
  time.sleep(3)
  time.sleep(0.5)
  p1.ChangeDutyCycle(75)
  p1.ChangeFrequency(0.5)
  time.sleep(6)
  p1.ChangeFrequency(1)
  time.sleep(3)