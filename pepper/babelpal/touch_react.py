# -*- encoding: UTF-8 -*-

"""Example: Say `My {Body_part} is touched` when receiving a touch event"""

import qi
import argparse
import functools
import sys

class ReactToTouch(object):
    """ A simple module able to react
        to touch events.
    """
    def __init__(self, app):
        super(ReactToTouch, self).__init__()
        self.listing = False

        # Get the services ALMemory, ALTextToSpeech.
        app.start()
        session = app.session
        self.memory_service = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        # Connect to an Naoqi1 Event.
        self.touch = self.memory_service.subscriber("TouchChanged")
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    ## todo: use proper version from main somehow
    def onTouched(self, strVarName, value):
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.id)

        listening = ""
        for sensor in value:
            sensor_name = sensor[0]
            state = sensor[1]
            if sensor_name.startswith("Head"):
                if state:
                    self.listing = not self.listing
                    listening_string = ''
                    if not self.listing:
                        listening_string = 'not '
                    listening = 'I am ' + listening_string + 'listening.'
                break

        self.say(listening)

        ## Reconnect again to the event
        # todo: check if it works when one sais short sentences, could take to long
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def say(self, sentence):
        self.tts.say(sentence)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.181",
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.1.181'.")
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