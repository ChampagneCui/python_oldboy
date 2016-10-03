#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json

user_path=r'..\db\user.txt'
record_path=r'..\db\record.txt'
login_user_path=r'..\db\login_user.txt'
user_table=json.load(open(r'..\db\user.txt'))
user_record=json.load(open(r'..\db\record.txt'))
market=json.load(open(r'..\db\market.txt'))
#login_user = json.load(open(login_user_path))
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
