#!/usr/bin/env python

import rospy
import scipy.io

import tf

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

pub_rate = 25 #publish rate for velocities Hz

x_pos = scipy.io.loadmat('x_elliptical_best0.mat')
y_pos = scipy.io.loadmat('y_elliptical_best0.mat')
rot = scipy.io.loadmat('psi_best0.mat')

rospy.init_node('tf_broadcaster', anonymous=True)
rate = rospy.Rate(pub_rate)

x_pos = x_pos["x_elliptical_best0"][0]
y_pos = y_pos["y_elliptical_best0"][0]
rot = rot["psi_best0"][0]

print(x_pos)
print(y_pos)
print(rot)

#code is written to publush all the velocities with certain rate once and stop

for i in range(len(x_pos)):
    if not rospy.is_shutdown():
        br = tf.TransformBroadcaster()
        br.sendTransform((x_pos[i], 0, y_pos[i]), tf.transformations.quaternion_from_euler(0, 0, rot[i]), rospy.Time.now(), "base_link", "odom")

        rate.sleep()

