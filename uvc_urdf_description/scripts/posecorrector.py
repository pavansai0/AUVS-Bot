#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

Corrected=Twist()
pub = rospy.Publisher('offset_cmd_vel',Twist,queue_size=1)

def callback(data):
	
				
	Corrected.angular.z = -data.linear.x
	Corrected.linear.x = -data.angular.z
		

	pub.publish(Corrected)	


def posecorrect_vel_publish():
	
	rospy.init_node('posecorrector',anonymous=True)		
	rospy.Subscriber("cmd_vel",Twist,callback)			
	rospy.spin()

		

if __name__ == '__main__':
	try:	
		
		posecorrect_vel_publish()
	except rospy.ROSInterruptException:
		pass
