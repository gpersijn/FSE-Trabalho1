# #!/usr/bin/env python3
import socketserver
import subprocess
import sys
from threading import Thread
from pprint import pprint
from .socket_utils import SingleTCPHandler, SimpleServer
import json


def init(ip, port):
    server = SimpleServer((ip, port), SingleTCPHandler)
    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)
