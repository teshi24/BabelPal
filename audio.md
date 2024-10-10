# Pepper Audio

## Microphone

Pepper has a microphone array in his head. The specification of the hardware can be found [here](http://doc.aldebaran.com/2-5/family/pepper_technical/microphone_pep.html).

The `naoqi_bridge` will create a topic `naoqi_driver/audio` of type [`naoqi_bridge_msgs/AudioBuffer`](https://github.com/ros-naoqi/naoqi_bridge_msgs/blob/master/msg/AudioBuffer.msg). Inside the `int16[] data` array, the raw audio buffer data can be found for the different channels. The `uint16 frequency` is given as a property as well .


## Speaker


The ears of the Pepper robot are its loundspeakers. The specification of the hardware can be found [here](http://doc.aldebaran.com/2-5/family/pepper_technical/loudspeaker_pep.html).



Pepper can play files that are within its filesystem. To play audio files from your environment, I have created a service. 

The service copies the local audio file to the pepper robot and makes pepper play that sound file.
    
- Service: `/pepper/play_audio_file`
- Call with string `path`
- Response with bool `success`

 The following call should make pepper play the *piano2.wav* file:

    rosservice call /pepper/play_audio_file "path: '/root/catkin_ws/src/pepper_nodes/pepper_audio/piano2.wav'"
