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

def get(host,src_path):
    transport = paramiko.Transport((dic[host][0], dic[host][1]))
    transport.connect(username=dic[host][2], password=dic[host][3])

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(src_path)

    transport.close()



def put(host,src_path, target_path):
    transport = paramiko.Transport((dic[host][0], dic[host][1]))
    transport.connect(username=dic[host][2], password=dic[host][3])

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(src_path, target_path)
    transport.close()