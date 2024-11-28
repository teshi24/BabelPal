import time

from naoqi import ALProxy

from pepper_robots import Robot, PepperConfiguration, PepperNames


class Sonar:
    def __init__(self, robot, config):
        self.robot = robot
        self.tts = ALProxy("ALTextToSpeech", config.Ip, config.Port)

    def status(self, status):
        self.tts.post.say("lalala status update")
        print(status)

    def obstacle_detected(self, position):
        self.tts.post.say("ah crap mate theres an obstacle in my way")
        print(position)

    def moving_to_free_zone(self, status):
        self.tts.post.say("im leaving to a free zone, i cant navigate the ural mountains")
        print(status)

    def trajectory_progress(self, progress):
        self.tts.post.say("lalala update on progress")
        print(progress)

    def abs_target_modified(self, newTarget):
        self.tts.post.say("mate i cant go there")
        print(newTarget)

    def motion_detected(self, sensorData):
        self.tts.post.say("theres rats in the walls i can see them moving")
        print(sensorData)

    def run_demo(self):
        data = self.robot.ALMemory.getData('Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value')
        print("Current Front Sonar Raw Value: ")
        print(data)

        data = self.robot.ALMemory.getData('Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value')
        print("Current Back Sonar Raw Value: ")
        print(data)

        # Raised when an obstacle is detected in the close area.
        status_subscriber = self.robot.ALMemory.subscriber("Navigation/AvoidanceNavigator/Status")
        status_subscriber.signal.connect(self.status)

        # Raised when an obstacle is detected in the close area.
        obstacle_detected_subscriber = self.robot.ALMemory.subscriber("Navigation/AvoidanceNavigator/ObstacleDetected")
        obstacle_detected_subscriber.signal.connect(self.obstacle_detected)

        # Raised when the robot starts or stops a motion to leave an obstacle neighbourhood.
        moving_to_free_zone_subscriber = self.robot.ALMemory.subscriber("Navigation/AvoidanceNavigator/MovingToFreeZone")
        moving_to_free_zone_subscriber.signal.connect(self.moving_to_free_zone)

        # Raised when the trajectory progress is updated.
        trajectory_progress_subscriber = self.robot.ALMemory.subscriber("Navigation/AvoidanceNavigator/TrajectoryProgress")
        trajectory_progress_subscriber.signal.connect(self.trajectory_progress)

        # Raised when the required target is unreachable because it is inside an obstacle.
        abs_target_modified_subscriber = self.robot.ALMemory.subscriber("Navigation/AvoidanceNavigator/AbsTargetModified")
        abs_target_modified_subscriber.signal.connect(self.abs_target_modified)

        # Raised when a sensor detects that something is moving around the robot.
        motion_detected_subscriber = self.robot.ALMemory.subscriber("Navigation/MotionDetected")
        motion_detected_subscriber.signal.connect(self.motion_detected)

        self.robot.ALSonar.subscribe("sonar_subscriber", period=100, precision=1)

        time.sleep(2)


if __name__ == '__main__':
    config = PepperConfiguration(PepperNames.Pale)
    robot = Robot(config, reset=True)
    sonar = Sonar(robot, config)
    sonar.run_demo()

