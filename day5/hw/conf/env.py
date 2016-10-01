#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
import json

user_path=r'..\db\user.txt'
record_path=r'..\db\record.txt'
user_table=json.load(open(r'..\db\user.txt'))
user_record=json.load(open(r'..\db\record.txt'))
market=json.load(open(r'..\db\market.txt'))

