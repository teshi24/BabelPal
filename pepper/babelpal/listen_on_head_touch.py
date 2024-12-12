# -*- encoding: UTF-8 -*-
import functools

class ListenOnHeadTouch(object):
    """ Listens on HeadTouch - first touch triggers on_listen, second touch on_stop
    """

    def __init__(self, memory_service, toggle_listening_callback, on_listen, on_stop):
        """
        :param memory_service: The memory service to subscribe to touch events.
        :param toggle_listening_callback: Callback to toggle listening state.
        :param on_listen: Callback executed when listening starts.
        :param on_stop: Callback executed when listening stops.
        """
        self.toggle_listening_callback = toggle_listening_callback
        self.on_listen = on_listen
        self.on_stop = on_stop

        self.touch = memory_service.subscriber("TouchChanged")
        self.id = self.__subscribe_to_touch_changed__()

    def __subscribe_to_touch_changed__(self):
        return self.touch.signal.connect(functools.partial(self._on_touched, "TouchChanged"))

    def _on_touched(self, strVarName, value):
        # Disconnect to the event when listening, to avoid repetitions
        self.touch.signal.disconnect(self.id)

        for sensor in value:
            sensor_name = sensor[0]
            state = sensor[1]
            if sensor_name.startswith("Head") and state:
                is_listening = self.toggle_listening_callback()
                if is_listening:
                    self.on_listen()
                    print("listening started")
                else:
                    print("listening stopped")
                    self.on_stop()
                break

        ## Reconnect again to the event
        self.id = self.__subscribe_to_touch_changed__()

if __name__ == "__main__":
    from interpreting_robot import PepperConfiguration, Robot
    config = PepperConfiguration("Pale")
    pepper = Robot(config)

    def custom_on_listen():
        print("Started listening!")

    def custom_on_stop():
        print("Stopped listening!")

    ListenOnHeadTouch(pepper.ALMemory, pepper.toggle_is_listening_thread_save, custom_on_listen, custom_on_stop)
    pepper.app.run()
