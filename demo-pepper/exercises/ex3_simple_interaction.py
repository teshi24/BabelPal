from pepper_robots import Robot, PepperConfiguration, PepperNames
from dialog import Dialog
import time

config = PepperConfiguration(PepperNames.Amber)
robot = Robot(config)
dialog = Dialog(robot)

topic_name = "introduction"
dialog.add_simple_reaction(topic_name, "hello", "hello human, pleased to meet you")
dialog.start_topic(topic_name)
print "time to interact with pepper"
time.sleep(20)
dialog.stop_topic(topic_name)

dialog.close_session()