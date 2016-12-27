#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import socket
import base64
import os,sys
import json
import hashlib
import time
import platform

def isWindowsSystem():
    return 'Windows' in platform.system()

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
            filename = abs_filepath.split(separator)[-1]
            md5sum=feature.md5(abs_filepath)
            print('file:%s size:%s') % (abs_filepath, file_size)
            msg_data = {'action': 'put', 'filename': filename, 'filesize': file_size,'md5':md5sum}
            c.send(bytes(json.dumps(msg_data)))
            time.sleep(0.5)

            print('start sending file', filename)
            f = open(abs_filepath, 'rb')
            for line in f:
                c.send(line)
            print('send file done')
        else:
            print("file %s is not exist") % (abs_filepath)

    @staticmethod
    def fget(cmd_list):
        abs_filepath = cmd_list[1]
        msg_data={'action':'fget','file':abs_filepath}
        c.send(bytes(json.dumps(msg_data)))
        msg_data=json.loads(c.recv(1024).decode())
        filesize=int(msg_data.get('filesize'))
        filemd5=msg_data.get('md5')
        filename=abs_filepath.split('\\')[-1]
        f = open(filename, 'wb')
        recv_size = 0
        time.sleep(0.5)
        while recv_size < filesize:
            data = c.recv(1024)
            f.write(data)
            recv_size += len(data)
            done = int(50 * recv_size / filesize)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
            sys.stdout.flush()
        print('file recv success')
        f.close()
        if feature.md5(filename)==filemd5:
            print('md5sum ok')
        else:
            print(feature.md5(filename))
            print(filemd5)
            print('md5sum fail')

    @classmethod
    def md5(self, filepath):
        f = open(filepath, 'rb')
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        f.close()
        return str(hash).upper()

    @staticmethod
    def ls( *args,**kwargs):
        msg_data = {'action': 'ls'}
        c.send(bytes(json.dumps(msg_data)))
        list=eval(c.recv(4096).decode())
        i=0
        try:
            while i < len(list):
                print(list[i])
                i+=1
        except:
            print('nothing！')

    @staticmethod
    def cd(cmd_list):
        abs_filepath = cmd_list[1]
        msg_data = {'action': 'cd','path': abs_filepath}
        c.send(bytes(json.dumps(msg_data)))
        if c.recv(1024)==False:
            print('No such directory!')



def main( ip='127.0.0.1', port=2222 ):
    global c
    port=int(port)
    ip_port = (ip, port)
    if IsOpen(ip,int(port))==True:
        c = socket.socket()
        c.connect(ip_port)
        username = raw_input('请输入账号：')
        password = raw_input('请输入密码：')

        c.send(bytes(base64.encodestring(username)))
        time.sleep(0.5)
        c.send(bytes(base64.encodestring(password)))
        print('Send to server......')

        res = c.recv(1024).decode()
        if res == 'True':
            recv_data = c.recv(1024)
            print(recv_data.decode())
            while True:
                send_data=raw_input(">>:").strip()
                if len(send_data)==0:continue
                cmd_list=send_data.split()
                task_type=cmd_list[0]
                if hasattr(feature, task_type):
                    func=getattr(feature, task_type)
                    func(cmd_list)
                else:
                    print("doesn't support type.")
                continue
        else:
            print('Wrong username or password!')
        c.close()
    else:
        print('Remote server does not exist!')

if __name__=='__main__':
    if isWindowsSystem==True:
        separator='\\'
    else:
        separator='/'

    ip = raw_input('Please enter server IP:')
    port = raw_input('Please enter server port:')
    #main(ip,port)
    main()



