# Setup
ssh ubuntu@172.20.10.5
turtlebot

roslaunch turtlebot3_bringup turtlebot3_robot.launch --screen

roslaunch realsense2_camera rs_camera.launch mode:=Manual color_width:=424 \
color_height:=240 depth_width:=424 depth_height:=240 align_depth:=true \
depth_fps:=6 color_fps:=6

# On Master
cd Documents/ros_workspaces/final_project
source devel/setup.bash

run: navigator
python3 src/navigator/src/nav.py

run: pose sender
python3 src/pose_sender/src/pose_sender.py

run: auto_turtle/launch/turtle.launch
roslaunch auto_turtle turtle.launch

run: auto_turtle/src/turtlebot_control.py
rosrun auto_turtle turtlebot_control.py

#Commands
AR_2:
0.7,0.6,1