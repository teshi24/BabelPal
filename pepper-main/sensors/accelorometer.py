from pepper_robots import PepperConfiguration, Robot, PepperNames


class Accelerometer:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        pass


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    accelerometer = Accelerometer(robot)
    accelerometer.run_demo()
