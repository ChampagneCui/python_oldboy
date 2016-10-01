#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json
from sys import path
path.append('..\conf')
from env import *


def outer(func):
    def inner(*args,**kwargs):
        if current_user in login_user:
            r = func(*args, **kwargs)
            return r
        else:
            print('请登陆！')
    return inner


def login(u,p):
    if u in user_table.keys():
        info=user_table[u]
        if info[0] == p:
            print('Welcome Login!')
            if user_table[u][1]!=0:
                user_table[u][1] = 0
                json.dump(user_table,open(user_path,'w'))
            return 0
        else:
            print('username or password wrong!')
            user_table[u][1] +=1
            if user_table[u][1] >= 3:
                user_table[u][2] = 'y'
            json.dump(user_table, open(user_path, 'w'))
            return 1
    else:
        print('No such user!')
        ask = raw_input('Do you want sign up a new acount?(y/n)')
        if ask == 'y':
            f = open(user_path, 'w')
            uu = raw_input('Please enter new username:')
            pp = raw_input('Passwd:')
            if uu in user_table.keys():
                print('Username alread exist.')
            else:
                user_table[uu] = [pp, 0, 'n']
            result = user_table
            f.write(str(result))
            f.close()
            print('Successful!')
        return 1
