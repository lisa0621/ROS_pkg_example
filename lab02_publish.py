#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sys, select, termios, tty

msg = """
Control Arduino LED color!
---------------------------
The color ypu can choose: 

R : red
G : green
B : blue  
     
CTRL-C to quit
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

##  start the process  ##
if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
     
    ##  setup the publisher  ##   
    pub = rospy.Publisher('pub_teleop', String, queue_size=10)
    rospy.init_node('publish_teleop', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    try:
        print msg 
        while(1): 
           key = getKey()
           if key == '\x03':
               break
           else:
               select_color = key
               print 'You enter {} '.format(select_color)
               pub.publish(select_color)
           
           #rospy.loginfo(select_color)

    except rospy.ROSInterruptException:
        pass
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
