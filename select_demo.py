#!/usr/bin/env python
#_*_coding:utf-8_*_

import select
import socket
import Queue


server = socket.socket()


server_address = ('localhost',8000)
server.bind(server_address)
server.listen(100)
server.setblocking(0)


def main():
    while True:
        readable,writable,expection=select.select(inputs,outputs,inputs)

        for r in readable:
            if r is server:
                conn, client_addr = r.accept()
                conn.setblocking(0)
                inputs.append(conn)
                m_queue[conn] = Queue.Queue()
            else:
                data = r.recv(1024)
                data=data.decode()
                print("收到数据:", data)
                m_queue[r].put(data)

                if r not in outputs:
                    outputs.append(r)
                else:
                    print("客户端断开了", r)

    for w in writable:
        try:
            next_msg = m_queue[w].get()
        except Queue.Empty:
            print("queue is empty..")
            outputs.remove(w)
        else:
            w.send(next_msg)
            outputs.remove(w)

    for e in expection:
        if e in outputs:
            outputs.remove(e)
            inputs.remove(e)
            e.close()


if __name__ == '__main__':
    inputs = [server, ]
    outputs = []
    m_queue = {}
    main()





