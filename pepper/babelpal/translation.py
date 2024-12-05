import time
import os
from abc import abstractmethod

import six.moves

from babelpal.env import load_dotenv

load_dotenv('.env')


class TranslationInterface(object):
    @abstractmethod
    def listen(self):
        pass
    @abstractmethod
    def translate(self):
        pass

class TranslationFactory(object):
    @staticmethod
    def get_translation_service():
        if os.getenv("TRANSLATION_SERVICE_AVAILABLE") == "True":
            return Translation()
        else:
            return TranslationMock()


class Translation(TranslationInterface):
    def listen(self):
        URL_START = "http://192.168.122.1:8080/start?language=de"
        result = six.moves.urllib.request.urlopen(URL_START)
        print(result.read())

    def translate(self):
        URL_STOP = "http://192.168.122.1:8080/stop?language=en"
        result = six.moves.urllib.request.urlopen(URL_STOP)
        text = result.read()
        print(text)
        return text


class TranslationMock(TranslationInterface):
    def listen(self):
        print("TranslationMock: listening started!")

    def translate(self):
        return "TranslationMock: I am translating now."

if __name__ == "__main__":
    from robot import PepperConfiguration, Robot

    translator = TranslationFactory.get_translation_service()

    config = PepperConfiguration("Pale")
    pepper = Robot(config)

    tts = pepper.ALAnimatedSpeech
    tts.setBodyLanguageModeFromStr("contextual")

    translator.listen()
    time.sleep(5)
    text = translator.translate()
    tts.say(text)