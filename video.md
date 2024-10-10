# Pepper Video

The pepper robot has two 2D cameras located at its front and its mouth. The technical details can be found [here](http://doc.aldebaran.com/2-5/family/pepper_technical/video_2D_pep.html#d-camera-pepper). Additionally, he has a depth camera in its eyes (see [here](http://doc.aldebaran.com/2-5/family/pepper_technical/video_3D_pep.html) for details).

The naoqi_driver publishes the video streams with the following topics:
- `/naoqi_driver/camera/front/image_raw`
- `/naoqi_driver/camera/bottom/image_raw`
- `/naoqi_driver/camera/depth/image_raw`
- `/naoqi_driver/camera/ir/image_raw`


The type of the message is [sensor_msgs/Image](http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Image.html). The encoding for the images is `bgr8` (color image with blue-green-red color order), except for the depth and ir images, which use the encoding `16UC1` (16-bit grayscale image).

Have a look at the [camera_subscriber.py](naoqi_driver/src/pepper_nodes/pepper_video/src/camera_subscriber.py) file how to use the [CvBridge](http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython) to convert ROS images to CV2 images.
