#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #返回脚本绝对路径



DB_CONN ="mysql+pymysql://root:Pass1234@localhost:3306/little_finger?charset=utf8"

'''
# Database
DATABASES = {
    'default': {
        'ENGINE': 'mysqldb',
        'NAME': 'LittleFinger',
        'HOST': '',
        'PORT':3306,
        'USER':'root',
        'PASSWORD': ''
    }
}
'''

