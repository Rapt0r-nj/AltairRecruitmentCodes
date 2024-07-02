#!/usr/bin/env python3
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def Publisher():
    rospy.init_node("streamer")
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=16)
    bridge = CvBridge()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        rospy.logerr("Could not open camera:(")
        return
    
    rate = rospy.Rate(4)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logerr("Could not read frame:(")
            break
        image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        image_pub.publish(image)
        rate.sleep()
    cap.release()


if __name__=='__main__':
    Publisher()
    