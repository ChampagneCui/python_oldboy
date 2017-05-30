#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: ChenWei
"""
import re
import random
import hashlib


def get_color(text, color='red'):
    """
    将字符串格式化为带颜色内容
    :param text: 接收字符串
    :param color:默认红色
    :return: ->str 返回带颜色的内容
    """
    color_table = {
        "red": "\033[31m",
        "green": "\033[32;1m",
        "yellow": "\033[33;1m",
        "purple": "\033[35;1m",
        "end": "\033[0m",  # 结束符号
    }
    li = [color_table.get(color), str(text), color_table["end"]]
    return ''.join(li)


def validate_input(num_1, num_2, msg='msg'):
    """
    验证用户输入
    :param num_1: 开始范围
    :param num_2: 结束范围
    :param msg: 输出语句
    :return: ->str 返回用户号码
    """
    while True:
        inp_select = input(msg).strip()
        if len(inp_select) == 0:  # 验证1:检测是否输入为空
            continue

        if inp_select.isdigit():
            inp_select = int(inp_select)
            if inp_select < num_1 or inp_select > num_2:  # 验证2:输入数字是否超过范围
                print(get_color('输入范围错误,请输入[{0}-{1}]'.format(num_1, num_2)))
                continue
            else:
                return str(inp_select)
        else:
            print(get_color('输入类型错误,请输入[{0}-{1}]'.format(num_1, num_2)))


def input_not_empty_msg(msg):
    """
    检验输入不能为空
    :param msg:
    :return:
    """
    while True:
        inp = input(msg).strip().lower()
        if len(inp) == 0:
            print(get_color("输入内容不能为空!"))
            continue
        else:
            return inp


def validation_num():
    """
    随机数生成器
    :return: ->str
    """
    li = []
    for i in range(6):
        r = random.randrange(0, 5)
        if r == 2 or r == 4:
            num = random.randrange(0, 10)
            li.append(str(num))
        else:
            temp = random.randrange(65, 91)
            c = chr(temp)
            li.append(c)
    res = ''.join(li)
    return res


def generate_credit_card_id():
    """
    生成开头为4500的16位信用卡ID
    :return: ->str
    """
    li = ['4500', ]
    for i in range(12):
        r = random.randrange(0, 10)
        li.append(str(r))
    res = ''.join(li)
    return res


def encrypted_password(string):
    """
    加密，这里用做密码加密
    :param string: 输入字符串
    :return: ->str :返回加密后的结果
    """
    key = 'a%?jkl&*W'  # 加盐
    obj = hashlib.md5(bytes(key, encoding='utf-8'))
    obj.update(bytes(string, encoding='utf-8'))
    result = obj.hexdigest()
    return result


def interactive_input(*args):
    """
    交互输入
    :param args:
    :return: -> list
    """
    res_list = []
    li = [args]
    for line in li[0]:
        while True:
            val = input(line).strip()
            if len(val) == 0:
                print(get_color('输入内容不能为空!'))
                continue
            else:
                res_list.append(val)
                break
    return res_list


def help_msg(filename):
    """
    打印帮助
    :param filename: 文件名
    :return: -> none
    """
    print(get_color('Usage: %s <start|stop>' % (filename,)))
