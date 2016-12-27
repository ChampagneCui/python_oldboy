#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import SocketServer
import base64
import json
import time
import os
from sys import path
path.append(r'../conf')
from settings import *
import hashlib


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
                action=data.get("action")
                if hasattr(self,action):
                    conn.send(bytes("start"))
                    func = getattr(self, action)
                    func(data)
                else:
                    print("task action is not supported", action)
        else:
            conn.sendall(bytes("False"))

    def put(self, *args, **kwargs):
        print("put", args, kwargs)
        filesize = args[0].get("filesize")
        filename = args[0].get("filename")
        filemd5 = args[0].get("md5")
        print(filename, filesize)
        f = open(filename, 'wb')
        recv_size = 0
        while recv_size < filesize:
            data = self.request.recv(4096)
            f.write(data)
            recv_size += len(data)
            print(recv_size, 'of',filesize)###
        print('file recv success')
        f.close()
        if MyServer.md5(filename)==filemd5:
            print('md5sum ok')
        else:
            print('md5sum fail')

    def fget(self, *args,**kwargs):
        print("fget", args,kwargs)
        file=args[0].get("file")
        if os.path.isfile(file):
            filemd5=MyServer.md5(file)
            filesize=os.stat(file).st_size
            msg_data=json.dumps({'filesize':filesize,'md5':filemd5})
            self.request.send(bytes(msg_data))
            self.request.recv(1024)
            print('start sending file', file)
            f = open(file, 'rb')
            for line in f:
               self.request.send(line)
            print('send file done')
            f.close()
        else:
            self.request.send(bytes('No such file!'))

    @classmethod
    def md5(self, filepath):
        f = open(filepath, 'rb')
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        f.close()
        return str(hash).upper()

    def ls(self, *args,**kwargs):
        list=os.listdir('./')
        self.request.send(bytes(list))


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer((ip_port), MyServer)
    server.serve_forever()
