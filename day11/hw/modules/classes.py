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
	def put(data,conn):
		conn.send(bytes('True',encoding='utf-8'))
		filesize = data["filesize"]
		filename = data["filename"]
		print(filename, filesize)
		f = open(filename, 'wb')
		recv_size = 0
		while filesize > recv_size :
			data = conn.recv(4096)
			f.write(data)
			recv_size += len(data)
		print('file recv success')
		f.close()

