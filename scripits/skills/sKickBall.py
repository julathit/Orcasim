from . import S_sKillNode
from utils import position

import math




def execute(robotIndex: int):
    
    S_sKillNode.sendCommand(robotIndex,0,0,0,True)
