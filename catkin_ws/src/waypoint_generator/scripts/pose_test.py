#!/usr/bin/env python3
import rospy
import numpy as np
# from classes import waypoint_pose
from geometry_msgs.msg import Pose
from tf.transformations import *

# from tf.transformations import euler_from_quaternion

roll, pitch ,yaw = 0,0,np.pi/2

q = quaternion_from_euler(roll,pitch,yaw,'sxyz')


if __name__ =='__main__':
    # initialize node
    rospy.init_node("pose_test")
    rospy.loginfo("pose_test node has been started.")

    pub = rospy.Publisher("Pose",Pose, queue_size=10)

    rate = rospy.Rate(2)


    while not rospy.is_shutdown():
        # msg = type
        msg = Pose()
        msg.position.x = 0
        msg.position.y = 0
        msg.position.z = 0
        msg.orientation.x = q[0]
        msg.orientation.y = q[1]
        msg.orientation.z = q[2]
        msg.orientation.w = q[3]
    
        pub.publish(msg)
        rate.sleep()
