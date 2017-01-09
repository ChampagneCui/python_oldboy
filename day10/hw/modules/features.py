#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

path.append(r'../conf')
from settings import *
import paramiko


transport = paramiko.Transport(('10.25.23.219', 22))
transport.connect(username='root', password='Pass1234')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df -H')
print stdout.read()

transport.close()