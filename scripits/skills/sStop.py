from . import S_sKillNode

def execute(pub,robotIndex):
    S_sKillNode.sendCommand(pub,robotIndex,0,0,0,False)