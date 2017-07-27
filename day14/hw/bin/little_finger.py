#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR) #将脚本所在路径也加入系统变量中

print(sys.path)

from modules.actions import excute_from_command_line

if __name__ == '__main__':

    excute_from_command_line(sys.argv)
