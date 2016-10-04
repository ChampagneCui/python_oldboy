#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json
from sys import path
path.append('..\conf')
from env import *
'''
商城登录模块，负责登录、登出、注册
登录函数登录成功会将登录用户写入login_user
以此实现多用户登录，登出会从login_user中删除
'''

def b_iflock(u):
    if u in b_user_table.keys():
        info=b_user_table[u]
        if info[2]=='y':
            print('You have been locked! Please contact to system admin.')
            return 1
        else:
            return 0
    else:
        return 0

def b_login(u,p):
    if b_iflock(u) == 1:
        return 1
    else:
        if u in b_user_table.keys():
            info=b_user_table[u]
            if info[0] == p:
                print('Welcome Login!')
                if b_user_table[u][1]!=0:
                    b_user_table[u][1] = 0
                    json.dump(b_user_table,open(b_user_path,'w'))
                a=json.load(open(b_login_user_path))
                if u not in a:
                    a.append(u)
                    json.dump(a,open(b_login_user_path,'w'))
                return 0
            else:
                print('账号或密码错误!')
                b_user_table[u][1] +=1
                if b_user_table[u][1] >= 3:
                    b_user_table[u][2] = 'y'
                json.dump(b_user_table, open(b_user_path, 'w'))
                return 1

def b_logout(u):
    a = json.load(open(b_login_user_path))
    if u in a:
        a.remove(u)
        json.dump(a, open(b_login_user_path, 'w'))

