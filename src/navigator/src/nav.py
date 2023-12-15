#!/usr/bin/env python

import rospy
import tf2_ros
import sys
import actionlib


from geometry_msgs.msg import Twist, Vector3
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


class NavDetector:
	def __init__(self):
		rospy.init_node('nav_detector', anonymous=True)
		self.pose_listener = rospy.Subscriber("user_poses", PoseStamped, self.pose_callback)
		self.pose_stmp = None
		self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
		print("waiting")
		self.client.wait_for_server()
		self.rate = rospy.Rate(10) # added this
		print("server active")

		
		self.process_movement()
		rospy.spin()

	def process_movement(self):
		while not rospy.is_shutdown():
			while self.pose_stmp is None:
				print("No pose")
			# print(self.pose)
			self.movebase_client()
			self.pose_stmp = None
			# self.rate.sleep() # added this afterwards


	def movebase_client(self):
		goal = MoveBaseGoal()
	

		goal.target_pose = self.pose_stmp
		goal.target_pose.pose.orientation.w = 1.0
		print(goal)

		wait = None

		self.client.send_goal(goal)
		wait = self.client.wait_for_result()
		if not wait:
			print("Action server not available!")
		else:
			print("Goal execution done!")
			return


	def pose_callback(self, msg):
		self.pose_stmp = msg


if __name__ == '__main__':
  NavDetector()