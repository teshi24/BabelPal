#!/usr/bin/env python2

import qi
import argparse
import sys
import functools
import rospy
from naoqi import ALModule

class Sensation(ALModule):

    def __init__(self):
        rospy.init_node('pepper_sensation_server')

        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="192.168.1.181",
                            help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181'.")
        parser.add_argument("--port", type=int, default=9559,
                            help="Naoqi port number")

        args = parser.parse_args()
        self.ip = args.ip
        self.port = args.port
        self.session = self.connect()
        self.memory_service = self.session.service("ALMemory")
        print(self.memory_service.getData("TouchChanged"))

        self.touch = self.memory_service.subscribeToEvent("TouchChanged", "Sensation", "onTouched")
        # self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))
        rospy.spin()


    def connect(self):
        session = qi.Session()
        try:
            session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)
        return session



    def onTouched(self, strVarName, value):
        print(strVarName)
        print(value)
        self.touch.signal.disconnect(self.id)

        touched_bodies = []
        for p in value:
           if p[1]:
              touched_bodies.append(p[0])

        self.say(touched_bodies)

        # Reconnect again to the event
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))


    def say(self, bodies):
        if (bodies == []):
            return

        sentence = "My " + bodies[0]

        for b in bodies[1:]:
            sentence = sentence + " and my " + b

        if (len(bodies) > 1):
            sentence = sentence + " are"
        else:
            sentence = sentence + " is"
        sentence = sentence + " touched."

        self.tts.say(sentence)


if __name__ == "__main__":
    sensation = Sensation()
    sensation.onTouched()



"""
import qi
import argparse
import functools
import sys

class ReactToTouch(object):
    def __init__(self, app):
        super(ReactToTouch, self).__init__()

        # Get the services ALMemory, ALTextToSpeech.
        app.start()
        session = app.session
        self.memory_service = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        # Connect to an Naoqi1 Event.
        print(self.memory_service.getData("TouchChanged"))
#        self.touch = self.memory_service.subscriber("TouchChanged")
 #       self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def onTouched(self, strVarName, value):
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.id)

        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        self.say(touched_bodies)

        # Reconnect again to the event
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def say(self, bodies):
        if (bodies == []):
            return

        sentence = "My " + bodies[0]

        for b in bodies[1:]:
            sentence = sentence + " and my " + b

        if (len(bodies) > 1):
            sentence = sentence + " are"
        else:
            sentence = sentence + " is"
        sentence = sentence + " touched."

        self.tts.say(sentence)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.181",
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["ReactToTouch", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    react_to_touch = ReactToTouch(app)
    app.run()
    """