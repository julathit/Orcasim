import socket
from reciveClient import  ssl_vision_geometry_pb2,ssl_vision_wrapper_pb2,ssl_vision_detection_pb2 # Import the wrapper packet

SSL_WrapperPacket = ssl_vision_wrapper_pb2.SSL_WrapperPacket

class SSLClient:
    
    def __init__(self, vision_ip, vision_port):
        self.vision_ip = vision_ip
        self.vision_port = vision_port
        self.sock = None

    def connect(self):
        # Create a UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.vision_ip, self.vision_port))  # Bind to the specified IP and port
        
        # Join the multicast group
        multicast_group = socket.inet_aton('224.5.23.2')  # Replace with your actual multicast address
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, multicast_group + socket.inet_aton(self.vision_ip))
        
        self.sock.settimeout(5)  # Set a timeout for receiving data

    def receive(self):
        try:
            data, _ = self.sock.recvfrom(8192)  # Buffer size
            wrapper_packet = SSL_WrapperPacket()  # Create an instance of SSL_WrapperPacket
            wrapper_packet.ParseFromString(data)  # Parse the incoming data

            # Check if the detection field is set
            if wrapper_packet.HasField('detection'):
                detection_frame = wrapper_packet.detection

                # Process the received detection frame
                print(f"Frame Number: {detection_frame.frame_number}")
                print(f"Capture Time: {detection_frame.t_capture}")
                print(f"Sent Time: {detection_frame.t_sent}")
                print(f"Camera ID: {detection_frame.camera_id}")

                # Loop through detected balls
                for ball in detection_frame.balls:
                    print(f"Ball - Confidence: {ball.confidence}, X: {ball.x}, Y: {ball.y}, Pixel X: {ball.pixel_x}, Pixel Y: {ball.pixel_y}")

                # Loop through yellow robots
                for robot in detection_frame.robots_yellow:
                    print(f"Yellow Robot - ID: {robot.robot_id}, Confidence: {robot.confidence}, X: {robot.x}, Y: {robot.y}, Orientation: {robot.orientation}")

                # Loop through blue robots
                for robot in detection_frame.robots_blue:
                    print(f"Blue Robot - ID: {robot.robot_id}, Confidence: {robot.confidence}, X: {robot.x}, Y: {robot.y}, Orientation: {robot.orientation}")
            else:
                print("No detection data available in the received packet.")

        except socket.timeout:
            print("No data received within the timeout period.")
        except Exception as e:
            print(f"Error while receiving data: {e}")

    def close(self):
        if self.sock:
            self.sock.close()  # Close the socket

if __name__ == "__main__":
    vision_ip = '0.0.0.0'  # Bind to all interfaces or specify your interface IP
    vision_port = 10020  # The port for the vision server
    
    client = SSLClient(vision_ip=vision_ip, vision_port=vision_port)
    client.connect()  # Connect to the vision server
    try:
        while True:
            client.receive()  # Continuously receive data
    except KeyboardInterrupt:
        print("Stopping client.")
    finally:
        client.close()  # Ensure the socket is closed on exit
