#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

rospy.init_node('move_arm')
pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
joint_dict = {'hip': 0, 'shoulder': 1, 'elbow': 2, 'wrist': 3}

jt = JointTrajectory()
jt.header.frame_id = "base_link"
jt.joint_names = ['hip', 'shoulder', 'elbow', 'wrist', 'l_g_base', 'r_g_base']
points = JointTrajectoryPoint()
jt.points.append(points)
initial_positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
jt.points[0].positions[:] = initial_positions[:]
gripper_extend = True

count = 0
rate = rospy.Rate(1)
while not rospy.is_shutdown():
	if count == 0:
		count = 1
		end_positions = [0.5, 0.3, 0.1, 0.0, 0.0, 0.0]
		jt.points[0].positions[:] = end_positions[:]
	jt.points[0].time_from_start = rospy.Duration(1)
	pub.publish(jt)
	rate.sleep()