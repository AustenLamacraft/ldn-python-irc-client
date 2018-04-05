import socket

HOST = "chat.freenode.net"
PORT = 6667

def send_data(socket, command):
    socket.send(command + '\n')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.send(b"USER Team4\n")
    s.send(b"NICK Team4\n")
    s.send(b"JOIN :#ldnpydojo\n")
    data = s.recv(1024)

    print(data)
