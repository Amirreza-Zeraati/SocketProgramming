import socket


PORT = 5050
TYPE = 'utf-8'
LEN = 1024
disconnect = '!exit'

host = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, PORT))
server.listen()

client, address = server.accept()

connected = True
while connected:
    print(f'[{address[0]}, {address[1]}] is connected')
    msg = client.recv(LEN).decode(TYPE)
    if msg == disconnect:
        connected = False
    else:
        print(msg)
    client.send(input('-: ').encode(TYPE))

server.close()
client.close()
