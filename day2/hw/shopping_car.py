#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

import time
import copy
from login_sys import iflock
from login_sys import login

user_tables=open('f.txt').read()
user_tables=eval(user_tables)
user_record=open('record.txt').read()
user_record=eval(user_record)
market=open('market.txt').read()
market=eval(market)

car=[] #购物车
welcome_msg='welcome to market!'.center(50,'*')
p_sort={} #用来记录分类与number的关系
p_sort1={} #用来记录分类下各物品与number的关系

def init():
    global money
    for u in user_tables.keys():
        if u==username :
            if user_tables[u][3]==0:
                money = raw_input('Please enter your salary:')
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
    global summary
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
    global parent
    global choice
    global p_sort
    for i in enumerate(market):
        index = i[0]
        p_product = i[1]
        print(index, p_product)
        p_sort[index] = p_product
    parent = '0'
    choice = raw_input('Please enter your choice(\'q\' to exit):')

def shop_list(choice):
    global parent
    global p_sort1
    global market1
    if choice=='q':
        clearing()
    elif choice=='b':
        init_shop_list()
        shop_list(choice)
    elif check_num(choice)==0:
        if int(choice)<=len(p_sort):
            if parent=='0':
                market1=market[p_sort[int(choice)]]
                for i in enumerate(market1):
                    index = i[0]
                    p_product = i[1]
                    p_price = market1[i[1]]
                    print(index, p_product, p_price)
                    p_sort1[index]=p_product
                parent+=str(choice)
        else:
            print('Wrong num!')
            init_shop_list()
            shop_list(choice)
    else:
        print('Wrong num!')
        #choice1 = raw_input('Please enter your choice(\'q\' to exit|\'b\' to back!):')
        init_shop_list()
        shop_list(choice)

def shopping(num,quantity):
    global car
    global money
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
    init_shop_list()
    while 1:
        shop_list(choice)
        ###bug
        choice=raw_input('What do you want to buy?(You can enter \'q\' to exit and \'b\' to back to last menu!)')
        if choice=='q':
            clearing()#结算
        elif choice=='b':
            init_shop_list()
            continue
        quantity=raw_input('How many do you want?')
        while ((check_num(choice)==1 and (choice!='q' or choice!='b')) or check_num(quantity)==1):
            choice = raw_input('What do you want to buy?(You can enter \'q\' to exit and \'b\' to back to last menu!)')
            quantity = raw_input('How many do you want?')
        choice=int(choice)
        quantity=int(quantity)
        ####bug
        shopping(choice,quantity)
        print('Your balance:',money,'Product in your car:',car)
        #以上打上##bug标注的这段很不满意，但不知道该如何修，这里会产生很多bug，但没有思路修
        #不将choice判断q，b这段写入shopping函数是因为，希望用户输入choice后可以直接进行结算或退到上一层，而不用再输无意义的quantity


