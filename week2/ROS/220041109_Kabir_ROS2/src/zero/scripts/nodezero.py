#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist

def Publisher():
    rospy.init_node("turtle_controller")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=16)
    rate = rospy.Rate(8)
    command = input("Enter Command: ")
    twist = Twist()

    if command == 'A':
        print("Circle!")
        while not rospy.is_shutdown():
            twist.linear.x = 2.0
            twist.angular.z = 2.0
            pub.publish(twist)
            rate.sleep()
    elif command == 'B':
        print("Square!")
        side_len = 2.0
        while not  rospy.is_shutdown():
            for i in range(4):
                twist.linear.x = side_len
                twist.angular.z = 0.0
                pub.publish(twist)
                rospy.sleep(1)

                twist.linear.x = 0.0
                twist.angular.z = math.pi/2
                pub.publish(twist)
                rospy.sleep(1)
    elif command == 'C':
        print("Spiral!")
        r = 0.1
        while not rospy.is_shutdown():
            twist.linear.x = r
            twist.angular.z = 2.0
            pub.publish(twist)
            r += 0.0625
            rate.sleep()


if __name__=='__main__':
    Publisher()
    