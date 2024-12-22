#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotMover(Node):
    def __init__(self):
        super().__init__('robot_mover')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        # generate timer
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        twist = Twist()

        # move forward
        if self.counter < 10:
            twist.linear.x = 0.2
            twist.angular.z = 0.0
        # rotation
        elif self.counter < 20:
            twist.linear.x = 0.0
            twist.angular.z = 0.4
        else:
            # reset counter
            self.counter = 0

        self.cmd_vel_pub.publish(twist)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = RobotMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
