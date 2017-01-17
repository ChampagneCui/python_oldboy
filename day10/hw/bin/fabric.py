#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

from sys import path
path.append(r'../conf')
path.append(r'../modules')
from settings import *
from features import *
import sys
import getopt

if __name__ == '__main__':
    #fab --host=leo@192.168.1.1:2299 --command="shell"
    #fab --host=192.168.1.1. --command="put" --src="/tmp" --dest="/tmp"
    opts, args = getopt.getopt(sys.argv[1:],longopts =["help","host=","mode=","src=","dest=","command="])
    for op, value in opts:'
            if (op == "--host"):
                '''用正则匹配@：等，没有则给予默认'''
                if value.find('@'):
                    username,value=value.split('@')
                if value.find(':')
                    hostname,port=value.split(':')
                    continue
                hostname=value
            elif (op == "--mode"):
                mode=value
            elif (op == "--src"):
                src=value
            elif (op == "--dest"):
                dest= value
            elif (op == "--command"):
                command=value
            else:
                usage() #help说明

    if mode=='do':
        ssh_command(hostname,command)
    elif mode=='get':
        get(hostname,src)
    elif mode=='put':
        put(hostname,src,dest)
    elif mode=='show':
        ####

