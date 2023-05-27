import socket
import tkinter
from tkinter import *
from threading import Thread

#Method for when clients are exchanging messages
def receive():
    while True:
        try:
            #Collect broadcast message (client -> server -> client)
            msg = sock.recv(1024).decode("utf8")
            #Newest message at the end of the message list
            msgList.insert(tkinter.END, msg)
        except:
            #For Error
            print("There is an error receiving the message")

#Method to define what happens when a user sends a message
def send():
    #Store message typed by client
    msg = my_msg.get()
    #Reset message field
    my_msg.set("")
    #Broadcase message to all connected clients
    sock.send(bytes(msg, "utf8"))
    #If client wants to quit
    if msg == "#quit":
        sock.close()
        window.close()

#Method for if a client wants to quit
def onClosing():
    my_msg.set("#quit")
    send()

#Creaty window GUI
window = Tk()
window.title("Chat Room")
window.configure(bg = "green")

#Configure message frame background
messageFrame = Frame(window, height = 100, width = 100, bg = "red")
messageFrame.pack()

my_msg = StringVar()
my_msg.set("")

#Configure message window
scrollBar = Scrollbar(messageFrame)
msgList = Listbox(messageFrame, height = 15, width = 100, bg = "red", yscrollcommand = scrollBar.set)
scrollBar.pack(side = RIGHT, fill = Y)
msgList.pack(side = LEFT, fill = BOTH)
msgList.pack()

#Create chat entry functionality
label = Label(window, text = "Enter the Message", fg = "blue", font = "Aerial", bg = "red")
label.pack()

entryField = Entry(window, textvariable = my_msg, fg = "red", width = 50)
entryField.pack()

sendButton = Button(window, text = "Send", font = "Aerial", fg = "white", command = send)
sendButton.pack()

quitButton = Button(window, text = "Quit", font = "Aerial", fg = "white", command = onClosing)
quitButton.pack()


host = 'localhost'
port = 8080
#Establish tcp connection between server and client. (SOCK_DGRAM for udp)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

#Create Thread
recieveThread = Thread(target = receive)
recieveThread.start()

#Events and Updates of window
mainloop()