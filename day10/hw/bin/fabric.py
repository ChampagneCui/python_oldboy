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
    #
    #fab --ip=leo@192.168.1.1:2299 --command="shell"
    #fab --ip=192.168.1.1. --command="put" --src="/tmp" --dest="/tmp"
    opts, args = getopt.getopt(sys.argv[1:],longopts =["help","host"=,"command=","src=","dest="])
    for op, value in opts:
            if (op == "--help"):
                usage() #help说明
            elif (op == "--host"):
                #用正则匹配@：，等，没有则给予默认
            elif (op == "--command"):
                command=value
            elif (op == "--src"):
                src=value
            elif (op == "--dest"):
                dest= value

    if command=='shell':


    # if choice[0]=='show':
    #     print(dic.keys())
    # elif choice[0] == 'get':
    #     get(choice)
    # elif choice[0] == 'put':
    #     put(choice)
    # else:
    #     ssh_command(choice)