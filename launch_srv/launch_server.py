#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from launch_srv.srv import Launch
import subprocess
from signal import SIGINT

class LaunchServer(Node):
    def __init__(self):
        super().__init__('launch_server')
        self.srv = self.create_service(Launch, 'launch_service', self.callback)
        self.processes = {}
        self.get_logger().info("Ready to launch.")
    def callback(self, request, response):
        command = ['ros2', 'launch', request.package_name, request.launch_file]
        if request.parameters != "":
            command.extend([request.parameters])
        key = " ".join(command)
        if request.terminate:
            if key in self.processes:
                process = self.processes.pop(key)
                process.send_signal(SIGINT)
                self.get_logger().info(f"Terminating {request.launch_file}...")
                process.wait()
                self.get_logger().info(f"{request.launch_file} terminated successfully.")
                response.success = True
                response.message = f"{request.launch_file} terminated successfully."
                return response
            else:
                self.get_logger().warn("File not launched yet.")
                response.success = False
                response.message = "File not launched yet."
                return response
        else:
            try:
                if key in self.processes:
                    self.get_logger().warn("File already launched. Skipping.")
                    response.success = False
                    response.message = "File already launched. Skipping."
                    return response
                else:
                    self.processes[key] = subprocess.Popen(command)
                    self.get_logger().info(f"Launching file {request.launch_file} from package {request.package_name}.")
                    response.success = True
                    response.message = f"Launching file {request.launch_file} from package {request.package_name}."
                    return response
            except Exception as e:
                self.get_logger().error("Failed to launch: %s", e)
                response.success = False
                response.message = f"Failed to launch: {e}"
                return response

def main(args=None):
    rclpy.init(args=args)
    node = LaunchServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()