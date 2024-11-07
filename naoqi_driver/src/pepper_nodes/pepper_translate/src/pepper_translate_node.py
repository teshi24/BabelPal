#!/usr/bin/env python2

import rospy
from pepper_translate.srv import Translate
from naoqi import ALProxy
from motion import Motion


class TranslationServer():

    def __init__(self):
        rospy.init_node('pepper_translate_server')
        service = rospy.Service('pepper_translate/pepper_translate', Translate, self.say_callback)
        
        IP = rospy.get_param('~pepper_ip', '192.168.1.181')
        PORT = rospy.get_param('~pepper_port', 9559)

        self.tts = ALProxy("ALTextToSpeech", IP, PORT)
        self.motion = Motion()
        rospy.spin()

    def say_callback(self, req):
        self.motion.nod()
        self.tts.say(req.message)

        rospy.loginfo("finsihed!")
        return True


if __name__ == "__main__":
    TranslationServer()
