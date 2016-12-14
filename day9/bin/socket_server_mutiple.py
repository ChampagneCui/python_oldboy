#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import SocketServer
import base64

from sys import path
path.append('..\conf')
from settings import *

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        conn=self.request
        u=base64.decodestring(conn.recv(1024).decode())
        p=base64.decodestring(conn.recv(1024).decode())
        print(u,p)
        if u in dic.keys() and p==dic[u][0]:
            conn.sendall(bytes("True"))
            conn.sendall(bytes(welcome_msg))
            flag=True
            while flag==True:
                recv_data=conn.recv(1024)
                if recv_data.decode()=='exit':
                    flag=False
                else:
                    send_data = recv_data.decode().upper()
                    conn.sendall(bytes(send_data))
        else:
            conn.sendall(bytes("False"))



if __name__=='__main__':
    server=SocketServer.ThreadingTCPServer((ip_port),MyServer)
    server.serve_forever()