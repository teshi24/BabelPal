from pepper_robots import PepperConfiguration, Robot, PepperNames
import almath

config = PepperConfiguration(PepperNames.Amber)
pepper = Robot(config)

# move 0.5 m forward: x=0.5, y=0, rotation theta=0
pepper.ALTextToSpeech.say("trying to move forward")
pepper.ALMotion.moveTo(x=0.5, y=0, theta=0)

# move 0.5 m backwards and rotate 180 degree
pepper.ALTextToSpeech.say("trying to move back")
pepper.ALMotion.moveTo(x=-0.5, y=0, theta=180 * almath.TO_RAD)

# Pepper stops to move when it detects an obstacle (sometimes even if there is none...)
# we can subscribe to the event "MoveFailed" to get some information of the cause
# first, we define a callback method
# check the "MoveFailed" event in the NAOqi documentation to see the definition of the "value"


def motion_error_callback(value):
    print("ERROR: stopped motion")
    print(" - cause: " + value[0])
    if value[1] == 0:
        print(" - move not started")
    elif value[1] == 1:
        print(" - move started but stopped")
    if value[2]:
        print(" - obstacle detected at position (x=" + str(value[2][0]) + ", y= " + str(value[2][1]) + " , z=" + str(value[2][2]) + ")")


# subscribe to the event and add the the callback method
subscriber = pepper.ALMemory.subscriber("ALMotion/MoveFailed")
subscriber.signal.connect(motion_error_callback)

# test the following motion when you stand in front of pepper
pepper.ALTextToSpeech.say("trying to move forward")
pepper.ALMotion.moveTo(x=0.5, y=0, theta=0)
pepper.ALTextToSpeech.say("trying to move back")
pepper.ALMotion.moveTo(x=-0.5, y=0, theta=180 * almath.TO_RAD)


