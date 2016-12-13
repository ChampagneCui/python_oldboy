#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import SocketServer

ip_port=('192.168.10.169',2222)

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        conn=self.request
        conn.sendall(bytes("Welcome to MyServer!"))
        flag=True
        while flag==True:
            recv_data=conn.recv(1024)
            if recv_data.decode()=='exit':
                flag=False
            else:
                send_data = recv_data.decode().upper()
                conn.sendall(bytes(send_data))



if __name__=='__main__':
    server=SocketServer.ThreadingTCPServer((ip_port),MyServer)
    server.serve_forever()