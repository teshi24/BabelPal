#!/usr/bin/env python2

import rospy
from pepper_audio.srv import PlayAudioFile
from naoqi import ALProxy
from file_transfer import FileTransfer




class PlayAudioFileServer():

    def __init__(self):
        rospy.init_node('play_audio_file_server')
        service = rospy.Service('pepper/play_audio_file', PlayAudioFile, self.play_callback)
        
        self.robot_ip = rospy.get_param('~robot_ip', '192.168.1.104')
        self.robot_psk = rospy.get_param('~robot_password', 'i4-p2e3p')
        self.robot_port = rospy.get_param('~robot_port', 9559)
        self.robot_username  = rospy.get_param('~robot_username', 'nao')
        try:
            self.file_transfer = FileTransfer(remote_host=self.robot_ip, remote_username=self.robot_username, remote_password=self.robot_psk, remote_path='/home/nao/audio.wav')
        except:
            rospy.logerr("file transfer failed to set up connection with robot")
        
        try:
            self.audio_player = ALProxy('ALAudioPlayer', self.robot_ip, self.robot_port)
        except:
            rospy.logerr("could not establish connection with al audio player")

        rospy.spin()

    def play_callback(self, req):
        rospy.loginfo("received request to play file")
        path = req.path
        try:
            self.file_transfer.transfer_file(local_path=path)
        except:
            rospy.logerr("failed to transfer audio file")
            return False
        try:
            self.audio_player.playFile(self.file_transfer.remote_path)
        except:
            rospy.logerr("failed to play audio file")
            return False
        return True


if __name__ == "__main__":
    PlayAudioFileServer()