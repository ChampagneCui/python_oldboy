#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
from modules import models
from modules.db_conn import engine,session
from modules.utils import print_err,yaml_parser
from conf.settings import help_msg,wisdom_file

class feature:
	def create_users(self,user_file):
		source = yaml_parser(user_file)
		print(source)
		if source:
			pass

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


def usage():
	print(help_msg)