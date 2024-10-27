import sys
import os

script_dir = os.path.abspath(os.path.expanduser("~/GIT/OrcasimV2/scripits"))
sys.path.append(script_dir)


from client import grsim_client

ssl_msg = grsim_client.Connection()

def sendCommand(robotIndex: int, x: float, y: float, z: float, kickPower: bool):
    ssl_msg.set_id(robotIndex)
    ssl_msg.set_vel_x(x)
    ssl_msg.set_vel_y(y)
    ssl_msg.set_vel_z(z)
    ssl_msg.set_kickspeed_x(20*kickPower)
    ssl_msg.send()

if __name__=="__main__":
    while True:
        sendCommand(0,50,0,0,0)