#!/usr/bin/python
import rospy
import sys
# print sys.path
sys.path.append("/opt/lang-evo/src/lang_evo/src/lang_evo")
from agent import Agent
if len(sys.argv) == 1:
    print("No name and sensor information for agent given. assigning name \"ag1\"")
    name = "ag1"
    sensors = []
else:
    name = sys.argv[1]
    sensors = sys.argv[1:]
print("running agent {} with sensors for variables {}".format(name, sensors))
#
agent = Agent(name, sensors)

