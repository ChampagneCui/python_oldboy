#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
# import logging
# import logging.config
# CONF_LOG = "../conf/logging.conf"
# logging.config.fileConfig(CONF_LOG)# 采用配置文件
# logger = logging.getLogger("xzs")
# logger.debug("Hello xzs")
#
# logger = logging.getLogger()
# logger.info("Hello root")
#
# ttt='hi everyone'
# logger = logging.getLogger("ttt")
# logger.critical(ttt)
from sys import path
path.append('..\conf')
from env import *
from shopping_car import s_main
from atm import b_main

def main():
    choose=raw_input(welcome_msg)
    if choose=='1':
        s_main()
    elif choose=='2':
        b_main()
    else:
        print('请重新输入：')
        main()

if __name__ == '__main__':
    main()