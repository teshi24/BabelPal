from interpreting_robot import PepperConfiguration, Robot

config = PepperConfiguration("Amber")
pepper = Robot(config)
pepper.start_interpreting()
pepper.app.run()