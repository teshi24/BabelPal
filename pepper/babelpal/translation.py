import time
import six.moves

from pepper_robots import PepperConfiguration, Robot

if __name__ == "__main__":
    config = PepperConfiguration("Pale")
    pepper = Robot(config)

    tts = pepper.ALAnimatedSpeech
    tts.setBodyLanguageModeFromStr("contextual")

    tts.say("Hello, my name is pepper")

    URL_START = "http://192.168.122.1:8080/start?language=de"
    result = six.moves.urllib.request.urlopen(URL_START)
    print(result.read())
    time.sleep(5)
    URL_STOP = "http://192.168.122.1:8080/stop?language=en"
    result = six.moves.urllib.request.urlopen(URL_STOP)
    text = result.read()
    tts.say(text)