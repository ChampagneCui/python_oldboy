#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

'''
用户管理程序：
    普通用户：登陆，注册，修改密码，查看本用户信息
    管理员用户：登陆，注册，修改密码，查看本用户信息，删除，添加普通用户，修改普通用户密码，查看所有普通用户，用户信息关键字搜索，提高用户权限
    用户信息用文件
    权限用装饰器
'''

login_status={'is_login':False,'current_user':'','role':'0'}
role_key={'1':'普通用户','2':'管理员用户'}



#装饰器（用来对每一个操作都验证登陆与否以及权限）
def outer(func):
    def inner(*args,**kwargs):
        if login_status['is_login']==True:
            r=func(*args,**kwargs)
            return r
        else:
            print('请登陆！')
    return inner

#所有的管理选项，在这里普通用户和管理员用户看到的选项将会不同，普通用户无法选择管理员用户的选项，从而避免了用装饰器来判断用户角色
@outer
def manager():
    role1=('''
    1.修改密码
    2.查看本用户信息
    请输入序号：''')
    role2=('''
    1.修改密码
    2.查看本用户信息
    3.删除用户信息
    4.添加普通用户
    5.修改普通用户密码
    6.查看所有普通用户
    7.用户信息搜索
    8.管理用户权限
    请输入序号：''')
    print(' Welcome! %s') %(login_status['current_user'])
    if login_status['role']=='1':
        choice=raw_input(role1)
    elif login_status['role']=='2':
        choice=raw_input(role2)
    if choice=='1':
        new_passwd=0
        new_passwd_again=1
        while new_passwd != new_passwd_again:
            new_passwd=raw_input('请输入新密码')
            new_passwd_again=raw_input('请再次输入新密码')
        changepwd(login_status['current_user'],new_passwd)
    elif choice=='2':
        info()
    elif choice=='3' and login_status['role']=='2':
        userdel()
    elif choice=='4' and login_status['role']=='2':
        adduser()
    elif choice=='5' and login_status['role']=='2':
        user = raw_input('你要为哪个用户修改密码：')
        new_passwd = 0
        new_passwd_again = 1
        while new_passwd != new_passwd_again:
            new_passwd = raw_input('请输入新密码')
            new_passwd_again = raw_input('请再次输入新密码')
        changepwd(user, new_passwd)
    elif choice == '6' and login_status['role'] == '2':
        list_user()
    elif choice == '7' and login_status['role'] == '2':
        find_info()
    elif choice == '8' and login_status['role'] == '2':
        user = raw_input('你要为哪个用户修改权限：')
        award_permission(user)
    else:
        print('错误的选项！')

def write_result(user_dic):
    f = open('user.txt', 'w')
    for user in user_dic.keys():
        f.write(user + '|' + user_dic[user][0] + '|' + user_dic[user][1] + '|' + user_dic[user][2] + '|' +
                user_dic[user][3] + '\n')
    f.close()

#登陆
def login(user,pwd):
    if user in user_dic and pwd==user_dic[user][0]:
        login_status['is_login']=True
        login_status['role']=user_dic[user][3]
        login_status['current_user']=user
        print('登陆成功!')
    else:
        print('错误的账号或密码!')

#注册
def register():
    user=raw_input('请输入新用户名:')
    passwd = raw_input('请输入密码:')
    if user not in user_dic:
        email=raw_input('请输入email:')
        mobile=raw_input('请输入电话号码:')
        role='1'
        user_dic[user]=[passwd,email,mobile,role]
        write_result(user_dic)
    else:
        print('用户已存在!')
        register()

#修改密码
@outer
def changepwd(user,new_pwd):
    if user_dic.get(user) != None:
        user_dic[user][0] =new_pwd
        write_result(user_dic)
    else:
        print('没有该用户')

#信息
@outer
def info():
    user_info = ('''用户名:%s,
                邮箱: %s,
                手机号:%s,
                '角色:' %s''') % (
    login_status['current_user'], user_dic[login_status['current_user']][1], user_dic[login_status['current_user']][2],
    role_key[login_status['role']])
    print(user_info)


@outer
def userdel():
    user=raw_input('请输入你要删除的用户：')
    if user_dic.get(user)!=None:
        del user_dic['alox']
        write_result(user_dic)
    else:
        print('没有该用户')

@outer
def adduser():
    user = raw_input('请输入新用户名:')
    passwd = raw_input('请输入密码:')
    if user not in user_dic:
        email = raw_input('请输入email:')
        mobile = raw_input('请输入电话号码:')
        role = '1'
        user_dic[user] = [passwd, email, mobile, role]
        write_result(user_dic)
    else:
        print('用户已存在!')
        adduser()

@outer
def list_user():
    for i in user_dic:
        print(i)

@outer
def find_info():
    word=raw_input('请输入你要查询的关键字：')
    for i in user_dic.keys():
        r = ''.join(user_dic[i])
        if r.find(word) >= 0:
            user_info = ('''用户名:%s,
                            邮箱: %s,
                            手机号:%s,
                            角色: %s''') % (
                i, user_dic[i][1],
                user_dic[i][2],
                role_key[user_dic[i][3]])
            print(user_info)

@outer
def award_permission(user):
    if user_dic.get(user) != None:
        user_dic[user][3] = '2'
        write_result(user_dic)
    else:
        print('没有该用户')

def main():
    global user_dic
    while 1:
        user_dic = {}
        f = open('user.txt')
        for line in f:
            u = line.strip().split('|')
            user_dic[u[0]] = u[1:]
        f.close()
        welcome = raw_input('''
             1.管理
             2.登陆
             3.注册
             请输入序号：''')
        if welcome == '1':
            manager()
        elif welcome == '2':
            user = raw_input('请输入用户名:')
            passwd = raw_input('请输入密码:')
            login(user, passwd)
        elif welcome == '3':
            register()
        else:
            print('错误选项，请重新选择!')

if __name__ == '__main__':
    main()