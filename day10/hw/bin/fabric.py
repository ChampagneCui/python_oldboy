#!/usr/bin/env python
#_*_coding:utf-8_*_

from sys import path
path.append(r'../conf')
path.append(r'../modules')
from settings import *
from features import *
import sys
import getopt
import threading

def usage():
    pass



if __name__ == '__main__':
    #fabric --group=testgroup --mode="shell" --command="ls -al"
    #fabric --host=1.1.1.1 --mode="put" --src="/tmp" --dest="/tmp"
    opts, args = getopt.getopt(sys.argv[1:],"h",["help","group=","host=","mode=","src=","dest=","command="])
    for op, value in opts:
            if (op == "--group"):
                operation["group"]=value
            elif (op == "--host"):
                operation["host"]=value
            elif (op == "--mode"):
                operation["mode"]=value
            elif (op == "--src"):
                operation["src"]=value
            elif (op == "--dest"):
                operation["dest"]= value
            elif (op == "--command"):
                operation["command"]=value
            else:
                usage() #help说明

    if hasattr(feature,operation["mode"]):
        func = getattr(feature, operation["mode"])
        i = 0
        host_list = get_host_info(operation)
        while i < len(host_list):
            # S= threading.Thread(target=func,args=(operation,ip,port,username,password,))
            # S.start()
            func(operation,i)
            i+=1
    else:
        print("doesn't support type.")

