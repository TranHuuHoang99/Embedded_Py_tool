import socket
import time

class Stm32Server:
    def __init__(self, hostname = '127.0.0.1', port = 4444) -> None:
        self.hostname = hostname
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind((self.hostname, self.port))
        self.connection.listen()
        self.data = bytes()

    def connect(self):
        while True:
            clientsocket, address = self.connection.accept()
            print(f"established connection to address {address} successfully !!!")
            while True:
                value = input("command: ")
                if value != "":
                    clientsocket.send(bytes(value, "utf-8"))


if __name__ == "__main__":
    server = Stm32Server()
    server.connect()

