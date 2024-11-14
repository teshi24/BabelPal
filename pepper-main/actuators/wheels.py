from pepper_robots import Robot, PepperConfiguration, PepperNames


class Wheels:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        pass


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    wheels = Wheels(robot)
    wheels.run_demo()

