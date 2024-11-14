from pepper_robots import PepperConfiguration, Robot, PepperNames
import time

config = PepperConfiguration(PepperNames.Amber)
pepper = Robot(config)


# Pepper triggers some events when it detects people
# we can subscribe to these events and define a custom callback method

# Let's define a callback function that is triggered if people are detected
def people_detected_callback(value):
    print("detected people")
    print(value)  # have a look at the definition:
                  # http://doc.aldebaran.com/2-5/naoqi/peopleperception/alpeopleperception-api.html#PeoplePerception/PeopleDetected
                  # you might want to add some classes to the naoqi_python_wrapper/al_values.py


# we need to subscribe to the service and connect the callback
subscriber = pepper.ALMemory.subscriber("PeoplePerception/PeopleDetected")
subscriber.signal.connect(people_detected_callback)

# time to test the people detection
pepper.ALTextToSpeech.say("trying to detect people")
time.sleep(10)