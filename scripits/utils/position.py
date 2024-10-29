import sys
import os

script_dir = os.path.abspath(os.path.expanduser("~/GIT/OrcasimV2/scripits"))
sys.path.append(script_dir)

from client import sslclient
import math

client = sslclient.SSLClient()
client.connect()

p_ball = (0,0)

def ballPos() -> list:

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

robot_dict = {i:robot(i) for i in range(10)}

def angToBall(robotIndex: int):
    robot_dict[robotIndex].get_x
    robot_dict[robotIndex].get_y
    robot_dict[robotIndex].get_Or
    return math.atan2(ballPos()[1] - robot_dict[robotIndex].get_y(),ballPos()[0] - robot_dict[robotIndex].get_x())

def distanceToBall(robotIndex: int):
    robot_dict[robotIndex].get_x
    robot_dict[robotIndex].get_y
    robot_dict[robotIndex].get_Or
    return math.sqrt((ballPos()[1] - robot_dict[robotIndex].get_y())**2 + (ballPos()[0] - robot_dict[robotIndex].get_x())**2) 

def angToPoint(robotIndex: int, point: tuple):
    robot_dict[robotIndex].get_x
    robot_dict[robotIndex].get_y
    robot_dict[robotIndex].get_Or
    return math.atan2(point[1] - robot_dict[robotIndex].get_y(),point[0] - robot_dict[robotIndex].get_x())

def distanceToPoint(robotIndex: int, point: tuple):
    robot_dict[robotIndex].get_x
    robot_dict[robotIndex].get_y
    robot_dict[robotIndex].get_Or
    return math.sqrt((point[1] - robot_dict[robotIndex].get_y())**2 + (point[0] - robot_dict[robotIndex].get_x())**2) 

if __name__ == "__main__":
    while True :
        print(distanceToPoint(0,(0,0)))