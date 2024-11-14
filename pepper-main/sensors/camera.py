from pepper_robots import Robot, PepperConfiguration, PepperNames


class Camera:
    def __init__(self, robot):
        self.robot = robot

    def run_demo(self):
        pass


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Amber)
    robot = Robot(config)
    cam = Camera(robot)
    cam.run_demo()
