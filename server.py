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
global inUse
inUse = False


def handle_echo(c):
    global inUse
    inUse = True
    global term
    message = c.recv(1024).decode('ascii')
    message = message[::-1]
    print("Message received from client")
    c.send(message.encode('ascii'))
    if (message == "dne"):
        term = False
    c.close()
    inUse = False
    



def main():
    global term
    term = True
    # Create socket for client to connect to.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.listen(5)
    print("Server is ready for connection...\n")
    
    while term:
        c, addr = s.accept()
        s.setblocking(1)
        handle_echo(c)
        if (not term):
            break
    s.close()
    print("server end")


if __name__ == '__main__':
    main()
