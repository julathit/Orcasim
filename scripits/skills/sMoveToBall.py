from . import S_sKillNode
from utils import position

import math


robot = position.robot_dict
angToBall = position.angToBall
distanceToBall = position.distanceToBall

def execute(robotIndex: int):
    
    headingAngToBall = angToBall(robotIndex) - robot[robotIndex].get_Or()
    
    if headingAngToBall > math.pi:
        headingAngToBall -= 2 * math.pi

    elif headingAngToBall < -math.pi:
        headingAngToBall += 2 * math.pi

        
    if distanceToBall(robotIndex) < 100:
        S_sKillNode.sendCommand(robotIndex,0,0,0,False)
    elif abs(headingAngToBall) < 0.1 :
        S_sKillNode.sendCommand(robotIndex,min(0.25*distanceToBall(robotIndex),20),0,0,False)
    elif abs(headingAngToBall) > 0.1:
        S_sKillNode.sendCommand(robotIndex,0,0,3*headingAngToBall,False)
