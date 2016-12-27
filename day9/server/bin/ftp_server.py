#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

import SocketServer
from sys import path
path.append(r'../conf')
path.append(r'../modules')
from settings import *
from classes import MyServer


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer((ip_port), MyServer)
    server.serve_forever()
