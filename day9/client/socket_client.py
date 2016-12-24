#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import socket
import base64
import os
import json

def IsOpen(ip,port):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        c.connect((ip,int(port)))
        c.shutdown(2)
        return True
    except:
        return False

class feature:
    @staticmethod
    def put(cmd_list):
        abs_filepath = cmd_list[1]
        if os.path.isfile(abs_filepath):
            file_size = os.stat(abs_filepath).st_size
            filename = abs_filepath.split('\\')[-1]
            print('file:%s size:%s') % (abs_filepath, file_size)
            msg_data = {'action': 'put', 'filename': filename, 'filesize': file_size}
            c.send(bytes(json.dumps(msg_data)))
            c.recv(1024)

            print('start sending file', filename)
            f = open(abs_filepath, 'rb')
            for line in f:
                c.send(line)
            print('send file done')
            return 1
        else:
            print("file %s is not exist") % (abs_filepath)
            return 0

    def get(cmd_list):
        print('get')


def main(ip='192.168.10.106',port='2222'):
    global c
    port=int(port) ###lambda
    ip_port = (ip, port)
    if IsOpen(ip,int(port))==True:
        c = socket.socket()
        c.connect(ip_port)

        username = raw_input('请输入账号：')
        password = raw_input('请输入密码：')

        c.send(bytes(base64.encodestring(username)))
        c.send(bytes(base64.encodestring(password)))
        print('Send to server......')

        res = c.recv(1024).decode()
        if res == 'True':
            while True:
                recv_data = c.recv(1024)
                print(recv_data.decode())
                send_data=raw_input(">>:").strip()
                if len(send_data)==0:continue
                cmd_list=send_data.split()
                if len(cmd_list)<2:continue
                task_type=cmd_list[0]
                if hasattr(feature, task_type):
                    func=getattr(feature, task_type)
                    a=func(cmd_list)
                    #a=feature.put(cmd_list)
                    if a==0:continue
                else:
                    print("doesn't support type.")
        else:
            print('Wrong username or password!')
        c.close()
    else:
        print('Remote server does not exist!')

if __name__=='__main__':
    ip = raw_input('Please enter server IP:')
    port = raw_input('Please enter server port:')
    #main(ip,port)
    main()

