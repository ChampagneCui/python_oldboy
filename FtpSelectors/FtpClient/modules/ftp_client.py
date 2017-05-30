#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: ChenWei
"""
import socket
import sys
import os
from lib import tools
from conf import code
from conf import settings


class FtpClient:
    def __init__(self, args):
        self.args = args
        self.host = None
        self.port = None
        self.sk = None
        self.args_parse()
        self.conn()

    def args_parse(self):
        if len(self.args) != 5:
            tools.help_msg(self.args[0])
            exit()
        require_args = ['-s', '-p']
        for arg in require_args:
            if arg not in self.args:
                sys.exit("参数错误")
            try:
                self.host = self.args[self.args.index('-s') + 1]
                self.port = int(self.args[self.args.index('-p') + 1])
            except Exception as e:
                tools.help_msg(self.args[0])

    def conn(self):
        try:
            self.sk = socket.socket()
            print(tools.get_color('连接FTP服务器{}:{}...'.format(self.host, self.port), color='green'))
            self.sk.connect((self.host, self.port))
            print(tools.get_color('连接FTP服务器成功!', color='green'))
            self.cmd_parse()
        except Exception as e:
            print(e)

    def cmd_parse(self):
        while True:
            user_inp = input('CMD >>:').strip()
            if user_inp == 'exit':
                break
            inp_list = user_inp.split()
            if len(inp_list) != 2:
                print('输入错误!')
                continue
            else:
                if hasattr(self, inp_list[0]):
                    func = getattr(self, inp_list[0])
                    func(inp_list)
                else:
                    print(tools.get_color('调用错误!'))

    def put(self, inp_list):
        """
        上传文件模块：put <文件名>
        :param inp_list: 用户输入参数
        :return:
        """
        if os.path.isfile(inp_list[-1]):
            fname = os.path.basename(inp_list[-1])
            fsize = os.path.getsize(inp_list[-1])
            put_info = '{cmd},{file_name},{file_size}'.format(cmd=inp_list[0], file_name=fname, file_size=fsize)
            print("File Size: ", fsize)
            self.sk.send(bytes(put_info, encoding='utf8'))  # 发送给服务端上传文件信息
            recv_data = self.sk.recv(1024)  # 接收服务端发回的确认，我是用文件名进行匹配
            print('recv_data-->', recv_data)
            sended_size = 0
            count = 0
            print('--------Begin Send Data --------------')
            with open(inp_list[-1], 'rb') as f:
                while fsize - sended_size >= 1024:
                    contant = f.read(1024)
                    r_size = len(contant)
                    self.sk.send(contant)
                    sended_size += r_size
                    count += 1
                else:
                    contant = f.read(fsize - sended_size)
                    self.sk.send(contant)
                    count += 1

            print('count >>>>>',count)
            print("Sended File Size >>>>", sended_size)
            print(tools.get_color('[%s]文件上传完毕' % (fname,), color='green'))
        else:
            print('文件不存在')

    def get(self, inp_list):
        inp = ','.join(inp_list)
        self.sk.send(bytes(inp, encoding='utf8'))  # 发送信息到服务端 (cmd,file)
        recv_by_server = self.sk.recv(1024)  # 接收服务端返回的消息，文件是否存在
        file_status, fsize = str(recv_by_server, encoding='utf8').split(',')
        if file_status == code.code_list['100']:
            self.sk.send(bytes("ready", encoding='utf8'))

            path = os.path.join(settings.DOWNLOAD_FILES_PATH, inp_list[-1])
            init_size = 0
            with open(path, 'wb') as fw:
                while init_size < int(fsize):
                    data = self.sk.recv(1024)
                    init_size += len(data)
                    fw.write(data)
                print(tools.get_color('Download file [%s] Successes' % inp_list[-1], color='green'))
        else:
            print("File doesn't exist")
