#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: ChenWei
"""
import selectors
import socket
# from conf import settings
import os

sel = selectors.DefaultSelector()


def accept(sock,fd, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)  # 如果数据来了,就调用read



filename_queue = {}


def read(conn, fd, mask):
    try:
        # 查看当前列表中是否有fd的键值,如果没有表示第一次传信息过来
        if not filename_queue.get(fd, ""):
            data = conn.recv(1024)  # Should be ready
            if data:
                con_str_list = str(data, encoding='utf-8').split(',')
                cmd, file_name, file_size = con_str_list
                print('Begin Recv Data From {0}', conn)
                # 记录当前连接客户端要发送的文件信息
                filename_queue.update({fd:{"filename": file_name, "filesize": int(file_size)}})
                # 回传消息
                conn.send(bytes(file_name, encoding='utf8'))
        else:
            # 发送有效数据
            file_name = filename_queue[fd].get("filename")
            file_size = filename_queue[fd].get("filesize")
            save_file = os.path.join(r"E:\Pythontest\Examples\Day11-selecter", file_name)
            if not os.path.isfile(save_file):
                # 第一次发送的时候文件是不存在的
                data = conn.recv(1024)  # Should be ready
            else:
                # 再次发送文件
                curr_file_size = os.path.getsize(save_file)

                if file_size - curr_file_size >= 1024:
                    data = conn.recv(1024)
                else:
                    data = conn.recv(file_size - curr_file_size)

            if data:
                with open(save_file, 'ab') as f:
                    f.write(data)

                if file_size == os.path.getsize(save_file):
                    print("File Size:{0}, Recved Size:{1}".format(file_size, os.path.getsize(save_file)))
                    print("<<<<<< File Recv Completed >>>>>>>>")
                    # 搞定了就清楚当前fd 对应信息,方便再次传新文件
                    if fd in filename_queue.keys():
                        filename_queue.pop(fd)
            else:
                # 可能客户端断开了
                print("客户端 {0} 断开连接了...".format(conn))
                conn.close()

                # print('upload file [%s] successes' % file_name)
    except Exception as e:
        print('closing', e)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)

# 如果有新的请求过来了,就调用accept
sel.register(sock, selectors.EVENT_READ, accept)  # select.select(inputs,outputs ...)来了新连接调用accept

while True:
    events = sel.select()  # 如果没有事件，就卡在这里
    for key, mask in events:
        # print('key', key)
        callback = key.data
        callback(key.fileobj, key.fd, mask)
