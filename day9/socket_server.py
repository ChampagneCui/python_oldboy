#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import socket
import os

ip_port=('192.168.10.169',2222)

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(ip_port)
s.listen(5)

while 1:
    print("Waiting to connect.")
    conn,addr=s.accept()
    print("Client ip:", addr )

    while 1:
        recv_data=conn.recv(1024)
        if not recv_data:
            print("connect break")
            break
        print(recv_data.decode())

        send_data=recv_data.decode().upper()
        conn.sendall(bytes(send_data))

conn.close()