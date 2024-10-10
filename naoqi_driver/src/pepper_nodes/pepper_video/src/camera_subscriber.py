#!/usr/bin/env python2

import rospy
import cv2 

from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 


class CameraSubscriber:
    
    def __init__(self):
        # initialize a node with a name, annonymous=True ensures that the name is unique
        rospy.init_node('camera_listener', anonymous=True)
        # subscribe to a topic of type Image  
        rospy.Subscriber("/naoqi_driver/camera/front/image_raw", Image, self.callback)
        rospy.sleep(2.0) # needed to make sure the node is indeed initialized
        
        # create a openCV <-> ROS bridge
        self.cv2_bridge = CvBridge()
        self.rate = rospy.Rate(10)  # the node is running at 10 hz
        self.image = None

    def callback(self, data):
        # the callback should be light and fast
        rospy.loginfo("Received camera image with encoding " + data.encoding)
        self.image = data

    def do_image_processing(self):
        if self.image:
            # image processing is done on the latest image received
            cv2img = self.cv2_bridge.imgmsg_to_cv2(self.image, "bgr8")
            # cv2.imwrite("tmp.jpg", cv2img)
            rospy.loginfo("Converted image for OpenCV with " + str(cv2img.size) + " pixels")

        
    def run(self):
        while not rospy.is_shutdown():
            self.do_image_processing()
            self.rate.sleep()


if __name__ == '__main__':
    cs = CameraSubscriber()
    cs.run()
