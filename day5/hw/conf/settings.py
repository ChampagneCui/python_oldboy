#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json

DB_BANK=r'../db/bank/'
DB_MARKET=r'../db/market/'

#银行额度
BUDGET_NAME='budget.txt'
BUDGET_PATH=DB_BANK+BUDGET_NAME

#超市用户
USER_NAME='user.txt'
USER_PATH=DB_MARKET+USER_NAME

#银行用户
B_USER_NAME='b_user.txt'
B_USER_PATH=DB_BANK+B_USER_NAME

#超市消费记录
RECORD_NAME='record.txt'
RECORD_PATH=DB_MARKET+RECORD_NAME

#银行流水账
B_RECORD_NAME='b_record.txt'
B_RECORD_PATH=DB_BANK+B_RECORD_NAME

#超市登录用户记录
LOGIN_USER_NAME='login_user.txt'
LOGIN_USER_PATH=DB_MARKET+LOGIN_USER_NAME

#银行登录用户记录
B_LOGIN_USER_NAME='b_login_user.txt'
B_LOGIN_USER_PATH=DB_BANK+B_LOGIN_USER_NAME

#超市货物
MARKET_NAME='market.txt'
MARKET_PATH=DB_MARKET+MARKET_NAME
MARKET=json.load(open(MARKET_PATH))

user_table=json.load(open(USER_PATH))
b_user_table=json.load(open(B_USER_PATH))
user_record=json.load(open(RECORD_PATH))
b_user_record=json.load(open(B_RECORD_PATH))
budget=open(BUDGET_PATH).read()
budget=int(budget)


current_user='None'
b_current_user='None'
p_sort={}
p_sort1={}
car=[]

WELCOME_MSG='''
1.购物市场
2.ATM机
请输入序号：'''

S_WELCOME_MSG='''
1.购物
2.登陆
3.查看购物历史
4.注册
5.登出
>>>请输入序号：'''

B_WELCOME_MSG='''
1.取现
2.登陆
3.还款
4.转账
5.管理
6.登出
>>>请输入序号：'''