#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from sys import path
path.append(r'..\modules')
path.append('..\conf')
from settings import *
from shopping_car import s_main
from atm import b_main

def main():
    choose=raw_input(WELCOME_MSG)
    if choose=='1':
        s_main()
    elif choose=='2':
        b_main()
    else:
        print('请重新输入：')
        main()

if __name__ == '__main__':
    main()