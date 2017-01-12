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
    opts, args = getopt.getopt(sys.argv[1:], "ha:b:c:")
    if len(opts) == 1:
        for op, value in opts:
            if (op == "-a"):
                aa = value
            elif (op == "-p"):
                aa = value
            elif (op == "-g"):
                aa = value

        print(aa)
    # if choice[0]=='show':
    #     print(dic.keys())
    # elif choice[0] == 'get':
    #     get(choice)
    # elif choice[0] == 'put':
    #     put(choice)
    # else:
    #     ssh_command(choice)