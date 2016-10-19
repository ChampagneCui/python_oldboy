#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from __future__ import division
#bug:目前有个很大的bug，不能精确到小数点，因为如果采用小数点计算，正则的\d没法识别
import re

def check(req):
    '''检查有没有除括号数字加减乘除以外的东西'''
    if re.findall('[^\(\)\+\-\*\/\d]',req) ==[]:
        return 1
    else:
        return 0

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

def sign(req):
    '''判断正负，单数减号即为负，return 1，双数减号为正'''
    expression=re.findall('\-', req)
    if len(expression)%2==0:
        return 0
    else:
        return 1

def cal(req):
    '''除乘减加顺序计算,这样不用考虑位置'''
    while re.findall('/',req)!=[]:
        a=re.findall('\d+\.?\d*/\-*\d+\.?\d*',req)
        a=a[0]
        num=re.findall('\d+\.?\d*',a)
        res=str(float(num[0])/float(num[1]))
        if sign(a)==0:
            res=res
        else:
            res='-'+res
        a=deal_a(a)
        req=re.sub(a,res,req,1)
    while re.findall('\*', req) != []:
        a = re.findall('\d+\.?\d*\*\-*\d+\.?\d*', req)
        a = a[0]
        num = re.findall('\d+\.?\d*', a)
        res = str(float(num[0]) * float(num[1]))
        if sign(a) == 0:
            res = res
        else:
            res = '-' + res
        a = deal_a(a)
        req = re.sub(a,res,req,1)
    num = re.findall('\+*\-*\+*\d+\.?\d*', req)
    while len(num) > 1:
        a = eval(num[0])
        b = eval(num[1])
        num[0] = str(a + b)
        del (num[1])
    return num[0]

def deal():
    '''剥离括号函数，即寻找括号内不再包含括号的运算式，然后计算并替换，如此往复'''
    expression=raw_input('请输入表达式：')
    if check(expression)==0:
        print('Input error!')
        deal()
    else:
        expression = '(' + expression + ')'
        while ('('  in expression) or (')'  in expression):
            if ('(' in expression and ')' not in expression) or ('(' not in expression and ')' in expression):
                exit('Input error!')
            else:
                a=re.findall('\([^()]*\)',expression)
                a=a[0]
                b=str(cal(a))
                a=deal_a(a)
                expression=re.sub(a,b,expression,1)
        print expression


if __name__ == '__main__':
     deal()
