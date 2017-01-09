#!/usr/bin/env python2.7
#_*_coding:utf-8_*_


from sys import path
path.append(r'../conf')
from settings import *
import paramiko


def ssh_command(host,command):
    transport = paramiko.Transport((dic[host][0], dic[host][1]))
    transport.connect(username=dic[host][2], password=dic[host][3])

    ssh = paramiko.SSHClient()
    ssh._transport = transport

    stdin, stdout, stderr = ssh.exec_command(command)
    print stdout.read()

    transport.close()