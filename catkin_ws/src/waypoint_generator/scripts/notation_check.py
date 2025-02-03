#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import Pose
from tf.transformations import *


# from tf.transformations import euler_from_quaternion
origin = [0,0,0]
x_axis = [1,0,0]
y_axis = [0,1,0]
z_axis = [0,0,1]
roll, pitch ,yaw = 0,0,np.pi/2
# quick test to check notation
Rx = rotation_matrix(roll, x_axis)
Ry = rotation_matrix(pitch, y_axis)
Rz = rotation_matrix(yaw, z_axis)
R = concatenate_matrices(Rz,Ry,Rx)
q = quaternion_from_euler(roll,pitch,yaw,'sxyz')
Rq = quaternion_matrix(q)

euler_from_quaternion(q,'sxyz')

print(is_same_transform(R,Rq))
print(q)

