#!/bin/bash

HOST_IP=$(ifconfig | grep -m 1 -Po '(?<=inet addr:)[0-9\.]+')
export ROS_HOSTNAME=$HOST_IP
echo "ROS_HOSTNAME=$HOST_IP" >> /etc/bash.bashrc
source /opt/catkin-ws/devel/setup.bash
rosrun listener listener.py
