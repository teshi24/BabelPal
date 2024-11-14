from pepper_robots import Robot, PepperConfiguration
from camera import Camera
from tablet import Tablet
import time
import vision_definitions
from datetime import datetime

config = PepperConfiguration("Ale")
robot = Robot(config)
camera = Camera(robot)
remote_folder_path = "/home/nao/recordings/cameras/"

cm_configs = {'TOP': [vision_definitions.kTopCamera, vision_definitions.k16VGA, 'jpg', vision_definitions.kARGBColorSpace],# Top 2D, 2560*1920px
              'BOTTOM': [vision_definitions.kBottomCamera, vision_definitions.k16VGA, 'jpg', vision_definitions.kARGBColorSpace],# Bottom 2D, 2560*1920px
              'DEPTH': [vision_definitions.kDepthCamera, vision_definitions.kQVGA, 'jpg', vision_definitions.kDepthColorSpace] }# 3D, 320*240px
print("test")
# take a picture
for cm_entry in cm_configs.keys():
    print(cm_entry)
    cm_config = cm_configs[cm_entry]
    #camera.configure_camera(cm_config[0], cm_config[1], cm_config[2], cm_config[3])
    filename = cm_entry + "-" + datetime.now().strftime('%H%M%y-%m-%d') + ".jpg"
    print(filename)
    # take a picture

    camera.take_picture(remote_folder_path, filename)

    tablet = Tablet(robot)

    try:
        tablet.show_image(remote_folder_path, filename)
        time.sleep(5)
        tablet.hide_image()
    except RuntimeError, e:
        print "error in showing image on tablet", e
        tablet.close()
    tablet.close()