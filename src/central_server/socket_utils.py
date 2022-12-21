import socketserver
import subprocess
import sys
from threading import Thread
from pprint import pprint
import json


class SingleTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the client connection
        data = self.request.recv(8192)  # clip input at 1Kb
        self.request.send(bytes(json.dumps({"status": "success!"}), 'UTF-8'))
        self.request.close()


class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(
            self, server_address, RequestHandlerClass)
