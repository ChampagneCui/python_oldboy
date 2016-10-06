#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json

user_path=r'..\db\market\user.txt'
b_user_path=r'..\db\bank\b_user.txt'
record_path=r'..\db\market\record.txt'
b_record_path=r'..\db\bank\b_record.txt'
login_user_path=r'..\db\market\login_user.txt'
b_login_user_path=r'..\db\bank\b_login_user.txt'
user_table=json.load(open(r'..\db\market\user.txt'))
b_user_table=json.load(open(r'..\db\bank\b_user.txt'))
user_record=json.load(open(r'..\db\market\record.txt'))
b_user_record=json.load(open(r'..\db\bank\b_record.txt'))
market=json.load(open(r'..\db\market\market.txt'))
current_user='None'
b_current_user='None'
budget=15000
p_sort={}
p_sort1={}
car=[]
welcome_msg='''
1.购物市场
2.ATM机
请输入序号：'''

s_welcome_msg='''
1.购物
2.登陆
3.查看购物历史
4.注册
5.登出
>>>请输入序号：'''

b_welcome_msg='''
1.取现
2.登陆
3.还款
4.转账
5.查流水账
6.管理
7.登出
>>>请输入序号：'''