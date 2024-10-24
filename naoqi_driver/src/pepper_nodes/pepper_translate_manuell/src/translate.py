#!/usr/bin/env python2

import rospy
from pepper_translate.srv import Translate
from naoqi import ALProxy


class TranslationServer():

    def __init__(self):
        rospy.init_node('translation_server')
        service = rospy.Service('pepper_translate/translate', Translate, self.say_callback)
        
        IP = rospy.get_param('~pepper_ip', '192.168.1.180')
        PORT = rospy.get_param('~pepper_port', 9559)


        self.tts = ALProxy("ALTextToSpeech", IP, PORT)
        rospy.spin()

    def say_callback(self, req):
        self.tts.say(req.message)
        return True


if __name__ == "__main__":
    TranslationServer()