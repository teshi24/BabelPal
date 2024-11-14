from pepper_robots import PepperConfiguration, Robot, PepperNames
import time


class SpeechRecognition(object):

    def __init__(self, robot, vocabulary, callback):

        memory = robot.session.service("ALMemory")
        self.subscriber = memory.subscriber("WordRecognized")
        self.subscriber.signal.connect(callback)
        self.__speech_recognition = robot.session.service("ALSpeechRecognition")
        self.__speech_recognition.pause(True)  # need to pause speech recognition to set parameters
        self.__speech_recognition.setLanguage("English")
        self.__speech_recognition.setVocabulary(vocabulary, False)
        self.__speech_recognition.pause(False)
        self.__speech_recognition.subscribe("SpeechDetection")
        print('Speech recognition engine started')

    def unsubscribe(self):
        self.__speech_recognition.unsubscribe("SpeechDetection")
        print('Speech recognition engine stopped')


if __name__ == "__main__":
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)

    vocabulary = ["let's start", "stop"]


    def speech_callback(value):
        print("recognized the following word:" + value[0] + " with accuracy: " + str(value[1]))
        if value[0] == "let's start":
            if value[1] > 0.35:
                print "received start signal"
        if value[0] == "stop":
            if value[1] > 0.35:
                print "received stop signal"

    speech_recognition = SpeechRecognition(robot, vocabulary, speech_callback)
    print("say a word from the vocabulary:")
    print(vocabulary)
    time.sleep(10)
    speech_recognition.unsubscribe()
    print("stop listening")





