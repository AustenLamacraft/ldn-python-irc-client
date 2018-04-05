import time
import threading
import socket

HOST = "irc.freenode.net"
PORT = 6667


SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.connect((HOST, PORT))
SOCK.send(b"NICK Team4\r\n")
SOCK.send(b"USER Team4bot 0 * :Team 4 test bot\r\n")
SOCK.send(b"JOIN :#ldnpydojo\r\n")


def recieve():
    while 1:
        recv = SOCK.recv(1024)
        if b"PRIVMSG" in recv and b"NOTICE" not in recv:
            print(recv.decode('ascii'))
        time.sleep(5)


if __name__ == '__main__':
    threading.Thread(target=recieve).start()
    while 1:
        message = input("> ")
        to_send = message.encode('ascii')
        SOCK.send(b"PRIVMSG #ldnpydojo :" + to_send + b"\r\n")
        time.sleep(2)
