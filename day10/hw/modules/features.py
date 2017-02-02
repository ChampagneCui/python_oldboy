#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

from sys import path
path.append(r'../conf')
from settings import *
import paramiko

def show_group():
    print(gsections)

def show_host():
    print(hsections)

def usage():
    print(example)

def get_host_info(operation):
    if "group" in operation.keys():
        group_name = operation["group"]
        host_list = gconf.get(group_name, "host")
        return host_list
    elif "host" in operation.keys():
        host_list = []
        host = operation["host"]
        host_list.append(host)
        return host_list

def get_info(host):
    ip = hconf.get(host, "ip")
    port = int(hconf.get(host, "port"))
    username = hconf.get(host, "username")
    password = hconf.get(host, "password")
    return ip,port,username,password

class feature:
    @staticmethod
    def shell(operation,i):
        if ("command" in operation.keys()):
            host_list = get_host_info(operation)
            ip,port,username,password=get_info(host_list[i])
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip, port=port, username=username, password=password)
            stdin, stdout, stderr = ssh.exec_command(operation["command"])
            if (stdout.read() ==''):stdout=stderr
            print(stdout.read())
            ssh.close()
        else:
            print('No command!')

    @staticmethod
    def get(operation,i):
        if ("src" in operation.keys() and "dest" in operation.keys()):
            host_list = get_host_info(operation)
            ip, port, username, password = get_info(host_list[i])
            transport = paramiko.Transport((ip,int(port)))
            transport.connect(username=username, password=password)

            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.get(operation["src"],operation["dest"])
            transport.close()
        else:
            print('Lack of src or dest!')

    @staticmethod
    def put(operation,i):
        if ("src" in operation.keys() and "dest" in operation.keys()):
            host_list = get_host_info(operation)
            ip, port, username, password = get_info(host_list[i])
            transport = paramiko.Transport((ip, int(port)))
            transport.connect(username=username, password=password)

            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.put(operation["src"], operation["dest"])
            transport.close()
        else:
            print('Lack of src or dest!')
