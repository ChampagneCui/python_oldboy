#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from sys import path
path.append(r'..\modules')
path.append('..\conf')
from settings import *
from course import login


def main():
    choose=raw_input(WELCOME_MSG)
    if choose in ['1','2','3']:
        login(choose)
    else:
        print('请重新输入：')
        main()

if __name__ == '__main__':
    main()