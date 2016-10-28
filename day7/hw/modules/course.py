#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import pickle
import os
from sys import path
path.append('..\conf')
from settings import *
# from login_system import login
# from login_system import register
# from login_system import logout

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
    def __init__(self):
        name = raw_input('Please enter a course you want create:')
        fee = raw_input('How much:')
        self.name = name
        self.fee=fee

    def course_bonding(self,teacher):
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

class managers:
        def __init__(self,name,passwd):
            self.name=name
            self.password=passwd


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
                    m_main()
                break

def s_main():
    choose=raw_input(S_WELCOME_MSG)
    student_db_file=STUDENTS_DB_PATH+current_user
    student=pickle.load(student_db_file)
    if choose == '1':#选课
        pass
    elif choose == '2':#上课
        pass
    elif choose == '3':#查看历史
        print(student.experience)
    elif choose == '4':#充值
        money=raw_input('How much do you want to add?')
        #check_num(money)
        student.st_add_money(int(money))


def m_main():
    choose = raw_input(M_WELCOME_MSG)
    teachers_list = pickle.load(open(r'../db/teachers/teachers.txt'))
    if choose=='1':
        a=teachers()
        teachers_list.append(a)
        pickle.dump(teachers_list,open(TEACHERS_DB_PATH,'w'))
    elif choose=='2':
        #创建课程
        course=courses()
        #绑定老师
        i=0
        while i < len(teachers_list):
            teachers_name_list.append(teachers_list[i].name)
            print(i,teachers_list[i].name)
            i+=1
        choose_t=raw_input('Press num to bonding teacher!')
        #check_num(choose_t)
        teacher=teachers_list[int(choose_t)]
        course.course_bonding(teacher) #封装
        COURSES_DB_FILE=COURSES_DB_PATH+course.name
        pickle.dump(course,open(COURSES_DB_FILE,'w'))

def login(u, p, r):
    if r == '1':
        user_db_path = STUDENTS_DB_PATH
    elif r == '2':
        user_db_path = MANAGERS_DB_PATH

    if u in os.listdir(user_db_path):
        u_file = user_db_path + u
        print(u_file)  ###############
        user = pickle.load(open(u_file))
        print user  ###########
        print(user.name, user.password)  #########
        if user.password == p:
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
        if r == '1':
            ask = raw_input('你要注册吗?(y/n)')
            if ask == 'y':
                register()
        return 1

def register():
    pass

def logout():
    pass

m_main()


# #读取老师列表
# teachers_list=pickle.load(open(r'../db/teachers/teachers.txt'))
# print(teachers_list[0].name)
#
# #添加老师
# a=teachers()
# teachers_list.append(a)
# f=file(TEACHERS_DB_PATH,'w')
# pickle.dump(teachers_list,f)
# f.close()


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

