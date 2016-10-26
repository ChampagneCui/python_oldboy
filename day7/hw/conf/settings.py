#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_

DB_PATH=r'../db/'
TEACHERS_PATH=r'teachers/'
TEACHERS_DB_PATH=DB_PATH+TEACHERS_PATH
COURSES_PATH=r'courses/'
COURSES_DB_PATH=DB_PATH+COURSES_PATH
STUDENTS_PATH=r'students/'
STUDENTS_DB_PATH=DB_PATH+STUDENTS_PATH
MANAGERS_PATH=r'managers/'
MANAGERS_DB_PATH=DB_PATH+MANAGERS_PATH

LOGIN_USER_NAME='login_user.txt'
LOGIN_USER_PATH=DB_PATH+LOGIN_USER_NAME
current_user='None'

WELCOME_MSG='''
1.学生登录
2.老师登录
3.管理员登录
请输入序号：'''

T_WELCOME_MSG='''
1.查看余额
请输入序号：'''

S_WELCOME_MSG='''
1.选课
2.上课（上完课评分）
3.查看历史
4.充钱
请输入序号：'''

M_WELCOME_MSG='''
1.新建老师
请输入序号：'''
