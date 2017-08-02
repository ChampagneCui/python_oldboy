#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
from modules import models
from modules.db_conn import engine,session
from modules.utils import print_err,yaml_parser
from conf.settings import help_msg,wisdom_file
from modules.common import common_filters

class feature:
	@staticmethod
	def create_users(user_file):
		source = yaml_parser(user_file)
		if source:
			for key, val in source.items():
				print(key, val)
				obj = models.UserProfile(username=key, password=val.get('password'))
				if val.get('groups'):
					'''如果val中含有group，且该group存在，则同时讲该用户加入对应group'''
					groups= common_filters.bind_group_filter(val)
					obj.groups = groups
				if val.get('bind_hosts'):
					'''如果val有bind_hosts，则同时绑定hosts'''
					bind_hosts = common_filters.bind_hosts_filter(val)
					obj.bind_hosts = bind_hosts
				session.add(obj)
			session.commit()

	@staticmethod
	def syncdb():
		print("Syncing DB....")
		models.Base.metadata.create_all(engine)
		source = yaml_parser(wisdom_file)
		if source:
			for key, val in source.items():
				obj = models.Wisdom(sentence=key)
				session.add(obj)
			session.commit()

	@staticmethod
	def stop():
		pass


def usage():
	print(help_msg)