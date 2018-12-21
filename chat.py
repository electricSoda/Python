#import libraries
import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(1)

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target = self.handler, args = (c, a))
            cThread.daemon = True
            cThread.start()
            connections.append(c)
            print(self.connections)


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address):
        self.sock.connect((address, 10000))


if (len(sys.argv) > 1):
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()
