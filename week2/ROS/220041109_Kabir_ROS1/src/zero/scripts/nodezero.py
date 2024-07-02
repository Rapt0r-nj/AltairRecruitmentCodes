#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def Publisher():
    rospy.init_node("node_pub")
    pub = rospy.Publisher('/text_info', String, queue_size=16)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish("Hello Mars!")
        rate.sleep()

if __name__=='__main__':
    Publisher()
    