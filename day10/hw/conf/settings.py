#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import ConfigParser

#db_file=r'../db/passwd'
operation={}

group_file='../db/group'
host_file='../db/host'
#dic=eval(open(db_file).read())

gconf = ConfigParser.ConfigParser()
hconf = ConfigParser.ConfigParser()
#用config对象读取配置文件
gconf.read(group_file)
hconf.read(host_file)
#以列表形式返回所有的section
gsections = gconf.sections()
hsections = hconf.sections()

#指定section，option读取值
#str_val = conf.get("sec_a", "a_key1")



