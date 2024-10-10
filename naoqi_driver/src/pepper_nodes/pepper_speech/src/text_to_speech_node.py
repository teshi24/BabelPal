#!/usr/bin/env python2

import rospy
from pepper_speech.srv import TextToSpeech
from naoqi import ALProxy


class TextToSpeechServer():

    def __init__(self):
        rospy.init_node('text_to_speech_server')
        service = rospy.Service('pepper_speech/text_to_speech', TextToSpeech, self.say_callback)
        
        IP = rospy.get_param('~pepper_ip', '192.168.1.180')
        PORT = rospy.get_param('~pepper_port', 9559)


        self.tts = ALProxy("ALTextToSpeech", IP, PORT)
        rospy.spin()

    def say_callback(self, req):
        self.tts.say(req.message)
        return True


if __name__ == "__main__":
    TextToSpeechServer()