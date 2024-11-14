from pepper_robots import Robot, PepperConfiguration, PepperNames
import qi

# connect to a virtual robot
port = 49717  # start Choregraphe, go to Edit > Preferences > Virtual Robot to see port number
config = PepperConfiguration(PepperNames.Simulation, port=port)
config.Ip = "10.0.2.2"
robot = Robot(config)

# let the robot talk and move in sequence
robot.ALTextToSpeech.say("hello")

# let the robot talk and move in parallel
