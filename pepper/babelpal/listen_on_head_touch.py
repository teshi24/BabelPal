# -*- encoding: UTF-8 -*-
import functools

class ListenOnHeadTouch(object):
    """ Listens on HeadTouch - first touch triggers on_listen, second touch on_stop
    """
    def __init__(self, robot, on_listen, on_stop):
        super(ListenOnHeadTouch, self).__init__()
        self.on_listen = on_listen
        self.on_stop = on_stop
        self.robot = robot

        self.memory_service = robot.ALMemory
        self.touch = self.memory_service.subscriber("TouchChanged")
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def onTouched(self, strVarName, value):
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.id)

        for sensor in value:
            sensor_name = sensor[0]
            state = sensor[1]
            if sensor_name.startswith("Head"):
                print(sensor_name)
                if state:
                    print(state)
                    robot_is_listening = self.robot.toggle_is_listening_thread_save()
                    if robot_is_listening:
                        self.on_listen()
                        print("listening started")
                    else:
                        self.on_stop()
                        print("listening stopped")
                break

        ## Reconnect again to the event
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

if __name__ == "__main__":
    from interpreting_robot import PepperConfiguration, Robot
    config = PepperConfiguration("Pale")
    pepper = Robot(config)

    def custom_on_listen():
        print("Started listening!")

    def custom_on_stop():
        print("Stopped listening!")

    ListenOnHeadTouch(pepper, custom_on_listen, custom_on_stop)
    pepper.app.run()
