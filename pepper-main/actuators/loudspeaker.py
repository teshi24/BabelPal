from pepper_robots import Robot, PepperConfiguration, PepperNames


class Loudspeaker:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        pass


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    speaker = Loudspeaker(robot)
    speaker.run_demo()

