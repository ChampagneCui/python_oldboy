#!/usr/bin/env python3
#_*_coding:utf-8_*_
import socket
import selectors
import os,sys
import json
import time


class feature:
	@staticmethod
	def ls(data,conn):
		list=os.listdir('./')
		conn.send(bytes(json.dumps(list),encoding='utf-8'))

	@staticmethod
	def fget(data,conn):
		file = data["file"]
		if os.path.isfile(file):
			filesize = os.stat(file).st_size
			msg_data = json.dumps({'filesize': filesize})
			conn.send(bytes(msg_data,encoding='utf-8'))
			print('start sending file', file)
			time.sleep(0.5)
			size = 0
				# f = open(abs_filepath, 'rb')
			with open(file, 'rb') as f:
				while filesize > size:
					send_data = f.read(4096)
					conn.send(send_data)
					size += 4096
			print('send file done')
		else:
			conn.send(bytes('No such file!'))


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

