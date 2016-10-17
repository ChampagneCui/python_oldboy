#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import re

def cal(req):
    '''乘除加减'''
    req=req.strip('(')
    req = req.strip(')')
    res=eval(req)
    return res

def deal():
    #expression=raw_input('请输入表达式：')
    expression='1+2*(2+(3+2))+2*(3+4)'
    expression='('+expression+')'
    #while 1:
    a=re.findall('\([^()]*\)',expression)
    a=a[0]
    b=str(cal(a))
    expression=re.sub(a,b,expression,1)
    print expression

deal()

