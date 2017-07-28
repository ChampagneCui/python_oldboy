#_*_coding:utf-8_*_
import sys,os
import getopt
from modules import actions

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
	opts, args = getopt.getopt(sys.argv[1:], "h","f", "c",["help"])
	for op, value in opts:
		if (op == "-f"):
			pass
		elif (op == "-c"):
			if (value in actions):
				pass
			else:


		print(a)
		# file.close()
		exit()
	else:
		print("python jpserver.py -c 'start_session'")  # help说明
		print("python jpserver.py -c 'import_user' -f 'user.yml'")
		exit()