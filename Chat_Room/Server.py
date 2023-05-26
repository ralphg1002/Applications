import socket
from threading import Thread

host = 'localhost'
port = 8080

clients = {}
addresses = {}

#Establish tcp connection between server and client. (SOCK_DGRAM for udp)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

def handleClients(conn, address):
    name = conn.recv(1024).decode() #1024 bytes for message
    welcome = "Welcome "+ name + ". Type #quit to leave the Chat Room"
    conn.send(bytes(welcome, "utf8")) #*Bytes -> alternative way to encode a message

    msg = name + " has joined the Chat Room"
    broadcast(bytes(msg, "utf8"))

    #Store connected client in dictionary
    clients[conn] = name

    #When the chat room is active:
    while True:
        msg = conn.recv(1024)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name + ":")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " has left the Chat Room", "utf8"))


#Handle client connections
def acceptClientConn():
    while True:
        clientConnection, clientAddress = sock.accept()
        print(clientAddress," Has Conencted")
        clientConnection.send("Welcome to the Chat Room. Please enter your name to continue.".encode('utf8')) #See alternative way above*

        #Store connected address in dictionary
        addresses[clientConnection] = clientAddress

        Thread(target = handleClients, args = (clientConnection, clientAddress)).start()

def broadcast(msg, prefix = ""):
    for client in clients:
        client.send(bytes(prefix, "utf8") + msg)

if __name__ == "__main__":
    sock.listen(5)
    print("The server is running and is listening to client requests")

    #Accept multiple client requests at the same time with threads
    t1 = Thread(target = acceptClientConn)
    t1.start()
    t1.join()