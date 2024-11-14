from pepper_robots import Robot, PepperConfiguration, PepperNames
from dialog import Dialog

config = PepperConfiguration(PepperNames.Amber)
robot = Robot(config)
dialog = Dialog(robot)

dialog.say("how are you today")
dialog.say_slowly("i am tired")
dialog.shout("what are you doing here?")

