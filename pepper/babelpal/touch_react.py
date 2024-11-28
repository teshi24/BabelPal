# -*- encoding: UTF-8 -*-
import functools

from pepper.babelpal.translation import TranslationFactory
from pepper.pepper_robots import PepperConfiguration, Robot


class ReactToTouch(object):
    """ A simple module able to react
        to touch events.
    """
    def __init__(self, robot):
        super(ReactToTouch, self).__init__()
        self.listing = False

        self.memory_service = robot.ALMemory
        self.tts = robot.ALTextToSpeech
        self.touch = self.memory_service.subscriber("TouchChanged")
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

        self.translator = TranslationFactory.get_translation_service()

    ## todo: use proper version from main somehow
    def onTouched(self, strVarName, value):
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.id)

        for sensor in value:
            sensor_name = sensor[0]
            state = sensor[1]
            if sensor_name.startswith("Head"):
                if state:
                    self.listing = not self.listing
                    if self.listing:
                        self.translator.listen()
                    else:
                        text = self.translator.translate()
                        self.say(text)
                break

        ## Reconnect again to the event
        # todo: check if it works when one sais short sentences, could take to long
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def say(self, sentence):
        self.tts.say(sentence)

if __name__ == "__main__":
    config = PepperConfiguration("Pale")
    pepper = Robot(config)

    ReactToTouch(pepper)
    pepper.app.run()