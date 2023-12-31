import socket
import threading

'''
    two (or more)(server and client) devices have to connect to same network
    and this script 'socket.gethostbyname(socket.gethostname())' give you
    the LOCAL ip address
    if you want it to work for the INTERNET, all you have to do is
    find your PUBLIC ip address and use it instead of 'socket.gethostbyname(socket.gethostname())'
'''

PORT = 5050
TYPE = 'utf-8'
HEADER = 64
disconnect = '!exit'
host = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, PORT))


def handling(connection, address):
    print(f'[{address[0]}, {address[1]}] is connected')
    connected = True
    while connected:
        message_len = connection.recv(HEADER).decode(TYPE)
        if message_len:
            message_len = int(message_len)
            message = connection.recv(message_len).decode(TYPE)
            print(f'[{address[0]}, {address[1]}] : {message}')
            if message == disconnect:
                print(f'[{address[0]}, {address[1]}] has been disconnected')
                connected = False
    connection.close()


def start():
    server.listen()
    print('Server is starting ...')
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handling, args=(connection, address))
        thread.start()
        print(f'Active Connections : {threading.active_count() - 1}')


start()
