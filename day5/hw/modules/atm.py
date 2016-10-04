#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import logging
import logging.config
import time
import json
from sys import path
path.append('..\conf')
from env import *
from login_bank import b_login
from login_bank import b_logout
CONF_LOG = "../conf/logging.conf"
logging.config.fileConfig(CONF_LOG)

def check_num(num):
    num=str(num)
    if num.isdigit()==True:#用digit函数判断
        return 0
    else:
        print('Please enter a right number!')
        return 1

def b_outer(func):
    def inner(*args,**kwargs):
        b_login_user = json.load(open(b_login_user_path))
        if b_current_user in b_login_user:
            r = func(*args, **kwargs)
            return r
        else:
            print('请登录！')
    return inner

def login_bank():
    '''登录atm'''
    username = raw_input('请输入账号：')
    password = raw_input('请输入密码')
    if b_login(username, password) == 0:
        current_user = username

@b_outer
def get_remain(u):
    '''额度查询'''
    if u in b_user_table.keys():
        u_budget=b_user_table[u][3]
        return u_budget

@b_outer
def get_cash(u):
    '''提取现金'''
    cash=raw_input('你要取多少')
    if check_num(cash)==1:
        get_cash(u)
    else:
        cash=int(cash)
        u_remain=get_remain(u)
        if cash*2<=(budget-u_remain):
            new_budget=cash*1.05+u_remain
            b_user_table[u][3]=new_budget
            json.dump(b_user_table,b_user_path,'w')
        else:
            print('超额！请重新输入')
            get_cash(u)

@b_outer
def forward_money(u):
    '''转账'''
    forward=raw_input('请输入你要转账的金额')
    target_card=raw_input('请输入你要转账的账号')
    target_u=raw_input('请输入你要转账人的姓名')
    if b_user_table[target_u][1]==target_card:
        if check_num(forward)==1:
            forward_money(u)
        else:
            forward=int(forward)
            u_remain=get_remain(u)
            if forward+u_remain<=budget:
                new_budget=forward+u_remain
                b_user_table[u][3] = new_budget
                json.dump(b_user_table,b_user_path,'w')
    else:
        print('您输入账户有错，请重新输入！')
        forward_money(u)

@b_outer
def check_detail():
    '''查流水账'''
    pass

def pay(amount):
    '''付费及记账，返回0成功，返回1账号密码错误，返回2额度不够'''
    u = raw_input('请输入银行卡账号：')
    p = raw_input('请输入银行卡密码')
    if u in b_user_table.keys() and p==b_user_table[u][0]:
        u_remain = get_remain(u)
        if amount + u_remain <=budget:
            new_budget = amount + u_remain
            b_user_table[u][3] = new_budget
            json.dump(b_user_table, b_user_path, 'w')
            b_user_record[u].append(amount)
            timestamp = time.localtime()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
            b_user_record[u].append(timestamp)
            json.dump(b_user_record,b_record_path,'w')
            return 0
        else:
            return 2 #额度不够
    else:
        return 1 #失败

@b_outer
def manager():
    '''管理接口，包括添加账户、用户额度，冻结账户'''
    pass

#尝试输入密码次数锁定