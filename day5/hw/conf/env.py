#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json

user_path=r'..\db\market\user.txt'
b_user_path=r'..\db\bank\b_user.txt'
record_path=r'..\db\market\record.txt'
login_user_path=r'..\db\market\login_user.txt'
user_table=json.load(open(r'..\db\market\user.txt'))
b_user_table=json.load(open(r'..\db\bank\b_user.txt'))
user_record=json.load(open(r'..\db\market\record.txt'))
market=json.load(open(r'..\db\market\market.txt'))
current_user='None'
welcome_msg='''
1.购物
2.登陆
3.查看购物历史
4.注册
5.登出
>>>请输入序号：'''
car=[] #购物车
p_sort={}
p_sort1={}
