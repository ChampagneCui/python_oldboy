#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from __future__ import division
import re


def deal_a(req):
    '''re.sub替换前加转义符'''
    for i in req:
        res=re.sub('\(','\\(',req)
        res = re.sub('\)', '\\)', res)
        res = re.sub('\+', '\\+', res)
        res = re.sub('\-', '\\-', res)
        res = re.sub('\*', '\\*', res)
        res = re.sub('\/', '\\/', res)
    return res

def cal(req):
    '''除乘减加顺序计算'''
    req=req.strip('(')
    req = req.strip(')')
    res=eval(req)
    return res

def deal():
    '''剥离括号函数，即寻找括号内不再包含括号的运算式，然后计算并替换，如此往复'''
    expression=raw_input('请输入表达式：')
    expression='('+expression+')'
    while ('('  in expression) or (')'  in expression):
        if ('(' in expression and ')' not in expression) or ('(' not in expression and ')' in expression):
            exit('Input error!')
        else:
            a=re.findall('\([^()]*\)',expression)
            a=a[0]
            b=str(cal(a))
            a=deal_a(a)
            expression=re.sub(a,b,expression,1)
            #print expression
    print expression

#处理异常没做

if __name__ == '__main__':
    deal()
