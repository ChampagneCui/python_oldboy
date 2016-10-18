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
    '''乘除加减'''
    req=req.strip('(')
    req = req.strip(')')
    res=eval(req)
    return res

def deal():
    expression=raw_input('请输入表达式：')
    expression='('+expression+')'
    while '('  in expression:
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


if __name__ == '__main__':
    deal()
