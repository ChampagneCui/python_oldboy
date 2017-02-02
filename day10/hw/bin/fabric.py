#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

from sys import path
path.append(r'../conf')
path.append(r'../modules')
from settings import *
from features import feature
import sys
import getopt
import threading

def usage():
    pass

def get_host_info(operation):
    if group in operation.keys():
        group_name = operation[group]
        host_list = gconf.get(group_name, "host")
        return host_list
    elif host in operation.keys():
        host_list = []
        host = operation[host]
        host_list.append(host)
        return host_list
    else:
        return 1 ##报错

if __name__ == '__main__':
    #fab --group=testgroup --mode="shell" --command="ls -al"
    #fab --host=1.1.1.1 --mode="put" --src="/tmp" --dest="/tmp"
    opts, args = getopt.getopt(sys.argv[1:],longopts =["help","group=","host=","mode=","src=","dest=","command="])
    for op, value in opts:
            if (op == "--group"):
                operation[group]=value
            elif (op == "--host"):
                operation[host]=value
            elif (op == "--mode"):
                operation[mode]=value
            elif (op == "--src"):
                operation[src]=value
            elif (op == "--dest"):
                operation[dest]= value
            elif (op == "--command"):
                operation[command]=value
            else:
                usage() #help说明

    if hasattr(feature,operation[mode]):
        func = getattr(feature, operation[mode])
        i = 0
        host_list = get_host_info(operation)
        while i < len(host_list):
            ip = hconf.get(host_list[i], "ip")
            port = hconf.get(host_list[i], "port")
            username = hconf.get(host_list[i], "username")
            password = hconf.get(host_list[i], "password")
            S= threading.Thread(target=func,args=(operation,ip,port,username,password,))
            S.start()
            i+=1
    else:
        print("doesn't support type.")

