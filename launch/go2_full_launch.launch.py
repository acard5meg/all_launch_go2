import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import pdb

# pdb.set_trace()
def generate_launch_description():
    go2_start = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('go2_bringup'), 'launch'),
            '/go2.launch.py'])
        )
    
    gps = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ublox_gps'), 'launch'),
            '/ublox_gps_node_zedf9p-launch.py'])
        )
    imu = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('witmotion_ros'), 'launch'),
            '/wt901.launch.py'])
        )
    cam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('go2_camera'), 'launch'),
            '/camera_feed.launch.py'])
        )
    lidar_odom = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('go2_lidar_odom'), 'launch'),
            '/lidar_odom.launch.py'])
        )


    return LaunchDescription([
        go2_start,
        gps,
        imu,
        cam,
        lidar_odom
    ])


# <!-- go2_bringup go2.launch.py -->
# <!-- ublox_gps ublox_gps_node_zedf9p-launch.py -->
# <!-- witmotion_ros wt901.launch.py -->
# <!-- go2_gps_nav gps_navigation.launch.py -->
# <!-- go2_camera camera_feed.launch.py -->

# <launch>
#     <include file="/home/jetson/ros2_ws/src/go2_robot/go2_bringup/launch/go2.launch.py" />
#     <include file="/home/jetson/ros2_ws/src/ros2-ublox-zedf9p/ublox_gps/launch/ublox_gps_node_zedf9p-launch.py"/>
#     <include file="/home/jetson/ros2_ws/src/witmotion_ros/launch/wt901.launch.py" />
#     <include file="/home/jetson/ros2_ws/src/go2_gps_nav/launch/gps_navigation.launch.py" />
#     <include file="/home/jetson/ros2_ws/src/go2_camera/launch/camera_feed.launch.py" />
# <launch>
