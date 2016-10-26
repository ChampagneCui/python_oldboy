#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import pickle
from sys import path
path.append('..\conf')
from login_system import login
from login_system import register
from login_system import logout

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
        passwd = raw_input('password:')
        age = raw_input('age:')
        favour = raw_input('favour:')
        self.name=name
        self.password=passwd
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
        def __init__(self,name,passwd,age):
            self.name=name
            self.password=passwd
            self.age=age
            self.asset=0
            self.experience=[]

        def st_add_money(self,money):
            self.asset+=money

        def st_add_experience(self,course,fee):
            self.experience.append(course)
            self.asset-=fee


def welcome(role):
    global current_user
    while 1:
        username = raw_input('请输入账号：')
        password = raw_input('请输入密码')
        if login(username,password,role) == 0:
                current_user=username
                if role=='1':
                    s_main()
                elif role=='2':
                    t_main()
                elif role=='3':
                    m_main()
                break

def s_main():
    pass

def t_main():
    pass

def m_main():
    pass






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

