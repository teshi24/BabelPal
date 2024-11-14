from pepper_robots import PepperConfiguration, Robot, PepperNames

pepper_name = 'Ale'
config = PepperConfiguration(PepperNames.Amber)
pepper = Robot(config)

tts = pepper.ALTextToSpeech
tts.setLanguage("English")
tts.setVolume(0.3) # between 0 and 1
tts.say("hello")

# tune up the volume
tts.setVolume(0.9)
tts.say("hi")
tts.setVolume(0.3)