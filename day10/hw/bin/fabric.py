#!/usr/bin/env python2.7
#_*_coding:utf-8_*_

from sys import path
path.append(r'../conf')
path.append(r'../modules')
from settings import *
from features import feature
import sys
import getopt

def usage():
    pass

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
        func(operation)
    else:
        print("doesn't support type.")

