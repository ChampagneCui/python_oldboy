#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import os


conf='haproxy.cfg'
new_conf='haproxy.cfg.new'
old_conf='haproxy.cfg.old'

def welcome():
    print('''
    HAproxy配置文件操作
    1. 查询backend信息
    2. 可添加backend 和sever信息
    3. 可修改backend 和sever信息
    4. 可删除backend 和sever信息
    6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
    ''')


def choise():
    num=raw_input('请输入操作序号：')
    while num.isdigit() != True:
        num=raw_input('请输入操作序号：')
    num = int(num)
    while num>4 :
        num = raw_input('请输入操作序号：')
    haproxy_conf(num)

def haproxy_conf(num):
    if num==1:
        a=raw_input('Which backend do you want to see?')
        feature1(a)
    elif num==2:
        a=raw_input('Please enter the backend name:')
        b=raw_input('Please enter the server information:')
        feature2(a,b)
    elif num==3:
        pass
    elif num ==4:
        a = raw_input('Please enter the backend name:')
        b = raw_input('Please enter the server information:')
        feature4(a, b)

def public(backend): #查看指定backend信息，思路：遇到匹配的行就把flag设为打印，然后再次遇到空行就flag设为结束
    global result
    result=[]
    with open(conf) as f1:
        print_flag=1 #1表示不输出，0表示输出
        for line in f1:
            if print_flag==0 and line=='\n':
                print_flag=1
            if print_flag==0:
                result.append(line.strip())
            if line.find('backend %s' % (backend)) >= 0:
                print_flag=0
    return result

def feature1(backend):
    if public(backend) != []:
        for i in result:
            print(i)
    else:
        print('Find nothing!')

def feature2(backend,server): #添加，思路：如果backend已有就加在现有的下面，没有则加最后
    blank=(' '*6)
    if public(backend)!=[]: #backend存在
        result_list=[]
        for i in result:
            new=i.split(' ')
            result_list+=new
        server_list=server.split(' ')
        server_ip=server_list[2]
        if server_ip in result_list: #server_ip已存在
            print('Already existed!')
        else:
            with open(conf) as f1:
                with open(new_conf,'w') as f2:
                    for line in f1:
                        f2.write(line)
                        if line.find('backend %s' % (backend)) >= 0:
                            server_temp = ('%s %s \n') % (blank, server)
                            f2.write(server_temp)
            mv()
    else: #原本backend也不存在
        with open(conf) as f1:
            with open(new_conf, 'w') as f2:
                for line in f1:
                    f2.write(line)
                f2.write('\n')
                backend_temp = ('backend %s \n') % (backend)
                server_temp = ('%s %s \n') % (blank, server)
                f2.write(backend_temp)
                f2.write(server_temp)
        mv()

def feature3(backend,server):#修改
    pass

def feature4(backend,server):#删除
    flag=1
    if public(backend) != []:  # backend存在
        result_list = []
        for i in result:
            new = i.split(' ')
            result_list += new
        server_list = server.split(' ')
        server_ip = server_list[2]
        if server_ip in result_list:  # server_ip已存在
            with open(conf) as f1:
                with open(new_conf, 'w') as f2:
                    for line in f1:
                        if line.find('backend %s' % (backend)) >= 0:
                            flag=0
                        if flag==0 and line.find(server_ip)>=0:
                            flag=1
                            continue
                        f2.write(line)
            mv()
        else:
            print('No such server in backend:%s') %(backend)
    else:
        print('No such backend!')

def mv():
    if os.path.exists(old_conf)==True:
        os.remove(old_conf)
    os.rename(conf,old_conf)
    os.rename(new_conf,conf)

def main():
    welcome()
    choise()

if __name__ == '__main__':
    main()
