from pepper_robots import Robot, PepperConfiguration, PepperNames


class Tablet:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        pass


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    tablet = Tablet(robot)
    tablet.run_demo()
