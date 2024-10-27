from . import sKillNode
from utils import position

import math


save_ball = position.save_ball
p_ball = position.p_ball
angToBall = position.angToBall
robot = position.robot
distanceToBall = position.distanceToBall

def execute(robotIndex: int):
    
    sKillNode.sendCommand(robotIndex,0,0,0,True)
