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
    name=raw_input('Name:')
    password=raw_input('passwd:')
    age=raw_input('age:')
    a=students(name,password,age)
    f=STUDENTS_DB_PATH+name
    pickle.dump(a,open(f,'w'))


