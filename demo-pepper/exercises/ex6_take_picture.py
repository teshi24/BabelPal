from pepper_robots import Robot, PepperConfiguration
from camera import Camera
from file_transfer import FileTransfer
import vision_definitions
from datetime import datetime

config = PepperConfiguration("Ale")
robot = Robot(config)
camera = Camera(robot)
remote_path = "/home/nao/recordings/cameras/"
locale_path = "\\Mac\\Home\\Downloads\\"

cm_configs = {'TOP': [vision_definitions.kTopCamera, vision_definitions.k16VGA, 'jpg', vision_definitions.kARGBColorSpace],# Top 2D, 2560*1920px
              'BOTTOM': [vision_definitions.kBottomCamera, vision_definitions.k16VGA, 'jpg', vision_definitions.kARGBColorSpace],# Bottom 2D, 2560*1920px
              'DEPTH': [vision_definitions.kDepthCamera, vision_definitions.kQVGA, 'jpg', vision_definitions.kDistanceColorSpace] }# 3D, 320*240px

# take a picture
for cm_entry in cm_configs.keys():
    cm_config = cm_configs[cm_entry]
    camera.configure_camera(cm_config[0], cm_config[1], cm_config[2], cm_config[3])
    filename = cm_entry + "-" + datetime.now().strftime('%H%M%y-%m-%d') + ".jpg"
    camera.take_picture(remote_path, filename)
    # copy file to local path
    ft = FileTransfer(robot)
    ft.get(remote_path + filename, locale_path + filename)
    ft.close()
