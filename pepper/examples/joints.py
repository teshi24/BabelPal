from pepper_robots import PepperConfiguration, Robot, PepperNames
import almath
import time

config = PepperConfiguration(PepperNames.Amber)
pepper = Robot(config, reset=True)


# Get current values for head yaw and head pitch
[yaw, pitch] = pepper.ALMotion.getAngles(['HeadYaw', 'HeadPitch'], useSensors=False)
print("yaw = " + str(yaw) + " rad, pitch = " + str(pitch) + " rad")

# move the head to the right
pepper.ALTextToSpeech.say("moving my head to the right")
pepper.ALMotion.setAngles('HeadYaw', -30 * almath.TO_RAD, fractionMaxSpeed=0.2)
time.sleep(2)
# move it back to center
pepper.ALMotion.setAngles('HeadYaw', 0, fractionMaxSpeed=0.2)
time.sleep(2)

# move it up and down
pepper.ALTextToSpeech.say("moving my head up and down")
pepper.ALMotion.setAngles('HeadPitch', 30 * almath.TO_RAD, fractionMaxSpeed=0.2)
time.sleep(2)
pepper.ALMotion.setAngles('HeadPitch', -30 * almath.TO_RAD, fractionMaxSpeed=0.2)
time.sleep(2)
pepper.ALMotion.setAngles('HeadPitch', 0, fractionMaxSpeed=0.2)
