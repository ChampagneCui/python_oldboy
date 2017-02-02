#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import ConfigParser

#db_file=r'../db/passwd'
operation={}
example='''Example: fabric --group="testgroup" --mode="shell" --command="ls -al"
                   fabric --host="host1" --mode="put" --src="/tmp/1.txt" --dest="/tmp/test.txt"'''

group_file='../db/group'
host_file='../db/host'

gconf = ConfigParser.ConfigParser()
hconf = ConfigParser.ConfigParser()
#用config对象读取配置文件
gconf.read(group_file)
hconf.read(host_file)
#以列表形式返回所有的section
gsections = gconf.sections()
hsections = hconf.sections()





