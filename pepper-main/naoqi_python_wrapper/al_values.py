import ctypes

class FaceDetected:
    def __init__(self, value):
        self.time_stamp = TimeStamp(value[0])  # this field is the time stamp of the image that was used to perform the detection.
        self.face_info = FaceInfo(value[1][0])
        self.time_filtered_reco_info = value[1][1]
        self.camera_pose_in_torso_frame = value[2]
        self.camera_pose_in_robot_frame = value[3]
        self.camera_id = value[4]


class TimeStamp:
    def __init__(self, value):
        self.seconds = value[0]
        self.microseconds = value[1]


class FaceInfo:
    def __init__(self, value):
        self.shape_info = value[0]
        self.extra_info = ExtraInfo(value[1])


class ShapeInfo:
    def __init__(self, value):
        self.alpha = value[1] # alpha and beta represent the face location in terms of camera angles
        self.beta = value[2]
        self.size_x = value[3] #  sizeX and sizeY are the face size in camera angle
        self.size_y = value[4]


class ExtraInfo:
    def __init__(self, value):
        self.face_id = value[0]  #  represents the ID number for the face
        self.score_reco = value[1]  # the score returned by the recognition process (the higher, the better)
        self.face_label = value[2]  # the name of the recognized face if the face has been recognized
        self.left_eye_points = value[3]  # leftEyePoints and rightEyePoints provide interesting points positions for the eyes (given in camera angles)
        self.right_eye_points = value[4]
        self.nose_points = value[7]   #  provides interesting points positions for the nose (given in camera angles)
        self.mouth_points = value[8]   # provides interesting points positions for the mouth (given in camera angles)