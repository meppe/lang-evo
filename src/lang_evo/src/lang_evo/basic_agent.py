import rospy
from std_msgs.msg import String


class BasicAgent:
    def __init__(self, _name):
        self.name = _name
        self.vars = {}
        rospy.init_node(self.name)


    def run(self):
        rospy.spin()