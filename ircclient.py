import socket

HOST = "chat.freenode.net"
PORT = 6667

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(b"JOIN :#ldnpydojo")
    data = s.recv(1024)

    print(data)
