#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import time
import copy
from login_sys import iflock
from login_sys import login
#最后使用了如下几个全局变量
#car用来存放购物车信息
#money当前剩余的金钱
#p_sort 用来记录分类与number的关系
#p_sort1 用来记录分类下各物品与number的关系
#market1用来记录所有物品及价格

user_tables=open('f.txt').read()
user_tables=eval(user_tables)
user_record=open('record.txt').read()
user_record=eval(user_record)
market=open('market.txt').read()
market=eval(market)

car=[] #购物车
welcome_msg='welcome to market!'.center(50,'*')
p_sort={}
p_sort1={}

def init():
    global money
    for u in user_tables.keys():
        if u==username :
            if user_tables[u][3]<10:
                print('You havn\'t enough money. Please add money!')
                money = raw_input('How much do you want to add?')
            else:
                money = user_tables[u][3]
                money=int(money)
                print('You have %s in your account.' %(money))
                ans=raw_input('Do you want add money?(y/n) and enter \'qd\' to see your shopping record detail and \'q\' to your shopping record!')
                if ans=='y':
                    while 1:
                        add=raw_input('How much do you want to add?(\'q\' to exit)')
                        if add=='q':
                            break
                        if check_num(add) ==0:
                            money+=int(add)
                            print('You have %s in your account.' % (money))
                            break
                        else:
                            continue
                elif ans=='qd':
                    query_record_detail(username)
                elif ans=='q':
                    query_record(username)

def query_record_detail(u): #显示详细（带时间）
    print('Product','Quantity','Price','Time')
    count=0
    for i in user_record[u]:
        count+=1
        if count%4==0:
            print(i)
        else:
            print(i),
    print('end').center(50,'*')

def find_all_index(arr,item): #显示一个元素在一个列表中的所有位置
    return [i for i,a in enumerate(arr) if a==item]

def query_record(u): #显示总共信息（想同叠加）
    summary=[]
    record=user_record[u]
    values={}
    for i in market.keys():
        values=dict(values,**market[i])
    market_total=values
    for i in market_total.keys():
        location = find_all_index(record, i)
        total = 0
        total_price=0
        if location == []:
            continue
        elif len(location) == 1:
            summary.append([i, 1,market_total[i]])
        else:
            for n in location:
                n=int(n)+1
                a = record[n]
                total+=a
                n=n+1
                b = record[n]
                total_price+=b
            summary.append([i,total,total_price])
    print('Product','Quantity','Total_price')
    for i in summary:
        for l in i:
            print(l),
        print('')
    print('end').center(50, '*')

def check_num(num):
    num=str(num)
    if num.isdigit()==True:#用digit函数判断
        return 0
    else:
        print('Please enter a right number!')
        return 1

def init_shop_list():
    global p_sort
    for i in enumerate(market):
        index = i[0]
        p_product = i[1]
        print(index, p_product)
        p_sort[index] = p_product
    choose(1)    #1代表来自菜单的选择，2代表来自购物的选择，两者都会有选择号码及q、b，但是购物的选择需要多问一个quantity，以此区别

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
                choose()

def shop_list(choice):
    global p_sort1
    global market1
    if int(choice)<=len(p_sort):
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

def shopping(num,quantity):
    global car
    global money
    print num,type(num),p_sort1
    if num<=len(p_sort1):
        old_money=money
        old_car=copy.deepcopy(car) #要用deepcopy
        p_price=market1[p_sort1[num]]
        car.append(p_sort1[num])
        car.append(quantity)
        car.append(p_price*quantity)
        timestamp=time.localtime()
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S", timestamp)
        car.append(timestamp)
        money=int(money)
        money-=(p_price*quantity)
        if money<0:
            print('You haven\'t enough money!')
            money=old_money
            car=old_car
    else:
        print('No such product!')

def clearing():
    f=open('f.txt','w')  #结算钱
    user_tables[username][3]=money
    result = user_tables
    f.write(str(result))
    f.close()
    r=open('record.txt','w')
    user_record[username]+=car
    result = user_record
    r.write(str(result))
    r.close()
    exit('See you next time!')


if __name__ =='__main__':
    print(welcome_msg)
    while 1:
        username = raw_input('username:')
        password = raw_input('password:')
        if iflock(username) == 0:  # 判断该用户是否为锁定用户
            if login(username, password)==0: # 登录
                break
            else:
                continue
        else:
            continue            #至此均为登录阶段
    init()   #提取用户信息，询问是否充值
    while check_num(money)==1:
        money=int(money)
        init()
    while 1:
        init_shop_list()
        print('Your balance:',money,'Product in your car:',car)
