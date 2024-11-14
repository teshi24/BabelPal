from pepper_robots import PepperConfiguration, Robot, PepperNames
from naoqi_python_wrapper import al_values

import time


if __name__ == "__main__":

    config = PepperConfiguration(PepperNames.Amber)
    pepper = Robot(config, reset=True)

    # use ALMemory to get information about the person pepper detected
    # if we find a person, we analyze the face
    person_ids = pepper.ALMemory.getData("PeoplePerception/PeopleList")
    if len(person_ids) == 0:
        print("Error: no faces detected")
    if len(person_ids) > 1:
        print("Error: multiple faces detected")
    if len(person_ids) == 1:
        pepper.ALFaceCharacteristics.analyzeFaceCharacteristics(person_ids[0])
        time.sleep(0.1)
        age_value = pepper.ALMemory.getData("PeoplePerception/Person/"+str(person_ids[0])+"/AgeProperties")
        expression_value = pepper.ALMemory.getData("PeoplePerception/Person/"+str(person_ids[0])+"/ExpressionProperties")
        if len(age_value) > 0:
            print("estimated age = " + str(age_value[0]))
        if len(expression_value) > 0 :
            print("the following expressions were estimated:")
            print(" - neutral = " + str(expression_value[0]))
            print(" - happy = " + str(expression_value[1]))
            print(" - surprised = " + str(expression_value[2]))
            print(" - angry = " + str(expression_value[3]))

    # Here, we use a callback to get more information about the face that is detected
    # Let's define a callback function that is triggered if a face is recognized
    def face_detected_callback(value):
        print("Face detected")
        # since the "value" is a complicated array of arrays, I've created a FaceDetected class in al_values.py
        face_detected = al_values.FaceDetected(value)
        print("face id = " + str(face_detected.face_info.extra_info.face_id))


    subscriber = pepper.ALMemory.subscriber("FaceDetected")
    subscriber.signal.connect(face_detected_callback)

    pepper.ALFaceDetection.subscribe("test_subscriber", precision=0.8, period=1000)

    time.sleep(10)


