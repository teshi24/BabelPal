# Pepper Motion


## Move Joints in ROS
Pepper can move its head, arms, hand and body using its different joints. While it is possible to set the angles of each joint by using the joint angles topic:

    rostopic pub /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed "{header: {seq: 0, stamp: now, frame_id: ''}, joint_names: ['HeadYaw', 'HeadPitch'], joint_angles: [0.5,0.1], speed: 0.1, relative: 0}"


it becomes quickly cumbersome to work with these angles.

## Choregraphe

To create animation of Pepper, I recommend using the Choregraphe software. 


1) Download Choregraphe [here](https://www.aldebaran.com/en/support/pepper-naoqi-2-9/downloads-softwares) choosing the old version 2.5.5.

2) Read the instructions [here](
http://doc.aldebaran.com/2-5/software/choregraphe/mouvement.html) to learn how to use the Timeline Tool to create animations.

3) You can export the animations by right-clicking into the time ruler and selecting *Export motion to clipboard* > *Python* > *Bezier*.

## Using ALAnimatedSpeech

To animate Pepper while he is speaking, you can use the [ALAnimatedSpeech](http://doc.aldebaran.com/2-5/naoqi/audio/alanimatedspeech.html) API:

```python
from naoqi import ALProxy


robot_ip = rospy.get_param('~robot_ip', '192.168.1.104')
robot_port = rospy.get_param('~robot_port', 9559)

animated_speech = ALProxy('ALAnimatedSpeech', robot_ip, robot_port)
animated_speech.say("something")
