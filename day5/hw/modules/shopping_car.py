#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import time
import json
from sys import path
path.append('..\conf')
from env import *
from login_market import login
from login_market import register
from login_market import logout
from atm import pay
#最后使用了如下几个全局变量
#car用来存放购物车信息
#money当前剩余的金钱
#p_sort 用来记录分类与number的关系
#p_sort1 用来记录分类下各物品与number的关系
#market1用来记录所有物品及价格

def outer(func):
    def inner(*args,**kwargs):
        login_user = json.load(open(login_user_path))
        if current_user in login_user:
            r = func(*args, **kwargs)
            return r
        else:
            print('请登录！')
    return inner

def check_num(num):
    num=str(num)
    if num.isdigit()==True:#用digit函数判断
        return 0
    else:
        print('Please enter a right number!')
        return 1

@outer
def query_record_detail(u=''): #显示详细（带时间）
    if u!='':
        print('Product','Quantity','Price','Time')
        count=0
        for i in user_record[u]:
            count+=1
            if count%4==0:
                print(i)
            else:
                print(i),
        print('end').center(50,'*')

@outer
def init_shop_list():
    global p_sort
    for i in enumerate(market):
        index = i[0]
        p_product = i[1]
        print(index, p_product)
        p_sort[index] = p_product
    choose(1)    #1代表来自菜单的选择，2代表来自购物的选择，两者都会有选择号码及q、b，但是购物的选择需要多问一个quantity，以此区别

@outer
def choose(i):
    choice=raw_input('Please enter your choice(\'q\' for exit and \'b\' for back!):')
    if choice=='q':
        clearing()
    elif choice=='b':
        init_shop_list()
    else:
        if i == 1:
            if check_num(choice) == 1:
                choose(1)
            else:
                shop_list(choice)
        elif i==2 :
            if check_num(choice)==0:
                choice = int(choice)
                quantity = raw_input('Please enter the quantity!')
                while check_num(quantity)==1:
                    quantity = raw_input('Please enter the quantity!')
                quantity=int(quantity)
                shopping(choice,quantity)
            else:
                choose(2)

@outer
def shop_list(choice):
    global p_sort1
    global market1
    if int(choice)<len(p_sort):
        market1=market[p_sort[int(choice)]]
        for i in enumerate(market1):
            index = i[0]
            p_product = i[1]
            p_price = market1[i[1]]
            print(index, p_product, p_price)
            p_sort1[index]=p_product
        choose(2)
    else:
        print('Wrong number!')

@outer
def shopping(num,quantity):
    global car
    if num<len(p_sort1):
        p_price=market1[p_sort1[num]]
        car.append(p_sort1[num])
        car.append(quantity)
        car.append(p_price*quantity)
        timestamp=time.localtime()
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
        car.append(timestamp)
    else:
        print('No such product!')

@outer
def clearing():
    i=2
    money=0
    while i < len(car):
        money+=car[i]
        i+=4
    print('您本次购物的商品为：{0}').format(car)
    print('总金额为{0}').format(money)
    result=pay(money)
    if result==0:   #付费交给银行
        user_record[current_user]+=car
        json.dump(user_record,open(record_path,'w'))
        logout(current_user)
        exit('see you next time!')
    elif result==1:
        clearing()
    elif result==2:
        print('余额不足！')


def s_main():
    global current_user
    while 1:
        welcome = raw_input(s_welcome_msg)
        if welcome == '1':
            init_shop_list()
        elif welcome == '2':
            username = raw_input('请输入账号：')
            password = raw_input('请输入密码')
            if login(username,password) == 0:
                current_user=username
        elif welcome == '3':
            query_record_detail(current_user)
        elif welcome == '4':
            register()
        elif welcome =='5':
            logout(current_user)
            exit('欢迎下次光临！')
        else:
            print('错误选项，请重新选择!')
