import socket


PORT = 5050
TYPE = 'utf-8'
HEADER = 64
disconnect = '!exit'
host = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, PORT))


def send(message):
    message = message.encode(TYPE)
    message_length = len(message)
    send_length = str(message_length).encode(TYPE)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


while True:
    msg = input('-: ')
    send(msg)
    if msg == disconnect:
        break
