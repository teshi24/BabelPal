#!/usr/bin/env python2

import qi
import argparse
import sys
import math
import time
import random


class Motion():

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="192.168.1.181",
                            help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181'.")
        parser.add_argument("--port", type=int, default=9559,
                            help="Naoqi port number")

        args = parser.parse_args()
        self.ip = args.ip
        self.port = args.port
        self.session = self.connect()
        self.motion_service = self.session.service("ALMotion")

        self.angle_absolute = True
        self.nod_angle_bottom = .2
        self.nod_angle_top = 0.
        self.nod_duration = .5


    def connect(self):
        session = qi.Session()
        try:
            session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)
        return session

    def nod(self):
        # Get the service ALMotion.
        self.motion_service.setStiffnesses("Head", 1.0)

        self.motion_service.setIdlePostureEnabled('Body', False)
        self.motion_service.setIdlePostureEnabled('Head', False)


        time.sleep(random.randint(2, 5))
        # while True:
        names  = "HeadPitch"
        self.motion_service.angleInterpolation(names, self.nod_angle_bottom, self.nod_duration, self.angle_absolute)
        self.motion_service.angleInterpolation(names, self.nod_angle_top, self.nod_duration, self.angle_absolute)
        time.sleep(random.randint(2, 5))


if __name__ == "__main__":
    motion = Motion()
    motion.nod()