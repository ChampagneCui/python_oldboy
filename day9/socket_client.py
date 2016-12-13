#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import socket

ip_port=('192.168.10.169',2222)

c=socket.socket()

c.connect(ip_port)

while 1:
    recv_data=c.recv(1024)
    print(recv_data.decode())
    msg=raw_input(">>:").strip()
    c.send(bytes(msg.encode("utf-8")))
    if msg == 'exit': break

c.close()