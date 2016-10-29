#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from sys import path
path.append(r'..\modules')
path.append('..\conf')
from settings import *
from course import welcome
from login_system import register


def main():
    choose=raw_input(WELCOME_MSG)
    if choose in ['1','2']:
        welcome(choose)
    elif choose=='3':
        register()
        main()
    else:
        print('请重新输入：')
        main()

if __name__ == '__main__':
    main()