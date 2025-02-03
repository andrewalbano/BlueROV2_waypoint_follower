#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import Pose
from tf.transformations import *


def add_global_waypoint(current_waypoints=None, new_waypoint=[0,0,0,0,0,0]):
    """
    Adds a new global waypoint to the existing waypoints array.

    Parameters:
        current_waypoints (numpy.ndarray): An array of current waypoints. Defaults to None.
        new_waypoint (Pose): The new waypoint Pose to add. Defaults to a default Pose.
    
    Returns:
        numpy.ndarray: An updated array of waypoints including the new waypoint.
    """
    if current_waypoints is None:
        current_waypoints = new_waypoint
    else:
        current_waypoints.append(new_waypoint)
    return current_waypoints
