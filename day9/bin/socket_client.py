#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import socket
import base64

ip_port=('192.168.10.169',2222)

c=socket.socket()

c.connect(ip_port)

username = raw_input('请输入账号：')
password = raw_input('请输入密码：')

c.send(bytes(base64.encodestring(username)))
c.send(bytes(base64.encodestring(password)))
print('Send to server......')
res=c.recv(1024).decode()

if res == 'True':
    while 1:
        recv_data=c.recv(1024)
        print(recv_data.decode())
        msg=raw_input("Let's play!>>:").strip()
        c.send(bytes(msg.encode("utf-8")))
        if msg == 'exit': break
else:
    print('Wrong username or password!')
c.close()