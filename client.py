import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    while True:
        msg = s.recv(4096)
        print(msg.decode("utf-8"))