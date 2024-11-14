from pepper_robots import PepperConfiguration, Robot, PepperNames
import time

config = PepperConfiguration(PepperNames.Amber)
pepper = Robot(config)


# Let's define two callbacks. One that should be triggered if a sound is detected and another
# when a sound is localized
def sound_detected_callback(value):
    print("detected sound")


def localized_sound_callback(value):
    print("localized sound")
    print(" - azimut in rad: " + str(value[0][1][0])) # check the ALSoundLocalization docu to understand the "value"


# we need to subscribe to the services and connect the callbacks
pepper.ALSoundDetection.subscribe("sound_detector", period=100, precision=1)
sound_subscriber = pepper.ALMemory.subscriber("SoundDetected")
sound_subscriber.signal.connect(sound_detected_callback)

pepper.ALSoundLocalization.subscribe(name="localizer", period=100, precision=1)
sound_localizer_subscriber = pepper.ALMemory.subscriber("ALSoundLocalization/SoundsLocated")
sound_localizer_subscriber.signal.connect(localized_sound_callback)

# give pepper some time to listen to sounds
pepper.ALTextToSpeech.say("trying to detect sounds")
time.sleep(10)
