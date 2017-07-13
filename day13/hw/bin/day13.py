#_*_coding:utf-8_*_
from sys import path
path.append(r'../modules')
path.append('../conf')
from settings import *
from students import s_main
from teachers import t_main



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