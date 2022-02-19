# Nathan Schneider
# Martin Nguyen

import socket



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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    message = input('\nPlease enter your message: ')
    s.send(message.encode('ascii'))
    response = s.recv(1024).decode('ascii')
    print("Echo response: " + response)
    if (response == "dne"):
        term = False


def main ():
    global term

    while (term):
        echo()
    s.close()
    print("Client End")

if __name__ == '__main__':
    main()
