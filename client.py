import socket
import time
from _thread import *
import threading

global HOST 
HOST = '127.0.0.1'
global PORT
PORT = 12345
global term
term = True
global s


def echo():
    global term
    global s
    message = input('\nPlease enter your message: ')
    s.send(message.encode('ascii'))
    response = s.recv(1024).decode('ascii')
    print("Echo response: " + response)
    if (response == "dne"):
        term = False

def main ():
    global term
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    while (term):
        echo()

    # message = input('\nPlease enter your message: ')
    # s.send(message.encode('ascii'))
    # response = s.recv(1024).decode('ascii')
    s.close()
    # while True and term:
    #     print("loop")
    #     message = input('\nPlease enter your message: ')
    #     s.send(message.encode('ascii'))
    #     response = s.recv(1024).decode('ascii')
    #     print("Response: " + response)
    #     term = (response != "dne")
    # s.close()
    # print("Client end")

if __name__ == '__main__':
    main()
