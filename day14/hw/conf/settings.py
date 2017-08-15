#!/usr/bin/env python
#_*_coding:utf-8_*_
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_CONN ="mysql+pymysql://root:Pass1234@localhost:3306/jpserver?charset=utf8"

init_msg='''I guess this is the first time you start JumpServer. Now what you should to do is syncdb then create_user...'''


help_msg='''
Available commands:
	 create_groups
	 start_session
	 syncdb
	 create_hosts
	 create_remoteusers
	 create_users
	 create_bindhosts
	 stop
'''

wisdom_file=r'./YAML/sentence.yml'

user_choice='''
Do you want list ungrouped hosts(H) or groups(G)?: '''