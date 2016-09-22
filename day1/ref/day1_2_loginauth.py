# -*- coding:utf-8 -*-
"""
__author: super
"""

import os
import json
import getpass
from datetime import datetime

# 存放所有用户信息列表变量
USER_INFO = []
# 存放登陆成功的用户名
LOGIN_USER = ""
# 存放登陆用户的权限，初始值为'admin'
LOGIN_USER_ROLE = "admin"
# 允许输入错误的最大次数
LOGIN_MAX_ERR_COUNT = 3
# 存放用户信息的文件
DB_TXT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'userinfo.txt')


# 初始化数据，将文件中的数据加载到全局变量中
def init_data():
    with open(DB_TXT_FILE, 'r') as f:
        for record in f.readlines():
            user_info = json.loads(record.strip())
            USER_INFO.append(user_info)

    return USER_INFO


# 管理员权限的显示菜单
def get_admin_menus():
    menu_list = (
        {'key': '1', 'menu': '[1] search  users ', 'function': 'user_search'},
        {'key': '2', 'menu': '[2] add new users ', 'function': 'user_add'},
        {'key': '3', 'menu': '[3] delete  users ', 'function': 'user_del'},
        {'key': '4', 'menu': '[4] unlock  users ', 'function': 'user_unlock'},
        {'key': '5', 'menu': '[5] exit system ', 'function': 'exit_sys'},
    )
    return menu_list


# 普通用户权限的显示菜单
def get_user_menus():
    menu_list = (
        {'key': '1', 'menu': '[1] search  users ', 'function': 'user_search'},
        {'key': '2', 'menu': '[2] modify password ', 'function': 'user_modify_passwd'},
        {'key': '5', 'menu': '[5] exit system ', 'function': 'exit_sys'},
    )
    return menu_list


# 根据输入的按键返回函数名称 ,如果选择按键不存在则返回False
def return_function_by_menu(menu_list):
    print("========= Choose Menu ========== \n")
    for menu in menu_list:
        print(menu['menu'])
    choose = raw_input('choose what do yo want to do :')
    # 获取要执行的函数名称
    for keys in menu_list:
        if keys['key'] == choose:
            return keys['function']
    else:
        print('\n\033[1;31m Error choose\033[0m')
        return False


# 查找用户模块，
def user_search():
    print("\n======== Search Users =============\n")
    name = raw_input("Input user name to search [\033[1;30mEnter\033[0m to show all] :").strip().lower()
    if len(name) > 0:
        print_search_user_info(name)
    else:
        print_all_user()
    return True


# 打印所有用户信息
def print_all_user():
    for user in USER_INFO:
        print('name: %-25s | user role:%-7s | create time: %s | lockstatus: %s \n' % (
                user['name'], user['userrole'], user['createtime'], user['islocked'])).strip()
    return True


# 打印查询到的用户数据，并高亮显示
def print_search_user_info(name):
    search_user = name
    i = 0
    record_count = 0

    # 开始在用户信息列表中循环查找
    while i < len(USER_INFO):
        user = USER_INFO[i]
        # 如果记录的用户包含要查找的名字
        if user['name'].count(search_user) > 0:
            name = user['name'].replace(search_user, '\033[1;31m' + search_user + '\033[0m')  # 高亮显示
            role = user['userrole']
            cdate = user['createtime']
            lockstat = user['islocked']
            print('name: %-25s | user role:%-7s | create time: %s | lockstatus: %s \n' % (
                name, role, cdate, lockstat)).strip()
            record_count += 1  # 找到记录数
        i += 1
    print('\n%s records found ' % str(record_count))


# 判断用户是否存在(True / False)
def check_user_is_exists(user_name):
    i = 0
    user_exists_status = False
    while i < len(USER_INFO):
        user = USER_INFO[i]
        if user['name'] == user_name:
            user_exists_status = True
            break
        else:
            i += 1
    return user_exists_status


# 添加用户模块
def user_add():
    # 添加完1个用户后是否继续添加标志
    add_more_flag = True

    print('====== Add New Users ===========')
    while add_more_flag:
        name = ""
        password = ""
        # 如果输入用户名为空则不停让输入，直到输入不为空
        while len(name) == 0:
            name = raw_input("username: ").strip().lower()
        # 如果输入密码为空则继续输入
        while len(password) == 0:
            password = raw_input("password: ").strip()
        # 选择用户角色
        role = raw_input("user role number[1:admin / 2:user(default)]: ")
        if len(role) == 0 or role == "2":
            user_role = "user"
        if role == "1":
            user_role = "admin"
        # 组合数据为字典
        user_info_dic = {"createtime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "password": password, "name": name,
                         "userrole": user_role, "islocked": "0"}
        USER_INFO.append(user_info_dic)
        save_data()
        # 继续添加吗?
        continue_flag = raw_input('add user successfull, add more?(Y/N)').strip().lower()
        if continue_flag == 'n':
            add_more_flag = False


# 删除用户模块
def user_del():
    print("========== Delete Users ==========\n")
    name = ""
    while len(name) == 0:
        name = raw_input("input the user name you want to delete:").strip().lower()
    # 检查用户是否存在
    is_exists = check_user_is_exists(name)
    if is_exists:
        i = 0
        while i < len(USER_INFO):
            if USER_INFO[i]["name"] == name:
                USER_INFO.remove(USER_INFO[i])
                save_data()
                print("\033[1;32m\nuser %s delete successfull !\033[0m" % name)
                break
            else:
                i += 1
    else:
        print("\033[1;31m\nThe user %s does not exists!\033[0m" % name)


# 修改用户密码模块
def user_modify_password():
    print("========== Modify User's Password ==========\n")
    i = 0
    flag = True
    while flag:
        new_password = getpass.getpass('input new password: ')
        confirm_passwod = getpass.getpass('input confirm password:').strip()
        # 如果两次密码一样的话
        if new_password == confirm_passwod:
            while i < len(USER_INFO):
                if USER_INFO[i]['name'] == LOGIN_USER:
                    USER_INFO[i]['password'] = new_password
                    save_data()
                    flag = False
                    print(" password change success. \n")
                    break
                i += 1
        else:
            print('new password and confirm password does not match! try again\n')


# 锁定账户模块
def user_lock():
    i = 0
    while i < len(USER_INFO):
        if USER_INFO[i]["name"] == LOGIN_USER:
            USER_INFO[i]['islocked'] = "1"
            save_data()
            break
        else:
            i += 1


# 解锁用户模块
def user_unlock():
    print("======== Unlock Users ============\n")
    unlock_user = raw_input("input the user name to be unlock:").strip().lower()
    i = 0
    while i < len(USER_INFO):
        if USER_INFO[i]["name"] == unlock_user:
            USER_INFO[i]['islocked'] = "0"
            save_data()
            print("unlock success ")
            break
        else:
            i += 1
    else:
        print("no user called %s found!" % unlock_user)


# 将内存的数据写入文件
def save_data():
    i = 0
    try:
        with open(DB_TXT_FILE, 'w+') as f:
            while i < len(USER_INFO):
                user = json.dumps(USER_INFO[i])
                f.write(user + "\n")
                i += 1
    except Exception as e:
        print(e.message)


# 用户登录
def user_login():
    try_failed_count = 0  # 重试失败次数
    print("========= Login system ===========\n")
    while try_failed_count < LOGIN_MAX_ERR_COUNT:
        i = 0
        uname = raw_input('user name:').strip().lower()
        upasswd = getpass.getpass('password: ').strip()
        while i < len(USER_INFO):
            # 如果找到搜索的用户
            if USER_INFO[i]['name'] == uname:
                LOGIN_USER = uname
                # 如果正确，检查用户是否锁定，如果锁定
                if USER_INFO[i]['islocked'] == "1":
                        print("Sorry,your accout is locked,contact administrator to unlock")
                        exit()
                else:
                    # 用户存在，检查输入密码是否正确
                    if USER_INFO[i]['password'] == upasswd:
                        LOGIN_USER_ROLE = USER_INFO[i]['userrole']
                        print("\033[1;32m\nwelcome %s!\033[0m" % uname)
                        return True
                        # 用户正确，密码验证失败
                    else:
                        print("login failed,name and password is not avaible,try again!")
                        try_failed_count += 1
                        break
            # 没找到? 下一条继续找...
            else:
                i += 1
        # 搜索一圈都没有找到搜索的用户
        else:
            print("user does not found! try again.")

    else:
        # 密码超过3次啦,账户要锁定了
        user_lock()
        print('sorry , you try more then 3 times, i locked  this account!')
        return False


if __name__ == "__main__":
    init_data()

    if user_login():
        # 根据用户角色加载菜单
        if LOGIN_USER_ROLE == "admin":
            menu_list = get_admin_menus()
        if LOGIN_USER_ROLE == "user":
            menu_list = get_user_menus()
            # 根据菜单选择执行函数
        while True:
            func = False
            while not func:
                func = return_function_by_menu(menu_list)

            if func == "user_search":
                user_search()
            elif func == "user_add":
                user_add()
            elif func == "user_del":
                user_del()
            elif func == "user_modify_passwd":
                user_modify_password()
            elif func == "user_unlock":
                user_unlock()
            elif func == "exit_sys":
                exit()
