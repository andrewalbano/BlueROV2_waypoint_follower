#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import Pose, PoseArray
from classes import waypoint_pose
from tf.transformations import *



global goal
goal = waypoint_pose()

global goal_waypoints
goal_waypoints = []


def goal_callback(msg: Pose):

    # x,y,z = msg.position.x, msg.position.y, msg.position.z

    q = msg.orientation
    roll,pitch,yaw = euler_from_quaternion([q.x,q.y,q.z,q.w],'sxyz')
    rospy.loginfo("Goal location\nGoal position (x,y,z): (" + str(msg.position.x) + "," + str(msg.position.y)+ "," + str(msg.position.z) + ")\nGoal orientation (r,p,y): (" + str(roll) + "," + str(pitch) + "," + str(yaw) + ")")
    
    goal = waypoint_pose(msg.position.x, msg.position.y, msg.position.z, roll,pitch,yaw)

def goal_waypoints_callback(msg: PoseArray):
    # clear the previous list need to adda n erse button in gui
    goal_waypoints = []
    # x,y,z = msg.position.x, msg.position.y, msg.position.z
    for waypoint in msg.poses:

        q = waypoint.orientation
        roll,pitch,yaw = euler_from_quaternion([q.x,q.y,q.z,q.w],'sxyz')
        goal_waypoints.append([waypoint.position.x,waypoint.position.y,waypoint.position.z, roll, pitch, yaw])
    print(goal_waypoints)



if __name__ =='__main__':
    # initialize node
    rospy.init_node("gui_subscriber")
    rospy.loginfo("gui_subscriber node has been started.")

    sub = rospy.Subscriber("add_new_goal", Pose, callback= goal_callback)
    sub2 = rospy.Subscriber("update_waypoint_goal_plot", PoseArray, callback= goal_waypoints_callback)

    rospy.spin()
    