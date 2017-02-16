#!/usr/bin/env python3
#_*_coding:utf-8_*_

import socket
import sys
import json

server_address = ('localhost', 10000)

# Create a TCP/IP socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

class feature:
	@staticmethod
	def ls(*args,**kwargs):
        	msg_data = {'action': 'ls'}
		c.send(bytes(json.dumps(msg_data)))
		list=eval(s.recv(4096))
		i=0
		try:
			while i < len(list):
			print(list[i])
			i+=1
		except:
			print('nothing!')

def main():
	while True:
    		send_data=bytes(input(">>:"),encoding="utf-8")
		if len(send_data)==0:continue
		cmd_list=send_data.split()
		task_type=cmd_list[0]
		if len(cmd_list)<2 and task_type !='ls':continue
		if hasattr(feature, task_type):
        		func=getattr(feature, task_type)
        		func(cmd_list)
		else:
			print("doesn't support type.")
		continue
    		#s.sendall(msg)
    		#data=s.recv(1024)
    		#print(data)
	s.close()

if __name__=='__main__':
	server_address = ('localhost', 10000)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(server_address)

	main()
