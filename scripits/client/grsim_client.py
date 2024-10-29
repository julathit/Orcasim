import sys
import os

sys.path.append(os.path.dirname(os.path.abspath("client/sendClient")))


import socket
import time
import sendClient.grSim_Commands_pb2 as commands  # Adjust this import to your file structure
import sendClient.grSim_Packet_pb2 as packet      # Adjust this import to your file structure

class Connection:
    def __init__(self, ip="127.0.0.1", port=20011):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
        self.time_stamp = 0
        self.wheel1 = 0.0
        self.wheel2 = 0.0
        self.wheel3 = 0.0
        self.wheel4 = 0.0
        self.kickspeed_x = 0.0
        self.kickspeed_z = 0.0
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.vel_z = 0.0
        self.id = 0
        self.spinner = False
        self.wheel_speed = False
        self.team_yellow = False

    def set_time(self, time_stamp):
        self.time_stamp = time_stamp

    def set_wheel1(self, wheel1):
        self.wheel1 = wheel1

    def set_wheel2(self, wheel2):
        self.wheel2 = wheel2

    def set_wheel3(self, wheel3):
        self.wheel3 = wheel3

    def set_wheel4(self, wheel4):
        self.wheel4 = wheel4

    def set_kickspeed_x(self, kickspeed_x):
        self.kickspeed_x = kickspeed_x

    def set_kickspeed_z(self, kickspeed_z):
        self.kickspeed_z = kickspeed_z

    def set_vel_x(self, vel_x):
        self.vel_x = vel_x

    def set_vel_y(self, vel_y):
        self.vel_y = vel_y

    def set_vel_z(self, vel_z):
        self.vel_z = vel_z

    def set_id(self, id):
        self.id = id

    def set_spinner(self, spinner):
        self.spinner = spinner

    def set_wheel_speed(self, wheel_speed):
        self.wheel_speed = wheel_speed

    def set_team_yellow(self, team_yellow):
        self.team_yellow = team_yellow

    def send(self):
        # Create the robot command
        robot_command = commands.grSim_Robot_Command(
            id=self.id,
            wheel1=self.wheel1,
            wheel2=self.wheel2,
            wheel3=self.wheel3,
            wheel4=self.wheel4,
            kickspeedx=self.kickspeed_x,
            kickspeedz=self.kickspeed_z,
            veltangent=self.vel_x,
            velnormal=self.vel_y,
            velangular=self.vel_z,
            spinner=self.spinner,
            wheelsspeed=self.wheel_speed
        )

        # Create the overall command packet
        command_packet = commands.grSim_Commands(
            timestamp=self.time_stamp,
            isteamyellow=self.team_yellow,
            robot_commands=[robot_command]
        )

        # Create the packet to send
        sim_packet = packet.grSim_Packet(commands=command_packet)

        # Serialize to bytes
        data = sim_packet.SerializeToString()

        # Send the packet
        try:
            self.sock.sendto(data, (self.ip, self.port))
        except Exception as e:
            print(f"Error sending data: {e}")

# Example usage
if __name__ == "__main__":
    conn = Connection()
    conn.set_id(0)  # Set robot ID
    conn.set_time(0)  # Set timestamp
    conn.set_wheel1(0)  # Set wheel speeds
    conn.set_wheel2(0)
    conn.set_wheel3(0)
    conn.set_wheel4(0)
    conn.set_kickspeed_x(0.0)  # Set kick speeds
    conn.set_kickspeed_z(0.0)
    conn.set_vel_x(0)  # Set velocities
    conn.set_vel_y(0.0)
    conn.set_vel_z(10)
    conn.set_team_yellow(False)  # Set team color

    while True:
        conn.send()  # Send commands continuously
