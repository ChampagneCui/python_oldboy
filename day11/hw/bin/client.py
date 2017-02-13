#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import socket
import sys


server_address = ('localhost', 10000)

# Create a TCP/IP socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(server_address)

while True:
    msg=bytes(raw_input(">>:"),encoding="utf-8")
    s.sendall(msg)
    data=s.recv(1024)
    print(data)
s.close()