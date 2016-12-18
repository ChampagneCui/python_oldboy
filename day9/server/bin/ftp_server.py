#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import SocketServer
import base64
import json
import time
from sys import path
path.append(r'../conf')
from settings import *


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        conn=self.request
        u=base64.decodestring(conn.recv(1024).decode())
        p=base64.decodestring(conn.recv(1024).decode())
	print(u,p)
        if u in dic.keys() and p==dic[u][0]:
            conn.sendall(bytes("True"))
            conn.sendall(bytes('welcome FTP : Hello %s' %(u)))
            while True:
                recv_data=conn.recv(1024)
                if len(recv_data)==0:break
		print("[%s] says:%s" %(self.client_address,recv_data.decode()))
		data=json.loads(recv_data.decode())
		action=data.get('action')
		try:
			func=getattr(self,action)
			func(data)
		except:
			print("task action is not supported",action)
        else:
            conn.sendall(bytes("False"))

    def put(self,*args,**kwargs):
	print("put",args,kwargs)
	filesize=args[0].get(filesize)
	filename=args[0].get(filename)
	f= opem()

if __name__=='__main__':
    server=SocketServer.ThreadingTCPServer((ip_port),MyServer)
    server.serve_forever()
