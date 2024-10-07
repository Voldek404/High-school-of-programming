from socketserver import BaseRequestHandler, TCPServer
import threading
from socket import socket, AF_INET, SOCK_STREAM


class TestTCPHandler(BaseRequestHandler):

    def handle(self):
        print("handle activated", self.client_address)
        self.data = self.request.recv(1024).strip()
        print(self.data)
        self.request.send(b'privet, User')


server = ThreadingTCPServer(('localhost', 12345), TestTCPHandler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()

clients = []
ports = [12345]
for port in ports:
    for _ in range(5):
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(('localhost', port))
        clients.append(client)
for client in clients:
    client.send(b'Hello')
    print(client.recv(1024).strip())
