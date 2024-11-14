from pepper_robots import PepperConfiguration, Robot, PepperNames
import time


class Dialog:

    def __init__(self, robot):
        self.__my_id = 123
        self.__al_dialog = robot.session.service("ALDialog")
        self.__al_tts = robot.ALTextToSpeech
        self.__al_dialog.setLanguage("English")
        self.__al_audio = robot.ALAudioDevice
        self.__al_dialog.openSession(self.__my_id)

    def add_simple_reaction(self, topic_name, user_input, robot_output):
        # see here how to define your own topic:
        # http://doc.aldebaran.com/2-5/naoqi/interaction/dialog/dialog-syntax_full.html
        topic_content = ('topic: ~' + topic_name + '()\n'
                         'language: enu\n'
                         'u:(' + user_input + ') ' + robot_output + '\n')
        self.__al_dialog.loadTopicContent(topic_content)

    def load_yes_no_question(self, topic_name, question, reaction_yes, reaction_no):
        topic_content = ('topic: ~' + topic_name + '()\n'
                         'language: enu\n'
                         'proposal: ' + question + '\n'
                         '   u1: (no) ' + reaction_no + ' $agree=0\n'
                         '   u1: (yes) ' + reaction_yes + ' $agree=1\n'
                         )
        self.__al_dialog.loadTopicContent(topic_content)

    def ask_yes_no_question(self, topic):
        self.__al_dialog.activateTopic(topic)
        self.__al_dialog.subscribe('myself')
        self.__al_dialog.setFocus(topic)  # focus on this topic (important for proposals)
        self.__al_dialog.forceOutput()  # start proposal sentence
        time.sleep(5)
        do_agree = self.__al_dialog.getUserData("agree", self.__my_id)
        self.__al_dialog.deactivateTopic(topic)
        return do_agree

    def start_topic(self, topic_name):
        self.__al_dialog.activateTopic(topic_name)
        self.__al_dialog.setFocus(topic_name)

    def stop_topic(self, topic_name):
        self.__al_dialog.deactivateTopic(topic_name)
        self.__al_dialog.unloadTopic(topic_name)

    def close_session(self):
        self.__al_dialog.closeSession()


config = PepperConfiguration(PepperNames.Amber)
pepper = Robot(config, reset=True)
dialog = Dialog(pepper)

# ask a yes or no question
topic_name = "topic_yes_no"
dialog.load_yes_no_question(topic_name, "hello human, are you ready to play a game", "great, let's start the game", "what a pity")
print "user's choice:  " + dialog.ask_yes_no_question(topic_name)
dialog.stop_topic(topic_name)

# simple interaction
# if you say hello, pepper will respond with "hello human, pleased to meet you"
topic_name = "introduction"
dialog.add_simple_reaction(topic_name, "hello", "hello human, pleased to meet you")
dialog.start_topic(topic_name)
print "time to interact with pepper: say hello"
time.sleep(10)
dialog.stop_topic(topic_name)


dialog.close_session()
