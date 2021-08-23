#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

#remove all unused velocities

#linear velocities
vx = [0.0, 0.0]
vy = [0.0, 0.0]
vz = [0.0, 0.0]

#angular velocities
vr = [0.0, 0.0]
vp = [0.0, 0.0]
vya = [0.0, 0.0]

#amount of all velocities should be the same

pub_rate = 10 #publish rate for velocities Hz

pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1) #if all massages should be send, increase queue size to size of the list. If topic is different, change cmd_vel to this other topic
rospy.init_node('vel_pub', anonymous=True)
rate = rospy.Rate(pub_rate)

#code is written to publush all the velocities with certain rate once and stop
for i in range(len(vx)):
    if not rospy.is_shutdown():
        msg = Twist() #init Twist msg with all velocities as zero

        #remove any velocity, which is not used in the code
        msg.linear.x = vx[i]
        msg.linear.y = vy[i]
        msg.linear.z = vz[i]

        msg.angular.x = vx[i]
        msg.angular.y = vy[i]
        msg.angular.z = vz[i]
        pub.publish(msg)
        print('Vel Sent') #just for debugging
        rate.sleep()