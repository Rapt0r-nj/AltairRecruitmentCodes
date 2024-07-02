#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def printer(data):
    rospy.loginfo(data.data)

def Subscriber():
    rospy.init_node("node_sub")
    rospy.Subscriber('/text_info', String, printer)
    rospy.spin()

if __name__=='__main__':
    Subscriber()
    