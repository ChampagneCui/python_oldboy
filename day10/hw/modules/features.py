#!/usr/bin/env python2.7
#_*_coding:utf-8_*_


from sys import path
path.append(r'../conf')
from settings import *
import paramiko

class feature:
    def ssh_command(username,hostname,port,command):
        if username == '':
            username=default_user
        if port=='':
            port=default_port
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=dic[host][3])
        ssh = paramiko.SSHClient()
        ssh._transport = transport
        stdin, stdout, stderr = ssh.exec_command(command)
        print stdout.read()
        transport.close()

    def get(username,hostname,port,src_path):
        if username == '':
            username = default_user
        if port == '':
            port = default_port
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=dic[host][3])

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(src_path)

        transport.close()



    def put(username,hostname,port,src_path, target_path):
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=dic[host][3])

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(src_path, target_path)
        transport.close()