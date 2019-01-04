#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import UInt64

def talker():
    pub = rospy.Publisher('chatter', UInt64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = int(rospy.get_time())
        rospy.loginfo("Sending: %d" % data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
