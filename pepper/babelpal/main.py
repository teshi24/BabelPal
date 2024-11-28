#from pepper_robots import PepperConfiguration, Robot
from pepper.babelpal.touch_react import ReactToTouch
from pepper.pepper_robots import PepperConfiguration, Robot

config = PepperConfiguration("Pale")
pepper = Robot(config)

ReactToTouch(pepper)
pepper.app.run()
