#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: ChenWei
"""

import select
import socket
import queue
import time
import os

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(5)
server.setblocking(False)  # False or 0 代表非阻塞

inputs = [server]
msg_queues = {}

while True:
    # select()方法接收并监控3个通信列表
    # rlist:让select帮你监测,
    # wlist:所有需要返回的放到这里
    # xlist:监测哪些socket有没有出问题
    r_list, w_list, exception_list = select.select(inputs, [], [])  # r_list里面只要有返回，肯定有数据
    for s in r_list:  # s相当于server的对象
        if s is server:  # 代表new conn进来了
            conn, addr = s.accept()
            print('got new conn', conn, addr)
            inputs.append(conn)  # 思路是需要委托select来进行监听
            msg_queues[conn] = queue.Queue()  # conn为key,初始化一个队列
        else:
            try:
                data = s.recv(1024)
                print('recv data from [%s]:[%s]:' % (s.getpeername(), data))
                msg_queues[s].put(data)
                if s not in w_list:
                    w_list.append(s)  # 等下次select的时候，确保w_list的数据能返回给客户端
            except ConnectionResetError as e:
                print("conn closed")
                inputs.remove(s)
                if s in w_list:
                    w_list.remove(s)
                del msg_queues[s]

    for s in w_list:
        try:
            data = msg_queues[s].get_nowait()
            con_str_list = str(data, encoding='utf-8').split(',')
            print('11111111', con_str_list)
            cmd, file_name, file_size = con_str_list
            s.send(bytes(file_name, encoding='utf8'))
            path = os.path.join(r"D:\s15\Day11\FtpSelectors\FtpServer\uploads", file_name)
            with open(path, 'wb') as f:
                init_size = 0
                count = 0
                print('count', init_size)
                while init_size < int(file_size):
                    print('loop', count)
                    data1 = s.recv(1024)
                    init_size += len(data1)
                    count += 1
                    f.write(data1)
                print('upload file [%s] successes' % file_name)

                # s.send(data.upper())
        except queue.Empty as e:
            w_list.remove(s)
