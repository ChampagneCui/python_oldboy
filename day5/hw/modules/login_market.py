#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json
from sys import path
path.append('..\conf')
from settings import *
'''
商城登录模块，负责登录、登出、注册
登录函数登录成功会将登录用户写入login_user
以此实现多用户登录，登出会从login_user中删除
'''

def iflock(u):
    if u in user_table.keys():
        info=user_table[u]
        if info[2]=='y':
            print('You have been locked! Please contact to system admin.')
            return 1
        else:
            return 0
    else:
        return 0

def login(u,p):
    if iflock(u) == 1:
        return 1
    else:
        if u in user_table.keys():
            info=user_table[u]
            if info[0] == p:
                print('Welcome Login!')
                if user_table[u][1]!=0:
                    user_table[u][1] = 0
                    json.dump(user_table,open(USER_PATH,'w'))
                a=json.load(open(LOGIN_USER_PATH))
                if u not in a:
                    a.append(u)
                    json.dump(a,open(LOGIN_USER_PATH,'w'))
                return 0
            else:
                print('账号或密码错误!')
                user_table[u][1] +=1
                if user_table[u][1] >= 3:
                    user_table[u][2] = 'y'
                json.dump(user_table, open(USER_PATH, 'w'))
                return 1
        else:
            print('没有这个用户!')
            ask = raw_input('你要注册吗?(y/n)')
            if ask == 'y':
                register()
            return 1

def register():
    u = raw_input('请输入你要注册的账号:')
    p = raw_input('密码:')
    if u in user_table.keys():
        print('账户已存在.')
    else:
        user_table[u] = [p, 0, 'n']
    json.dump(user_table, open(USER_PATH, 'w'))
    print('Successful!')

def logout(u):
    a = json.load(open(LOGIN_USER_PATH))
    if u in a:
        a.remove(u)
        json.dump(a, open(LOGIN_USER_PATH, 'w'))

