#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR) #将脚本所在根路径也加入系统变量中

print(sys.path)




if __name__ == '__main__':
    from modules.actions import excute_from_command_line #这种写法只有python3支持
    excute_from_command_line(sys.argv)
