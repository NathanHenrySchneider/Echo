# Nathan Schneider
# Martin Nguyen

import socket
import time


global HOST 
HOST = '127.0.0.1'
global PORT
PORT = 12345
global term
term = True
global connecting
connecting = True


def handle_echo(c):
    global term
    message = c.recv(1024).decode('ascii')
    message = message[::-1]
    print("Message received from client")
    c.send(message.encode('ascii'))
    if (message == "dne"):
        term = False
    


def main():
    global term
    global connecting


    # Create socket for client to connect to.
    while connecting:
        print("Connecting to port")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((HOST, PORT))
            connecting = False
        except:
            print("Failed to connect\nTrying again")
            time.sleep(3)


    s.listen(1)
    print("Server is ready for connection...\n")
    while term:
        c, addr = s.accept()
        s.setblocking(1)
        handle_echo(c)
        if (not term):
            break
    s.close()
    print("Server End")


if __name__ == '__main__':
    main()
