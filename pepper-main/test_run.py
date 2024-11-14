from pepper_robots import PepperConfiguration, Robot, PepperNames

config = PepperConfiguration(PepperNames.Pale)
pepper = Robot(config)

tts = pepper.ALAnimatedSpeech  # text to speech service

tts.say("Hello, my name is pepper")

tts.say("Watch out, i'll try to move")

success = pepper.ALMotion.moveTo(0.5, 0, 0)

if not success:
    tts.say("Ohh, I could not move. Maybe there is an obstacle in front of me. Or my brake is not released")
if success:
    tts.say("Yeah,A I've reached my destination")