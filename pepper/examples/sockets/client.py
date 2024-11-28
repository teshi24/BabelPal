#!/usr/bin/env python27
# Run the script with Python 2.7
# example:   C:\Python27\python.exe client.py

import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 54321        # The port used by the server

print("starting python client with python version:")
print(sys.version)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Hello, world')
data = s.recv(1024)

print('Received', repr(data))
