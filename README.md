# Pepper ROS - NaoQi Bridge
This Docker container is the ROS connection for the Pepper robot.

## Prerequisites
- Virtual Machine or native Ubuntu 22.04
- VS Code with Docker and Remote Dev Extensions
- Docker engine

## Settings
A few settings must be made for the setup to work correctly:

1. In the [docker-compose.yaml](docker-compose.yaml) file, you need to edit the `ROBOT_IP` and `ROBOT_PASSWORD` environment variables:

    | Robot Name | `ROBOT_IP` | `ROBOT_PASSWORD` |
    | --- | --- | --- |
    | Ale |   192.168.1.180 | i4-p2e3p | 
    | Pale |   192.168.1.181 | i3-p2e3p | 


## Start-up

1. Connect to the `robo-duckie` network with password `entenhausen`.
2. In your VM, use the network adapter **bridged** (VM > Settings > Network Adapter).
3. In VS Code, right-click on the docker-compose.yaml file and select `docker compose up`
4. In VS Code, click on the green arrows on the lower left and select  `attach to running container` and chose the right container.
5. The code in `/src/pepper_nodes` is shared with the container.
6. Create your code inside the container within the folder `~/catkin_ws/src/pepper_nodes/`

### How to generate a new package
```shell
cd ~/catkin_ws/src/pepper_nodes
# replace pkg_name with your name; also, not clear whether all dependencies are required for each pkg
catkin_create_pkg pepper_<pkg_name> std_msgs rospy roscpp message_generation
cd pepper_<pkg_name>/src
touch pepper_<pkg_name>_node.py
chmod +x pepper_<pkg_name>_node.py
cd ~/catkin_ws
catkin_make
source devel/setup.bash
# das Pythonfile ist jetzt wie folgt ausführbar:
rosrun pepper_<pkg_name> pepper_<pkg_name>_node.py
```
# todo: automatically register service at startup
# todo: at the end, start service automatically when docker compose up was called
### How to add a new service type to the pkg
```shell
cd ~/catkin_ws/src/pepper_nodes/pepper_<pkg_name>
mkdir srv
touch srv/<ServiceTyp>.srv
```
dann im `CMakeLists.txt` die Funktion wie folgt anpassen:
```
add_service_files(
    FILES
    <ServiceTyp>.srv
)
```
danach via shell neu builden:
```shell
cd ~/catkin_ws
catkin_make
source devel/setup.bash
# testen ob ersichtlich
rossrv show pepper_<pkg_name>/<ServiceTyp>.srv
```

### How to use a service
1. run .py file to start the service if not already listed with `rosrun pepper_<pkg_name> pepper_<pkg_name>_node.py`
2. call it with `rosservice call /pepper_<pkg_name>/pepper_<pkg_name>`


### ROS environment

The docker container uses the [naoqi_bridge](https://github.com/ros-naoqi/naoqi_bridge) and the [pepper_dcm_robot](https://github.com/ros-naoqi/pepper_dcm_robot) packages. Within the container, list the available topics with

    rostopic list

and services

    rosservice list

If your start-up procedure has worked fine, you should see multiple topics, such as

- `naoqi_driver/audio`
- `naoqi_driver/camera/bottom/image_raw`
- etc. 

### Audio and Video

For Audio and Video, have a look at  [audio.md](audio.md) and [video.md](video.md)


### Use of Pepper's APIs

Pepper provides many functionalities with its own SDK [NAOqi](http://doc.aldebaran.com/2-5/naoqi/). To access these functionalities, you need to make the following import in python:

```python
from naoqi import ALProxy
```

To setup the connection with a API, you need the robot ip and the port (9559). Here, we use the [Animated Speech API](http://doc.aldebaran.com/2-5/naoqi/audio/alanimatedspeech-api.html).

```python
tts = ALProxy('ALAnimatedSpeech', robot_ip, robot_port)
```

The proxy provides the method `say()`:

```python
tts.say("hello")
```
<br>
<br>
<br>
<br>
<br>
<br>
-



#### Notes FH

- added rviz
- need to start RVIZ with 
    `sudo QT_X11_NO_MITSHM=1 rviz`
- install pepper meshes manually (need to agree license)
    apt-get install ros-kinetic-pepper-meshes
