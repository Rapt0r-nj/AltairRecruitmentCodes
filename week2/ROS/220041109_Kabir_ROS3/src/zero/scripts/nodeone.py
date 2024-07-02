#!/usr/bin/env python3
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def callback(data):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.imshow("Strem", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        rospy.signal_shutdown("quit.")

def Subscriber():
    rospy.init_node("viewer")
    rospy.Subscriber('/camera/image_raw', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__=='__main__':
    Subscriber()