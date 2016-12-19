from basic_agent import BasicAgent
import rospy
from std_msgs.msg import String

class Agent(BasicAgent):

    def __init__(self, _name, _sensors=[]):
        BasicAgent.__init__(self, _name)
        self.sensors = _sensors
        self.subscribers = {}

        for s in self.sensors:
            self.subscribers[s] = rospy.Subscriber(self.name, String, self.cb_setvar)

    def cb_setvar(self, msg):
        print("Received" + msg)
        # self.vars
