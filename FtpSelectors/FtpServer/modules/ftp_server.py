#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: ChenWei
"""
import socket
import os
from lib import tools
from conf import settings
from conf import code


class FtpServer:
    def __init__(self, args):
        self.args = args
        self.args_parse()
        self.conn = None
        self.addr = None

    def args_parse(self):
        if len(self.args) != 2:
            tools.help_msg(self.args[0])
            exit()
        if hasattr(self, self.args[1]):
            func = getattr(self, self.args[1])
            func()
        else:
            tools.help_msg(self.args[0])
            exit()

    def start(self):
        server = socket.socket()
        server.bind((settings.SERVER_IP, settings.PORT))
        server.listen(5)
        print(tools.get_color('FTP服务器{}:{}已启动'.format(settings.SERVER_IP, settings.PORT), color='green'))
        while True:
            self.conn, self.addr = server.accept()
            print('建立新的连接----', self.conn, self.addr)
            while True:
                try:  # 捕获客户端异常关闭
                    receive_data = self.conn.recv(1024)  # 等待接收客户端消息
                    if len(receive_data) == 0:
                        break
                    self.cmd_parse(receive_data)
                except ConnectionResetError as e:
                    break

    def cmd_parse(self, data):
        conv_recv_data = str(data, encoding='utf8')
        recv_data_list = conv_recv_data.split(',')
        if hasattr(self, recv_data_list[0]):
            func = getattr(self, recv_data_list[0])
            func(recv_data_list)
        else:
            print('调用错误!')

    def put(self, data_list):
        """
        客户端上传文件,服务端接收
        :return:
        """
        print('put-->', data_list)
        cmd, file_name, file_size = data_list
        self.conn.send(bytes(file_name, encoding='utf8'))
        init_size = 0
        path = os.path.join(settings.UPLOAD_FILES_PATH, file_name)
        with open(path, 'wb') as f:
            while init_size < int(file_size):
                data = self.conn.recv(1024)
                init_size += len(data)
                f.write(data)
            print('upload file [%s] successes' % file_name)

    def get(self, data_list):
        file = os.path.join(settings.UPLOAD_FILES_PATH, data_list[-1])
        if os.path.exists(file):
            fsize = os.path.getsize(file)
            send_info = '{},{}'.format(code.code_list['100'], fsize)
            self.conn.send(bytes(send_info, encoding='utf8'))
            if str(self.conn.recv(1024), 'utf-8') == "ready":
                with open(file, 'rb') as f:
                    for line in f:
                        self.conn.send(line)
                print(tools.get_color('[%s]文件下载完毕' % (file,), color='green'))
        else:
            send_info = '{},{}'.format(code.code_list['101'], 0)
            self.conn.send(bytes(send_info, encoding='utf8'))
            print(tools.get_color('get,文件不存在'))
