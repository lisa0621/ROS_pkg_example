#!/usr/bin/env python

import rospy
import RPi.GPIO as gpio
from std_msgs.msg import String, Float64, Int32

gpio.setwarnings(False)

# set gpio
LED_PIN = 18

# setmode
gpio.setmode(gpio.BCM)
gpio.setup(LED_PIN, gpio.OUT)
pwm_led = gpio.PWM(LED_PIN, 60)
pwm_led.start(0)

# set output
gpio.output(LED_PIN, gpio.LOW)

tempD = 0


def changelight(data):
    distance = data.data
    print("Distance: %.1f (cm)" % distance)
    #rospy.loginfo(rospy.get_name()+"I heard %s", data.data)

    chgval = 1
    addval = 1
    if tempD > distance:
        chgval = chgval+addval
    else:
        chgval = chgval-addval

    pwm_led.ChangeDutyCycle(chgval)
    print("Distance: %.1f (cm)" % distance)
    print("chgval:" + str(chgval))
    time.sleep(0.02)


if __name__ == '__main__':

    rospy.init_node('subcriber_teleop', anonymous=True)

    while(True):
        if rospy.is_shutdown() == True:
            gpio.cleanup()
            print''
            break
        else:
            rospy.Subscriber("pub_teleop", Float64, changelight)
            rospy.spin()
