#!/usr/bin/env python3

import rospy
from launch_srv.srv import Launch, LaunchResponse
import subprocess
from signal import SIGINT

processes = {}

def callback(request):
    global processes
    command = ['roslaunch', request.package_name, request.launch_file]
    if request.parameters != "":
        command.extend([request.parameters])
    key = " ".join(command)
    if request.terminate:
        if key in processes:
            process = processes.pop(key)
            process.send_signal(SIGINT)
            rospy.loginfo(f"Terminating {request.launch_file}...")
            process.wait()
            rospy.loginfo(f"{request.launch_file} terminated successfully.")
            return LaunchResponse(success=True, message=f"{request.launch_file} terminated successfully.")
        else:
            rospy.logwarn(f"File not launched yet.")
            return LaunchResponse(success=False, message="File not launched yet.")
    else:
        try:
            if key in processes:
                rospy.logwarn("File already launched. Skipping.")
                return LaunchResponse(success=False, message="File already launched. Skipping.")
            else:
                processes[key] = subprocess.Popen(command)
                rospy.loginfo(f"Launching file {request.launch_file} from package {request.package_name}.")
                return LaunchResponse(success=True, message=f"Launching file {request.launch_file} from package {request.package_name}.")
        except Exception as e:
            rospy.logerr("Failed to launch: %s", e)
            return LaunchResponse(success=False, message=f"Failed to launch: {e}")

def main():
    rospy.init_node('launch_server')
    srv = rospy.Service('launch_service', Launch, callback)
    rospy.loginfo("Ready to launch.")
    rospy.spin()

if __name__ == '__main__':
    main()