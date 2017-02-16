#!/usr/bin/env python3
#_*_coding:utf-8_*_
import socket
import selectors
import os,sys
import json


class feature:
	@staticmethod
	def ls(data,conn):
		list=os.listdir('./')
		conn.send(bytes(json.dumps(list),encoding='utf-8'))

	@staticmethod
	def get(data,conn):
		pass

	@staticmethod
	def put(operation,i):
		pass
