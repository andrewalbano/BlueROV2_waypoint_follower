#!/usr/bin/env python3
import rospy

if __name__ =='__main__':
    # initialize node
    rospy.init_node("test_node")
    rospy.loginfo("Test node has been started.")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()


    # # basically print lines opf different types
    # rospy.loginfo("Hello from test node")
    # rospy.logwarn("this is a warning")
    # rospy.logerr("This is a log error")


    # rospy.sleep(1.0)
    # rospy.loginfo("End of program")


