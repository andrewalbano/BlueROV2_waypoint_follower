#!/usr/bin/env python3
import rospy
import numpy as np
# from classes import waypoint_pose
from geometry_msgs.msg import Pose
from tf.transformations import *

# from tf.transformations import euler_from_quaternion

roll, pitch ,yaw = 0,0,np.pi/2

q = quaternion_from_euler(roll,pitch,yaw,'sxyz')


def pose_callback(msg: Pose):
    q = msg.orientation
    roll,pitch,yaw = euler_from_quaternion([q.x,q.y,q.z,q.w],'sxyz')
    rospy.loginfo("Position: (" + str(msg.position.x) + "," + str(msg.position.y)+ "," + str(msg.position.z) + ")\nOrientation (r,p,y): (" + str(roll) + "," + str(pitch) + "," + str(yaw) + ")")


if __name__ =='__main__':
    # initialize node
    rospy.init_node("pose_test_subscriber")
    # rospy.loginfo("pose_test_subscriber node has been started.")

    sub = rospy.Subscriber("Pose", Pose, callback= pose_callback)
    
    rospy.loginfo("pose_test_subscriber node has been started.")

    rospy.spin()
    


    # pub = rospy.Publisher("Pose",Pose, queue_size=10)

    # rate = rospy.Rate(2)


    # while not rospy.is_shutdown():
    #     # msg = type
    #     msg = Pose()
    #     msg.position.x = 0
    #     msg.position.y = 0
    #     msg.position.z = 0
    #     msg.orientation.x = q[0]
    #     msg.orientation.y = q[1]
    #     msg.orientation.z = q[2]
    #     msg.orientation.w = q[3]
    
    #     pub.publish(msg)
    #     rate.sleep()
