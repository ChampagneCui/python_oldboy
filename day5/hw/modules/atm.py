#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import logging
import logging.config
CONF_LOG = "../conf/logging.conf"
logging.config.fileConfig(CONF_LOG)

def login_bank():
    '''登录atm'''
    pass

def budget():
    '''额度查询'''
    pass

def get_cash():
    '''提取现金'''
    pass

def forward_money():
    '''转账'''
    pass

def check_detail():
    '''查流水账'''
    pass

def pay():
    '''付费'''
    pass

def manager():
    '''管理接口，包括添加账户、用户额度，冻结账户'''
    pass