#!/usr/bin/env python3
#_*_coding:utf-8_*_

import socket
import os,sys
import json
import platform

def isWindowsSystem():
    return 'Windows' in platform.system()

server_address = ('localhost', 10000)

# Create a TCP/IP socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

class feature:
	@staticmethod
	def ls(*args,**kwargs):
		msg_data = {'action': 'ls'}
		s.send(bytes(json.dumps(msg_data),encoding='utf-8'))
		list=json.loads(s.recv(4096).decode())
		i=0
		try:
			while i < len(list):
				print(list[i])
				i+=1
		except:
			print('nothing!')

	@staticmethod
	def put(cmd_list):
		abs_filepath = cmd_list[1]
		if os.path.isfile(abs_filepath):
			file_size = os.stat(abs_filepath).st_size
			filename = abs_filepath.split(separator)[-1]
			print(type(abs_filepath), type(file_size))
			print('file:',abs_filepath, 'size:',file_size)
			msg_data = {'action': 'put', 'filename': filename, 'filesize': file_size}
			s.send(bytes(json.dumps(msg_data),encoding='utf-8'))

			if s.recv(1024).decode() == 'True':
				print('start sending file', filename)
				# f = open(abs_filepath, 'rb')
				size = 0
				with open(abs_filepath, 'rb') as f:
					while file_size - size > 4096:
						send_data = f.read(4096)
						s.send(send_data)
						size += 4096
						continue
					else:
						s.send(f.read(file_size - size))


				print('send file done')
		else:
			print("file %s is not exist") % (abs_filepath)

	@staticmethod
	def fget():
		pass


def main():
	while True:
		send_data=input(">>:")
		if len(send_data)==0:continue
		cmd_list=send_data.split()
		task_type=cmd_list[0]
		#if len(cmd_list)<2 and task_type !='ls':continue
		if hasattr(feature,task_type):
			func=getattr(feature,task_type)
			func(cmd_list)
		else:
			print("doesn't support type.")
		continue
		#s.sendall(msg)
		#data=s.recv(1024)
		#print(data)
	s.close()

if __name__=='__main__':
	if isWindowsSystem == True:
		separator = '\\'
	else:
		separator = '/'
	server_address = ('localhost', 10000)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(server_address)

	main()
