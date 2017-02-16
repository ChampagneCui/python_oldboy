#!/usr/bin/env python3
#_*_coding:utf-8_*_

from sys import path
path.append(r'../conf')
path.append(r'../modules')
from settings import *
from classes import *
import selectors
import socket

sel = selectors.DefaultSelector()
sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    recv_data = conn.recv(1000)  # Should be ready
    if data:
            print('echoing', repr(recv_data), 'to', conn)
            data=json.loads(recv_data.decode())
            action=data.get("action")
            if hasattr(feature,action):
                    func = getattr(feature, action)
                    func(data,conn)
            else:
                    print("task action is not supported", action)
    else:
            print('closing', conn)
            sel.unregister(conn)
            conn.close()


while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
