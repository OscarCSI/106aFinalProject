#!/usr/bin/env python3
#The line above tells Linux that this file is a Python script,
#and that the OS should use the Python interpreter in /usr/bin/env
#to run it. Don't forget to use "chmod +x [filename]" to make
#this script executable.

#Import the rospy package. For an import to work, it must be specified
#in both the package manifest AND the Python file in which it is used.
import rospy
import tf2_ros
import sys
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3, PoseStamped

# base_frame, goal_frame = sys.argv[1], sys.argv[2] #camera_link and ar_marker
base_frame, goal_frame = "camera_link", "ar_marker_8"
class ArDetector:
  def __init__(self):
    rospy.init_node('ar_detector', anonymous=True)
    self.distToObstacle = 0.25
    self.laser_distanceToObstacle = 0.25
    self.scan_sub = rospy.Subscriber("/scan", LaserScan, self.scan_callback)
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.pose_pub = rospy.Publisher('user_poses', PoseStamped, queue_size=10)
    self.tfBuffer = tf2_ros.Buffer()
    self.tfListener = tf2_ros.TransformListener(self.tfBuffer)
    self.r = rospy.Rate(10)
    self.control_command = Twist()
    self.laser_distance = 0
    self.K1 = .15
    self.K2 = 1
    self.ar_tag_count = 0
    self.ar_found = False
    self. map_tags= {}
    self.cmd = Twist()
    self.trans = None
    self.error_counter = 0
    self.process_movement()
    rospy.spin()
    

  def process_movement(self):
    while not rospy.is_shutdown():
      try:
        self.trans = self.tfBuffer.lookup_transform(base_frame, goal_frame, rospy.Time())

        dist_offset = abs(self.trans.transform.translation.x - self.distToObstacle)
        laser_offset = abs(self.laser_distance - self.laser_distanceToObstacle)
        offset = 0.1
        offset_plus = 0.13

        if(dist_offset > offset and laser_offset > offset):
          self.control_command.linear.x = 1 * self.K1 * self.trans.transform.translation.x
          self.control_command.angular.z = 0
          self.ar_found = True
          self.error_counter +=1
        else:
          if dist_offset <= offset + offset_plus and self.ar_found and self.error_counter > 15: #.08
            self.ar_tag_count += 1
            self.trans = None
            self.ar_found = False
          self.error_counter = 0

          while True:
            done = self.turn(False, .1, 3)
            if done:
              break
        if self.ar_tag_count >= 3:
          #reset robot and break from loop
          self.control_command.linear.x = 0
          self.control_command.angular.z = 0
          self.reset_robot()
          break
        self.pub.publish(self.control_command)
        

      except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException, ValueError):
        if self.ar_found:
          try:
            self.map_tags[self.ar_tag_count] = self.tfBuffer.lookup_transform("map", "camera_link", rospy.Time())
          except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            a = 'inf'
          self.ar_found = False
        pass
      self.r.sleep()

  def reset_robot(self):
    pub_pose = PoseStamped()
    pub_pose.header.seq = 0
    pub_pose.header.stamp = rospy.Time.now()
    pub_pose.header.frame_id = "map"
    self.pose_pub.publish(pub_pose)

  def pose_talker(self):
    pub_pose = PoseStamped()
    pose.header.seq = count
    pose.header.stamp = rospy.Time.now()
    pose.header.frame_id = "map"
    self.pose_pub.publish(pub_pose)

  def self_navigate(self):
    print("nav")


  def turn(self, clockwise, speed, time):
      # Initilize velocities
      self.control_command.linear.x = 0
      self.control_command.linear.y = 0
      self.control_command.linear.z = 0
      self.control_command.angular.x = 0
      self.control_command.angular.y = 0
      if clockwise:
          self.control_command.angular.z = -speed
      else:
          self.control_command.angular.z = speed

      i = 0
      # loop to publish the velocity estimate, current_distance = velocity * (t1 - t0)
      while (i <= time):

          # Publish the velocity
          self.pub.publish(self.control_command)
          i += 1
          self.r.sleep()
      return True


  def scan_callback(self, msg):
    new_list = [msg.ranges[0],msg.ranges[2],msg.ranges[230]]
    self.laser_distance = min(new_list)

if __name__ == '__main__':
  ArDetector()

