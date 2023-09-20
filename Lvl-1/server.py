import socket

PORT = 5050
TYPE = 'utf-8'
host = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(communication_socket)
    print('address : ', address)
    message = communication_socket.recv(1024).decode(TYPE)
    print('message is : ', message)
    communication_socket.send("i've got your message".encode(TYPE))
    communication_socket.close()
