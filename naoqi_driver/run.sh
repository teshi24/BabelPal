#!/bin/bash

# Initialization of the ROS environment
export PATH=$PATH:$HOME/.local/bin$
export PYTHONPATH=/pynaoqi-python2.7-pynaoqi-python2.7-2.8.7.4-linux64-20210819_141148/lib/python2.7/site-packages:${PYTHONPATH}

source /opt/ros/noetic/setup.bash
source /root/catkin_ws/devel/setup.bash

echo "Starting ROS..."

# Start of the first ROS Launch file and redirect the output to a log file
roslaunch pepper_launch pepper_launch.launch 2>&1 | tee /root/pepper_bringup_log.txt &

# Wait for 10 seconds to ensure the first launch file has started
sleep 10

# Start the second ROS Launch file using environment variables
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=$ROBOT_IP nao_port:=$ROBOT_PORT network_interface:=$NETWORK_INTERFACE 2>&1 | tee /root/naoqi_driver_log.txt &

echo "ROS launches started."

# Loop to keep the container running
while true; do
    sleep 1
done