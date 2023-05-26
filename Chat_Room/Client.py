import socket

host = 'localhost'
port = 8080

#Establish tcp connection between server and client. (SOCK_DGRAM for udp)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

#Assign bytes to message
message = sock.recv(1024)

while message:
    print("Message:", message.decode())
    message = sock.recv(1024)

sock.close()