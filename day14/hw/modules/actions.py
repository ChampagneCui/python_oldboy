#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
from modules import models
from modules.db_conn import engine,session
from modules.utils import print_err,yaml_parser
from conf.settings import help_msg,wisdom_file
from modules import common

def auth():
	while 1:
		user=input('Please enter your username:')
		if user=='exit':
			exit()
		passwd=input('passwd:')
		user_obj = session.query(models.UserProfile).filter(models.UserProfile.username == user,
															models.UserProfile.password == passwd).first()
		if user_obj:
			return user_obj
		else:
			print("Wrong username or password.")

class feature:
	@staticmethod
	def create_users(user_file):
		source = yaml_parser(user_file)
		if source:
			for key, val in source.items():
				print(key, val)
				obj = models.UserProfile(username=key, password=val['password'])
				if val.get('groups'):
					'''如果val中含有group，且该group存在，则同时讲该用户加入对应group'''
					groups= common.bind_group_filter(val)
					obj.groups = groups
				if val.get('bind_hosts'):
					'''如果val有bind_hosts，则同时绑定hosts'''
					bind_hosts = common.bind_hosts_filter(val)
					obj.bind_hosts = bind_hosts
				session.add(obj)
			session.commit()

	@staticmethod
	def create_groups(group_file):
		source = yaml_parser(group_file)
		if source:
			for key, val in source.items():
				print(key, val)
				obj = models.Group(name=key)
				if val.get('user_profiles'):
					user_profiles = common.user_profiles_filter(val)
					obj.user_profiles = user_profiles
				if val.get('bind_hosts'):
					bind_hosts = common.bind_hosts_filter(val)
					obj.bind_hosts = bind_hosts
				session.add(obj)
			session.commit()

	@staticmethod
	def create_hosts(host_file):
		source = yaml_parser(host_file)
		if source:
			for key, val in source.items():
				print(key, val)
				obj = models.Host(hostname=key,ip_addr=val['ip_addr'], port=val.get('port') or 22)
				session.add(obj)
			session.commit()

	@staticmethod
	def create_bindhosts(bindhost_file):
		source = yaml_parser(bindhost_file)
		if source:
			for key,val in source.items():
				host_obj=session.query(models.Host).filter(models.Host.hostname==val['hostname']).first()
				#print(host_obj.id)
				for item in val['remote_users']:
					print(item)
					if item['auth_type'] == 'ssh-key':
						remoteuser_obj=session.query(models.RemoteUser).filter(models.RemoteUser.username==item['username'],models.RemoteUser.auth_type=='ssh-key').first()
					elif item['auth_type'] == 'ssh-passwd':
						remoteuser_obj=session.query(models.RemoteUser).filter(models.RemoteUser.username==item['username'],models.RemoteUser.password==item['password']).first()
					print(remoteuser_obj.id)
					if (not host_obj) or (not remoteuser_obj):
						print('There is something error between hostname or remote_user.')
						continue
					bindhost_obj = models.BindHost(host_id=host_obj.id, remoteuser_id=remoteuser_obj.id)
					session.add(bindhost_obj)
				if val['groups']:
					for item in val['groups']:
						group_obj = session.query(models.Group).filter(models.Group.name.in_(item )).all()
						bindhost_obj.groups = group_obj
				if val['user_profiles']:
					for item in val['user_profiles']:
						userprofile_obj=session.query(models.UserProfile).filter(models.UserProfile.username.in_(item)).all()
						bindhost_obj.user_profiles = userprofile_obj

			session.commit()

	@staticmethod
	def create_remoteusers(remoteuser_file):
		source = yaml_parser(remoteuser_file)
		if source:
			for key, val in source.items():
				print(key, val)
				obj = models.RemoteUser(username=val['username'], auth_type=val['auth_type'],
										password=val.get('password'))
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

	@staticmethod
	def start_session():
		user = auth()
		if user:
			print('Hello %s!' %(user.username))
			#print(user.bind_hosts)
			#print(user.groups)
			exit_flag = False
			while not exit_flag:
				choice=input(user_choice)
				if choice=='H':
					print(user.bind_hosts)
				elif choice=='G':
					print(user.groups)
				else:
					continue



def usage():
	print(help_msg)