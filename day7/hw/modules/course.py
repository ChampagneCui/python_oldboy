#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import pickle
from sys import path
path.append('..\conf')

def outer(func):
    def inner(*args,**kwargs):
        login_user = pickle.load(open(LOGIN_USER_PATH))
        if current_user in login_user:
            r = func(*args, **kwargs)
            return r
        else:
            print('请登录！')
    return inner

class teachers:
    def __init__(self):
        name = raw_input('name:')
        age = raw_input('age:')
        favour = raw_input('favour:')
        self.name=name
        self.age=age
        self.asset=0
        self.favour = favour

    def grade(self,point):
        if int(point)>=3:
            print('Thx! Have a nice lessons!')
        else:
            self.asset=self.asset-5

    def gain(self,fee):
        self.asset = self.asset + fee

class courses:
    def __init__(self,name,fee,teacher):
        name = raw_input('Please enter a course you want create:')
        fee = raw_input('How much:')
        teacher = raw_input('Which teacher?')
        self.name = name
        self.fee=fee
        self.teacher=teacher

    def lessons(self,experience,course,fee):
        teachers.gain(fee)
        students.st_add_experience(course,fee)

class students:
        def __init__(self,name, age):
            self.name=name
            self.age=age
            self.asset=0
            self.experience=[]

        def st_add_money(self,money):
            self.asset+=money

        def st_add_experience(self,course,fee):
            self.experience.append(course)
            self.asset-=fee


def login(role):
    global current_user
    while 1:
        username = raw_input('请输入账号：')
        password = raw_input('请输入密码')
        if role='1':
            if s_login(username,password) == 0:
                current_user=username
                break
        elif role='2':
            if t_login(username,password) == 0:
                current_user=username
                break
        elif role='3':
            if m_login(username,password) == 0:
                current_user=username
                break




# a=teachers()
# teachers_path=teachers_db_path+a.name
# f=file(teachers_path,'w')
# pickle.dump(a,f)
# f.close()

# f=file('1.txt')
# b=pickle.load(f)
# f.close()
# print(b.name)
# b.print_info()

