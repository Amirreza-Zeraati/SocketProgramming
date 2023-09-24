import socket


PORT = 5050
TYPE = 'utf-8'
LEN = 1024
disconnect = '!exit'

host = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, PORT))

connected = True
while connected:
    client.send(input('-: ').encode(TYPE))
    msg = client.recv(LEN).decode(TYPE)
    if msg == disconnect:
        connected = False
    else:
        print(msg)
