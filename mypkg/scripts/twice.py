#!/usr/bin/python
import rospy
from std_msgs.msg import Int32

n = 0

def cd(message):
	global n
	n = message.data*7

if __name__ == '__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up', Int32, cd)
	pub = rospy.Publisher('twice', Int32, queue_size=1)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish(n)
		rate.sleep()
