#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(dt):
    print ('-------------------------------------------')
    print ('Range data at 0 deg:   {}'.format(dt.ranges[0]))
    print ('Range data at 90 deg:   {}'.format(dt.ranges[90]))
    print ('Range data at 270 deg:  {}'.format(dt.ranges[270]))
    print ('-------------------------------------------')
    thr6 = 0.6
    thr1 = 0.5
    thr2 = 2.3
    thr3 = 0.7
    thr4 = 4.0
    thr5 = 0.7

    right_distance = dt.ranges[90] # Distance to the right
    front_distance = dt.ranges[0] # Distance in front
    left_distance = dt.ranges[270] # Distance to the left


    if front_distance > thr1 : # If there's an obstacle in front
        move.linear.x = 0.2
        move.angular.z = 0.0 # Turn left
    elif front_distance < thr3 and right_distance > thr2: # If there's space in front and a wall to the right
        move.linear.x = 0.0
        move.angular.z = 3
    elif front_distance < thr3 and left_distance > thr2: # If there's space in front and a wall to the right
        move.linear.x = 0.0
        move.angular.z = 0.0
    elif front_distance < thr1: # If there's space in front and a wall to the right
        move.linear.x = 0.0
        move.angular.z = -2.54
    elif front_distance < thr6: # If there's space in front and a wall to the right
        move.linear.x = 0.0
        move.angular.z = -2.47
    elif front_distance < thr5 and left_distance < thr4: # If there's space in front and a wall to the right
        move.linear.x = 0.0
        move.angular.z = 0.0
        rospy.loginfo("Accomplished!")
        rospy.sleep(100000000)

    pub.publish(move)

move = Twist()
rospy.init_node('obstacle_avoidance_node')
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

sub = rospy.Subscriber("/scan", LaserScan, callback)

rospy.spin()
