#!/usr/bin/env python
#_*_coding:utf-8_*_
import sys,os
import getopt


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from modules import actions
from modules.wisdom import wisdom

if __name__ == '__main__':
	wisdom()
	if len(sys.argv) < 2:
		actions.usage()
		exit()

	opts, args = getopt.getopt(sys.argv[1:], "h",
							   ["start_session", "syncdb", "help", "create_users=", "create_groups=", "create_hosts=","create_bindhosts=","create_remoteusers=",
								"stop"])
	for op, value in opts:
		if (op in ["--start_session","--syncdb","--stop"]):
			op=op.strip('-')
			func=getattr(actions.feature,op)
			func()
			exit()
		elif (op in ["--create_users","--create_groups","--create_hosts","--create_bindhosts","--create_remoteuser"]):
			op=op.strip('-')
			func=getattr(actions.feature,op)
			func(value)
			exit()
		else:
			actions.usage()
			exit()
