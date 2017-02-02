#!/usr/bin/env python2.7
#_*_coding:utf-8_*_


from sys import path
path.append(r'../conf')
from settings import *
import paramiko
import ConfigParser





class feature:
    @staticmethod
    def ssh_command(operation,ip,port,username,password):
        transport = paramiko.Transport((ip,port ))
        transport.connect(username=username,password=password )
        ssh = paramiko.SSHClient()
        ssh._transport = transport
        stdin, stdout, stderr = ssh.exec_command(operation[command])
        print stdout.read()
        transport.close()

    @staticmethod
    def get(operation,ip,port,username,password):
        transport = paramiko.Transport((ip,port))
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(operation[src])

        transport.close()

    @staticmethod
    def put(operation,ip,port,username,password):
        transport = paramiko.Transport((ip, port))
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(operation[src], operation[dest])
        transport.close()
