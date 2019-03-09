#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import Bool
from sensor_msgs.msg import NavSatFix
from picket import Fence

fence=Fence()
fence.add_point((26.5140211, 80.2308319))
fence.add_point((26.5140021, 80.2309535))
fence.add_point((26.514535, 80.230839))
fence.add_point((26.5144763, 26.5144763))
ser=serial.Serial('/dev/ttyACM1', 9600)

def check_fence(data, pub):
    inTheFence=fence.check_point((data.latitude,data.longitude))
    rospy.loginfo(inTheFence)
    pub.publish(inTheFence)
    if(inTheFence):
      ser.write('T')
    else:
      ser.write('F')
    
def subscriber():
    rospy.init_node('geofencer', anonymous=True)
    pub = rospy.Publisher('geostop', Bool, queue_size=10)
    rospy.Subscriber("mavros/global_position/global", NavSatFix , check_fence, (pub) )
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
