#!/usr/bin/env python
import RPi.GPIO as gpio
import rospy
import time
from std_msgs.msg import String
import sys, select, termios, tty

gpio.setmode(gpio.BCM)
TRIGGER_PIN = 27
ECHO_PIN    = 22
gpio.setup(TRIGGER_PIN,  gpio.OUT)
gpio.setup(ECHO_PIN,     gpio.IN)
gpio.output(TRIGGER_PIN, gpio.LOW)
v = 343		# (331 + 0.6*20)

def measure() :
    gpio.output(TRIGGER_PIN, gpio.HIGH)
    time.sleep(0.00001)	# 10uS 
    gpio.output(TRIGGER_PIN, gpio.LOW)
    pulse_start = None
    pulse_end   = None

    while gpio.input(ECHO_PIN) == gpio.LOW:
        pulse_start = time.time()

    while gpio.input(ECHO_PIN) == gpio.HIGH:
        pulse_end = time.time()

    t = pulse_end - pulse_start

    d = t * v
    d = d/2

    return d*100

##  start the process  ##
if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
     
    ##  setup the publisher  ##   
    pub = rospy.Publisher('pub_teleop', String, queue_size=10)
    rospy.init_node('publish_teleop', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    try :
        while True:
            distance = measure()
            print("Distance: %.1f (cm)" % distance)            
            pub.publish(distance)
            time.sleep(0.5)
           #rospy.loginfo(select_color)

    except rospy.ROSInterruptException:
        pass
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
