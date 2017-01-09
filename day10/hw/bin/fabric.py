#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

from sys import path
path.append(r'../conf')
path.append(r'../modules')
from settings import *
from features import *


if __name__ == '__main__':
    choice=raw_input('Please enter command? :')
    if choice=='show':
        print(dic.keys())
    elif choice == 'get':
        pass
    elif choice == 'put':
        pass
    else:
        ssh_command( 'SSSVL0219','df -H')