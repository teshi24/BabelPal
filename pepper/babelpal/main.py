from babelpal.listen_on_head_touch import ListenOnHeadTouch
from robot import PepperConfiguration, Robot

config = PepperConfiguration("Pale")
pepper = Robot(config)

ListenOnHeadTouch(pepper, pepper.listen, pepper.translate)
pepper.app.run()
