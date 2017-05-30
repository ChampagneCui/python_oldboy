#!/usr/bin/env python
#_*_coding:utf-8_*_

import socket

def main():
    send_data = raw_input('>>:')
    print("send",send_data)
    s.send(bytes(send_data))
    s.close()


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s=socket.socket()
    s.connect(server_address)
    main()