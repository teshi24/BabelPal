import time

from naoqi import ALProxy
from pepper_robots import Robot, PepperConfiguration, PepperNames


class Laser:
    def __init__(self, robot, config):
        self.robot = robot
        self.tts = ALProxy("ALTextToSpeech", config.Ip, config.Port)

    def run_demo(self):
        print("Raw infra-red Data: ")

        data = self.robot.ALMemory.getData('Device/SubDeviceList/Platform/InfraredSpot/Left/Sensor/Value')
        print(data)

        data = self.robot.ALMemory.getData('Device/SubDeviceList/Platform/InfraredSpot/Right/Sensor/Value')
        print(data)

        time.sleep(2)


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Pale)
    robot = Robot(config)
    laser = Laser(robot, config)
    laser.run_demo()

