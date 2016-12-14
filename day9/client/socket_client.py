#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import socket
import base64


def IsOpen(ip,port):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        c.connect((ip,int(port)))
        c.shutdown(2)
        return True
    except:
        return False

def main():
    ip = raw_input('Please enter server IP:')
    port = raw_input('Please enter server port')
    port=int(port) ###lambda
    if IsOpen(ip, port) == True:
        ip_port = (ip, int(port))

        c = socket.socket()
        c.connect(ip_port)

        username = raw_input('请输入账号：')
        password = raw_input('请输入密码：')

        c.send(bytes(base64.encodestring(username)))
        c.send(bytes(base64.encodestring(password)))
        print('Send to server......')
        res = c.recv(1024).decode()

        if res == 'True':
            while 1:
                recv_data = c.recv(1024)
                print(recv_data.decode())
                msg = raw_input("Let's play!>>:").strip()
                c.send(bytes(msg.encode("utf-8")))
                if msg == 'exit': break
        else:
            print('Wrong username or password!')
        c.close()

if __name__=='__main__':
    main()

