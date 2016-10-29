#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import pickle
import os
from sys import path
path.append('..\conf')
from settings import *
from lei import *
from login_system import login


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
    while 1:
        choose=raw_input(S_WELCOME_MSG)
        student_db_file=STUDENTS_DB_PATH+current_user
        student=pickle.load(open(student_db_file))
        if choose == '1':#选课
            for i in os.listdir(COURSES_DB_PATH):
                print i
            course_name=raw_input('Press the course you want！')
            #if_exist_course
            f=COURSES_DB_PATH+course_name
            course=pickle.load(open(f))
            student.choose_course(course)
            pickle.dump(student,open(student_db_file,'w'))
        elif choose == '2':#上课
            for num,i in enumerate(student.course):
                print(num,i.name)
            course_num = raw_input('Press the number you want！')
            #if_exist_course
            student.have_lesson(course_num)
            f=STUDENTS_DB_PATH+student.name
            pickle.dump(student,open(f,'w'))
            # teacher_name=student.course[int(course_num)].teacher.name
            # teacher_path=TEACHERS_DB_PATH+teacher_name
            # pickle.dump(teacher,open(teacher_path,'w'))
        elif choose == '3':#查看历史
            print(student.experience)
        elif choose == '4':#充值
            money=raw_input('How much do you want to add?')
            #check_num(money)
            student.st_add_money(int(money))
            pickle.dump(students,open(student_db_file,'w'))


def m_main():
    while 1:
        choose = raw_input(M_WELCOME_MSG)
        if choose=='1':
            a=teachers()
            f=TEACHERS_DB_PATH+a.name
            pickle.dump(a,open(f,'w'))
        elif choose=='2':
            #创建课程
            course=courses()
            #绑定老师
            for i in os.listdir(TEACHERS_DB_PATH):
                print i
            teacher_name=raw_input('Press bonding teacher!')
            teacher_path=TEACHERS_DB_PATH+teacher_name
            teacher=pickle.load(open(teacher_path))
            course.course_bonding(teacher) #封装
            f=COURSES_DB_PATH+course.name
            pickle.dump(course,open(f,'w'))


#
# #
f=STUDENTS_DB_PATH+'leo'
a=pickle.load(open(f))
print(a.name,a.experience,a.asset,a.course[0].teacher.asset)
#

#
f=TEACHERS_DB_PATH+'kk'
a=pickle.load(open(f))
print(a.name,a.asset)

f=COURSES_DB_PATH+'music'
a=pickle.load(open(f))
print(a.name,a.fee,a.teacher.name)