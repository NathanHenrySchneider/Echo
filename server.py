import socket
import time
from _thread import *
import threading

from black import NewLine

global HOST 
HOST = '127.0.0.1'
global PORT
PORT = 12345
global newLine
newLine = "\n"
global term
term = True


def handle_echo(c):
    global term
    message = c.recv(1024).decode('ascii')
    message = message[::-1]
    print("handl: " + message)
    c.send(message.encode('ascii'))
    # c.send(newLine.encode('ascii'))
    # term = (message != "dne")
    # print("Term: " + str(term))
    if (message == "dne"):
        term = False
        c.close()
    



def main():
    global term
    term = True
    # Create socket for client to connect to.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.listen(5)
    print("Server is ready for connection...\n")
    
    while term:

        # Establish connection with client.
        c, addr = s.accept()
        s.setblocking(1)

        # Start a new thread for each individual client.
        print("Starting new client thread.")
        handle_echo, (c,)
    s.close()
    print("server end")


if __name__ == '__main__':
    main()
