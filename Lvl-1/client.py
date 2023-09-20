import socket


port = 5050
host = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

client.send('hi there'.encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
