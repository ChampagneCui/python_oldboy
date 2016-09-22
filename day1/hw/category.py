#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import re

def init(): ##初始化
	global parent
	parent='0'
	for i in open('map.txt') :
		i=i.strip('\n')
		i=i.split(' ')
		if int(i[0])<10:#显示10以内的地域名，默认为最高级
			print i[0][-1],i[1]

def ifexist(parent): #判断选项是否存在，不在就返回1
	f = open('map.txt', 'r').read()
	a=re.split('\n| ',f) #import了re函数，可以多个字符过滤
	if parent in a:
		return 0
	else:
		return 1

		
def choose(parent): #返回choose结果
	 for i in open('map.txt') :
                i=i.strip('\n')
                i=i.split(' ')
		if i[0][0:-1]==parent:
			print i[0][-1],i[1]
	
if __name__ == '__main__':
	init()
	while 1:
		choice=raw_input('---->')
		while choice=='':
			choice=raw_input('---->')
		if choice=='q':
			init()
		elif choice =='b':
			if parent!='0' :
				parent=str(parent[0:-1])
				choose(parent)
			else:
				print('This is the edge! Please choose again!')
		else:
			old=parent
			parent=str(parent)+choice
			if ifexist(parent) == 0:
				choose(parent)
			else:
				parent=old
				print('Wrong! Choose again!')
