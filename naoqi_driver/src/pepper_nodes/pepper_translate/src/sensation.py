#!/usr/bin/env python2

import qi
import argparse
import sys
import functools
import rospy
from naoqi import ALModule


# parser = argparse.ArgumentParser()
# parser.add_argument("--ip", type=str, default="192.168.1.181",
#                     help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181.")
# parser.add_argument("--port", type=int, default=9559,
#                     help="Naoqi port number")

# args = parser.parse_args()
# # Initialize qi framework.
# connection_url = "tcp://" + args.ip + ":" + str(args.port)
# pepper = qi.Application(["ReactToTouch", "--qi-url=" + connection_url])

# #pepper = qi.Application()
# pepper.start()
# session = pepper.session
# memory = session.service("ALMemory")

# def touch_event(*args, **kwargs):
#     pass

# # Listen to public addresses on a random port,
# # so that services registered from here are accessible.
# session.listen("tcp://0.0.0.0:0")

# # An object that will be registered as a service.
# class MySubscriber:

#     # It needs at least a callback to get ALMemory events.
#     def onTouched(key, value):
#         pass

# subscriber = MySubscriber()

# # Register it with an arbitrary name.
# service_name = "MySubscriber"
# session.registerService(service_name, subscriber)

# # Subscribe and tell exactly which service and method to call back.
# memory.subscribeToEvent("TouchChanged", service_name, "onTouched")

# # rospy.spin()


# """
# import qi
# import argparse
# import sys
# import functools
# import rospy
# from naoqi import ALModule

# class Sensation(ALModule):

#     def __init__(self, app):

#         app.start()
#         self.session = app.session
#         ALModule.__init__(self, "Sensation")  # Register the module

#         rospy.init_node('pepper_sensation_server')

#         # parser = argparse.ArgumentParser()
#         # parser.add_argument("--ip", type=str, default="192.168.1.181",
#         #                     help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181'.")
#         # parser.add_argument("--port", type=int, default=9559,
#         #                     help="Naoqi port number")

#         # args = parser.parse_args()
#         # self.ip = args.ip
#         # self.port = args.port
#         # self.session = self.connect()

#         self.memory_service = self.session.service("ALMemory")
#         print(self.memory_service.getData("TouchChanged"))

#         self.touch = self.memory_service.subscribeToEvent("TouchChanged", "Sensation", "onTouched")
#         # self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))
#         rospy.spin()


#     def connect(self):
#         session = qi.Session()
#         try:
#             session.connect("tcp://" + self.ip + ":" + str(self.port))
#         except RuntimeError:
#             print ("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
#                 "Please check your script arguments. Run with -h option for help.")
#             sys.exit(1)
#         return session



#     def onTouched(self, strVarName, value):
#         print(strVarName)
#         print(value)

#         touched_bodies = []
#         for p in value:
#            if p[1]:
#               touched_bodies.append(p[0])

#         self.say(touched_bodies)


#     def say(self, bodies):
#         if (bodies == []):
#             return

#         sentence = "My " + bodies[0]

#         for b in bodies[1:]:
#             sentence = sentence + " and my " + b

#         if (len(bodies) > 1):
#             sentence = sentence + " are"
#         else:
#             sentence = sentence + " is"
#         sentence = sentence + " touched."

#         self.tts.say(sentence)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--ip", type=str, default="192.168.1.181",
#                         help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181.")
#     parser.add_argument("--port", type=int, default=9559,
#                         help="Naoqi port number")

#     args = parser.parse_args()
#     try:
#         # Initialize qi framework.
#         connection_url = "tcp://" + args.ip + ":" + str(args.port)
#         app = qi.Application(["SensationApp", "--qi-url=" + connection_url])
#     except RuntimeError:
#         print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
#                "Please check your script arguments. Run with -h option for help.")
#         sys.exit(1)
#     sensation = Sensation(app)
#     app.run() """

""" """
import qi
import argparse
import functools
import sys
import rospy

# An object that will be registered as a service.
class MySubscriber:

    # It needs at least a callback to get ALMemory events.
    def onTouched(key, value):
        rospy.loginfo(value)
        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        self.say(touched_bodies)
        pass

class ReactToTouch(object):
    def __init__(self, app):
        super(ReactToTouch, self).__init__()

        # Get the services ALMemory, ALTextToSpeech.
        app.start()
        session = app.session
        
        memory = naoqi.ALProxy("ALMemory")
        memory.subscribeToEvent("TouchChanged", self.getName(), "onTouched")

        self.memory_service = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        # Connect to an Naoqi1 Event.
        print(self.memory_service.getData("TouchChanged"))
        #self.touch = self.memory_service.subscriber("FaceDetected")
        #self.touch = self.memory_service.subscriber("TouchChanged")
        #self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

        # Listen to public addresses on a random port,
        # so that services registered from here are accessible.
        session.listen("tcp://172.17.0.1:45633/")

        subscriber = self

        # Register it with an arbitrary name.
        service_name = "MySubscriber"
        session.registerService(service_name, subscriber)

        # Subscribe and tell exactly which service and method to call back.
        self.memory_service.subscribeToEvent("/naoqi_driver/head_touch", service_name, "onTouched")


    def onTouched(self, value):
        print(f"called with {value}")
        # # Disconnect to the event when talking,
        # # to avoid repetitions
        # self.touch.signal.disconnect(self.id)

        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        self.say(touched_bodies)

        # # Reconnect again to the event
        # self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

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
    """ """