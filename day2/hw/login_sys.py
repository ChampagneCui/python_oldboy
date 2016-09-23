#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_


user_table=open('f.txt').read()
user_table=eval(user_table)

def iflock(u):
    if u in user_table.keys():
        info=user_table[u]
        if info[2]=='y':
            print('You have been locked! Please contact to system admin.')
            return 1
        else:
            return 0
    else:
        return 0


def login(u,p):
    if u in user_table.keys():
        info=user_table[u]
        if info[0] == p:
            print('Welcome Login!')
            f = open('f.txt', 'w')
            user_table[u][1]=0
            result = user_table
            f.write(str(result))
            f.close()
            return 0
        else:
            f=open('f.txt','w')
            print('username or password wrong!')
            user_table[u][1]=int(user_table[u][1])+1
            if user_table[u][1] >=3 :
                user_table[u][2]='y'
            result=user_table
            f.write(str(result))
            f.close()
            return 1
    else:
        print('No such user!')
        ask = raw_input('Do you want sign up a new acount?(y/n)')
        if ask == 'y':
            f = open('f.txt', 'w')
            uu = raw_input('Please enter new username:')
            pp = raw_input('Passwd:')
            if uu in user_table.keys():
                print('Username alread exist.')
            else:
                user_table[uu] = [pp, 0, 'n']
            result = user_table
            f.write(str(result))
            f.close()
            print('Successful!')
        return 1


