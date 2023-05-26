import socket

host = 'localhost'
port = 8080

#Establish tcp connection between server and client. (SOCK_DGRAM for udp)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

#Socket is continously listening to client requests
sock.listen(1)
print("The Server is running and is listening top client requests")
connection, address = sock.accept()

#Once connection is established
message = "Hey there is something important for you"
connection.send(message.encode())

#Close connection
connection.close()