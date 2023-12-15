#!/usr/bin/env python3
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the rospy package. For an import to work, it must be specified
# in both the package manifest AND the Python file in which it is used.
import rospy

# Import the String message type from the /msg directory of the std_msgs package.
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Twist, Point, Quaternion


# Define the method which contains the node's main functionality
def pose_talker():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # std_msgs/String to the topic /chatter_talk
    pub = rospy.Publisher('user_poses', PoseStamped, queue_size=10)
    
    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    r = rospy.Rate(10) # 10hz
    count = 0

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)
        # pub_string = "hello world %s" % (rospy.get_time())
        input_msg = input("Please enter pose and press x, y ,r <Enter>: ")
        input_vals = [float(i) for i in input_msg.split(",")]
        count += 1
        pose = PoseStamped()
        pose.header.seq = count
        pose.header.stamp = rospy.Time.now()
        pose.header.frame_id = "map"
        # print(input_vals)
        pose.pose.position.x = input_vals[0]
        pose.pose.position.y = input_vals[1]
        pose.pose.orientation.z = input_vals[2]
        
        # Publish our string to the 'chatter_talk' topic
        pub.publish(pose)
        # print(pose)
        
        # Use our rate object to sleep until it is time to publish again
        r.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('pose_talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        pose_talker()
    except rospy.ROSInterruptException: pass