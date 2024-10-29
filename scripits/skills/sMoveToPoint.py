import S_sKillNode
from utils import position

import math

robot_dict = position.robot_dict
angToPoint = position.angToPoint
distanceToPoint = position.distanceToPoint

def moveSpeed(distance):
    if distance < 1440:
        return 0.6
    else:
        return 20

def execute(robotIndex: int,point: tuple):
    headingAngToBall = angToPoint(robotIndex,point) - robot_dict[robotIndex].get_Or()
    distanceTp = distanceToPoint(robotIndex,point)
    
    if headingAngToBall > math.pi:
        headingAngToBall -= 2 * math.pi

    elif headingAngToBall < -math.pi:
        headingAngToBall += 2 * math.pi

    if distanceTp < 60:
        S_sKillNode.sendCommand(robotIndex,0,0,0,False)
    elif abs(headingAngToBall) < 0.1:
        S_sKillNode.sendCommand(robotIndex,moveSpeed(distanceTp),0,0,False)
    elif abs(headingAngToBall) > 0.1:
        S_sKillNode.sendCommand(robotIndex,0,0,35*headingAngToBall,False)


if __name__=="__main__":
    while True:
        execute(0,(0,0))