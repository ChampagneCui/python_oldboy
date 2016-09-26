#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_


conf='haproxy.cfg'
new_conf='haproxy.cfg.new'

'''
HAproxy配置文件操作
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
'''


def choise():
    num=raw_input('请输入操作序号：')
    while num.isdigit() != True:
        num=raw_input('请输入操作序号：')
    num = int(num)
    while num>4 :
        num = raw_input('请输入操作序号：')
    choise(num)

def haproxy_conf(num):
    if num==1:
        pass
    elif num==2:
        pass
    elif num==3:
        pass
    elif num == 4:
        pass

def feature1(backend): #查看指定backend信息
    pass

def feature2(backend,server): #添加
    pass

def feature3(backend,server):#修改
    pass

def feature4(backend,server):#删除
    pass

def main():
    with open(conf,'r') as f1:
        with open(new_conf,'w') as f2:
            for i in f1:
                f2.write(i)

if __name__ == '__main__':
    main()
