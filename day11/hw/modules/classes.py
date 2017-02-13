#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import select
import socket
import Queue


server = socket.socket()


server_addr = ('localhost',10000)
server.bind(server_addr)
server.listen(100)
print('starting up on %s port %s' % server_addr)
server.setblocking(0)

inputs = [server, ] #自己也要监测呀,因为server本身也是个fd
outputs = []
msg_dic= {}


print("waiting for next event...")
readable, writeable, exeptional = select.select(inputs, outputs, inputs)# 如果没有任何fd就绪,那程序就会一直阻塞在这里
server.accept()

while True:
    for r in readable:  # 每个s就是一个socket
        if r is server:
            conn, client_addr = r.accept()
            print("new connection from", client_addr)
            conn.setblocking(0)
            inputs.append(conn)
            msg_dic[conn] = Queue.Queue() #一建立链接就生成队列
        else:
            # 客户端的数据过来了,在这接收
            data = r.recv(1024)
            print("收到数据:",data)
            msg_dic[r].put(data)
            if r not in outputs:
                outputs.append(r) #放入返回的链接队列里
            else:
                print("客户端断开了", r)

                if s in outputs:
                            self.outputs.remove(s)

                        self.inputs.remove(s)
                        del self.message_queues[s]

    for w in writeable:
        try:
            next_msg = msg_dic[w].get()
        except Queue.Empty:
            print("queue is empty..")
            outputs.remove(w)
        else:
            w.send(next_msg)
            outputs.remove(w)

    for e in exeptional:
        if e in outputs:
            outputs.remove(e)
            inputs.remove(e)
            e.close()

        del msg_dic[e]