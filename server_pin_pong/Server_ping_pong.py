import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.1.105', 1673))

server.listen(5)

while True:
    user, addres = server.accept()
    user.send("You are connected".encode())