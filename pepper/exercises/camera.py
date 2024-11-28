import vision_definitions


class Camera:

    __camera_id = vision_definitions.kTopCamera #which camera
    __resolution = vision_definitions.kVGA  # 640x480px
    __specturm = vision_definitions.kARGBColorSpace
    __picture_format = "jpg"

    def __init__(self, robot):
        self.__al_photo = robot.ALPhotoCapture
        self.configure_camera(self.__camera_id, self.__resolution, self.__picture_format, self.__specturm)

    def configure_camera(self, camera_id, resolution, format, spectrum):
        self.__al_photo.setCameraID(camera_id)
        self.__al_photo.setResolution(resolution)
        self.__al_photo.setPictureFormat(format)
        self.__al_photo.setColorSpace(spectrum)

    def take_picture(self, path, file_name):
        self.__al_photo.takePicture(path, file_name)
