import sys
import os

script_dir = os.path.abspath(os.path.expanduser("~/GIT/OrcasimV2/scripits"))
sys.path.append(script_dir)


from client import grsim_client

import time

def deltaTime():
    # Store the previous time as an attribute of the function
    if not hasattr(deltaTime, "previous_time"):
        deltaTime.previous_time = time.time()  # Initialize the first time
    
    # Get the current time
    current_time = time.time()
    
    # Calculate delta time
    delta_time = current_time - deltaTime.previous_time
    
    # Update previous time
    deltaTime.previous_time = current_time
    
    return delta_time*3000


ssl_msg = grsim_client.Connection()


def sendCommand(robotIndex: int, x: float, y: float, z: float, kickPower: bool):
    K = 50
    ssl_msg.set_id(robotIndex)
    ssl_msg.set_vel_x(x*K*deltaTime())
    ssl_msg.set_vel_y(y*K*deltaTime())
    ssl_msg.set_vel_z(z*K*deltaTime())
    ssl_msg.set_kickspeed_x(20*kickPower)
    ssl_msg.send()

if __name__=="__main__":
    while True:
        sendCommand(0,0,20,0,0)