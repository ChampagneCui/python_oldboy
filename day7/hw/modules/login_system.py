#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import pickle
import os
from sys import path
path.append('..\conf')
from settings import *
from lei import *


def login(u,p,r):
    if r=='1':
        user_db_path=STUDENTS_DB_PATH
    elif r=='2':
        user_db_path = MANAGERS_DB_PATH

    if u in os.listdir(user_db_path):
        u_file=user_db_path+u
        user=pickle.load(open(u_file))
        if user.password==p:
            print('welcome login!')
            # f=file(LOGIN_USER_PATH)
            # a = pickle.load(f)
            # f.close()
            # if u not in a:
            #     a.append(u)
            #     f=file(LOGIN_USER_PATH,'w')
            #     pickle.dump(a,f)
            #     f.close()
            return 0
        else:
            print('账号或密码错误!')
            return 1
    else:
        print('没有这个用户!')
        if r=='1':
            ask = raw_input('你要注册吗?(y/n)')
            if ask == 'y':
                register()
        return 1

def register():
    pass

def logout():
    pass

