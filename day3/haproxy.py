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


def choise()
    




def main():
    with open(conf,'r') as f1:
        with open(new_conf,'w') as f2:
            for i in f1:
                f2.write(i)

if __name__ == '__main__':
    main()
