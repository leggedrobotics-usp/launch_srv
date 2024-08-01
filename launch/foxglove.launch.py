from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    foxglove_bridge = Node(
        package="foxglove_bridge",
        executable="foxglove_bridge",
        output="screen"
    )
    launch_server = Node(
        package="launch_srv",
        executable="launch_server.py",
        output="screen"
    )
    return LaunchDescription([foxglove_bridge, launch_server])