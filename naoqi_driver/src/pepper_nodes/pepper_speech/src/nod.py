#!/usr/bin/env python2

import qi
import argparse
import sys
import math
import time
import random


class Nod():

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="192.168.1.181",
                            help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181'.")
        parser.add_argument("--port", type=int, default=9559,
                            help="Naoqi port number")

        args = parser.parse_args()
        session = qi.Session()
        try:
            session.connect("tcp://" + args.ip + ":" + str(args.port))
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
                "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

        # Get the service ALMotion.
        motion_service = session.service("ALMotion")
        motion_service.setStiffnesses("Head", 1.0)
        motion_service.setIdlePostureEnabled('Body', False)

        while True:
            names  = "HeadPitch"
            isAbsolute = True
            angle_bottom = .15
            angle_top = 0.
            duration_down = .5
            duration_up = .5
            motion_service.angleInterpolation(names, angle_bottom, duration_down, isAbsolute)
            motion_service.angleInterpolation(names, angle_top, duration_up, isAbsolute)
            time.sleep(random.randint(2, 5))


if __name__ == "__main__":
    Nod()