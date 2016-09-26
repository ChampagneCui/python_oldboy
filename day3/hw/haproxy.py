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
    elif num == 4:
        pass

def feature1(backend): #查看指定backend信息，思路：遇到匹配的行就把flag设为打印，然后再次遇到空行就flag设为结束
    with open(conf) as f1:
        print_flag=1
        for line in f1:
            if print_flag==0:
                print line
            if line.find('backend %s' % (backend)) >= 0:
                print_flag=0
            if print_flag==0 and line=='\n':
                print_flag=1

def feature2(backend,server): #添加，思路：如果backend已有就加在现有的下面，没有则加最后
    blank=(' '*5)
    flag=1
    with open(conf) as f1:
        with open(new_conf,'w') as f2:
            for line in f1:
                f2.write(line)
                if line.find('backend %s' %(backend)) >=0:
                    server_temp = ('%s %s \n') % (blank, server)
                    f2.write(server_temp)
                    flag=0
            if flag==1:
                f2.write('\n')
                backend_temp=('backend %s \n') %(backend)
                server_temp=('%s %s \n') %(blank,server)
                f2.write(backend_temp)
                f2.write(server_temp)
    mv()

def feature3(backend,server):#修改
    pass

def feature4(backend,server):#删除
    pass

def mv():
    os.remove(old_conf)
    os.rename(conf,old_conf)
    os.rename(new_conf,conf)

def main():
    welcome()
    choise()

if __name__ == '__main__':
    main()
