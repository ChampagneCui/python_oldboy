#_*_coding:utf-8_*_
from sys import path
path.append(r'..\modules')
path.append('..\conf')
from settings import *
from students import t_login
from teachers import s_login
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


def main():
    choose=raw_input(WELCOME_MSG)
    if choose=='1':
        s_main()
    elif choose=='2':
        t_main()
    else:
        print('请重新输入：')
        main()

if __name__ == '__main__':
    main()