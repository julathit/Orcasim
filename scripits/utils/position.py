import sys
import os

script_dir = os.path.abspath(os.path.expanduser("~/GIT/OrcasimV2/scripits"))
sys.path.append(script_dir)

from client import sslclient
import math

client = sslclient.SSLClient()
client.connect()

p_ball = (0,0)

def ballPos():

    global p_ball
    client.receive()
    ball = client.detection_frame.balls

    try:
        p_ball = (ball[0].x,ball[0].y)
        return p_ball
    except:
        return p_ball
    
    
class robot:
    def __init__(self,robot_Id):
        self.robot_Id = robot_Id
        self.x = 0
        self.y = 0
        self.orientation = 0
        self.p_robot = {}
    def get_x(self):
        client.receive()
        robots = client.detection_frame.robots_blue
        try:
            for ro in robots:
                if ro.robot_id == self.robot_Id:
                    self.p_robot = ro
                    break
            self.x = self.p_robot.x
            return self.x
        except:
            return self.x
        
    def get_y(self):
        client.receive()
        robots = client.detection_frame.robots_blue
        try:
            for ro in robots:
                if ro.robot_id == self.robot_Id:
                    self.p_robot = ro
                    break
            self.y = self.p_robot.y
            return self.y
        except:
            return self.y
        
    def get_Or(self):
        client.receive()
        robots = client.detection_frame.robots_blue
        try:
            for ro in robots:
                if ro.robot_id == self.robot_Id:
                    self.p_robot = ro
                    break
            self.orientation = self.p_robot.orientation
            return self.orientation
        except:
            return self.orientation

if __name__ == "__main__":
    robot_0 = robot(0)
    while True :
    #    print(ballPos())
        print(robot_0.get_x(),robot_0.get_y(),robot_0.get_Or())
        # print(blue_botPos(0))