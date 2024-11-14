from pepper_robots import Robot, PepperConfiguration, PepperNames

import time
import math
import qi


class ConversationDemo:
    def __init__(self, robot):
        self.robot = robot
        self.robot.ALTextToSpeech.say("Hello there. I'm currently correctly configured and we will start the demo now.")
        self.state = "waiting_for_hello"
        self.asr = robot.ALSpeechRecognition
        self.tts = robot.ALAnimatedSpeech
        self.mem = robot.ALMemory
        # self.audio = robot.ALAudioPlayer
        self.localize = robot.ALSoundLocalization


        self.word_subscriber = self.mem.subscriber("WordRecognized")
        self.word_subscriber.signal.connect(self.on_word_recognized)

        self.localize_subscriber = self.mem.subscriber("ALSoundLocalization/SoundLocated")
        self.localize_subscriber.signal.connect(self.on_localize)

    def on_localize(self, value):
        # print("Sound localized:" + (' '.join(' '.join(l) for l in value)))
        if value[1][2] > 0.7:
            print("Seconds: " + str(value[0][0]))
            print("u Seconds: " + str(value[0][1]))
            print("Azimuth (rad): " + str(value[1][0]) + " (deg): " + str((value[1][0] * 180 / math.pi)))
            print("Elevation (rad): " + str(value[1][1]) + " (deg): " + str((value[1][1] * 180 / math.pi)))
            print("Confidence: " + str(value[1][2]))
            print("Energy: " + str(value[1][3]))
            print("=====================================\n")
            # [ [time(sec), time(usec)],
            #
            #   [azimuth(rad), elevation(rad), confidence, energy],
            #
            #   [Head Position[6D]] in FRAME_TORSO
            #   [Head Position[6D]] in FRAME_ROBOT
            # ]

    def on_word_recognized(self, value):
        word, confidence = value[0], value[1]
        print("Received value from WordRecognized: " + word + ", confidence: " + str(confidence))

        if self.state == "waiting_for_hello" and word == "hello" and confidence > 0.4:
            self.state = "waiting_for_how_are_you"
            self.set_vocabulary(["Perfect", "Not good"])

            hello_message = "^start(animations/Stand/Gestures/Hey_1)"
            hello_message += "Hello, how are you? "
            hello_message += "^wait(animations/Stand/Gestures/Hey_1)"
            self.tts.say(hello_message)
        elif self.state == "waiting_for_how_are_you" and "Perfect" in word and confidence > 0.4:
            self.state = "end"

            self.tts.say("Glad to hear, I'm good too.")

            self.cleanup()
        elif self.state == "waiting_for_how_are_you" and "Not good" in word and confidence > 0.4:
            self.state = "end"

            self.tts.say("I hope you'll get better soon... Let's play some music for you!")
            # doesn't work on windows...?
            # self.audio.playFile("C:/Users/JumpStart/Desktop/hellodarknessmyoldfriend.wav")

            self.cleanup()

    def set_vocabulary(self, words):
        self.asr.pause(True)
        self.asr.setVocabulary(words, False)
        self.asr.pause(False)

    def run_demo(self):
        print("Starting the conversation demo...")
        self.set_vocabulary(["hello"])
        self.asr.subscribe("ConversationDemo", 500, 0.0)

        while self.state != "end":
            time.sleep(1)

    def cleanup(self):
        self.asr.unsubscribe("ConversationDemo")


# connect to a virtual robot
port = 9559  # start Choregraphe, go to Edit > Preferences > Virtual Robot to see port number
config = PepperConfiguration(PepperNames.Simulation, port=port)
config.Ip = "192.168.1.104"
pepper = Robot(config)
# let the robot talk and move in sequence


demo = ConversationDemo(pepper)
demo.run_demo()
