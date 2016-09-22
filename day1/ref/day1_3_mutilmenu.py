# -*- coding:utf-8 -*-
"""
__author: super
blog: blog.csdn.net/songfreeman
"""


# 一级菜单： 省
def show_province():
    province_list = (
        {'pid': '1', 'pname': '北京'},
        {'pid': '2', 'pname': '河北'},
        {'pid': '3', 'pname': '河南'},
        {'pid': '4', 'pname': '湖北'},
        {'pid': '5', 'pname': '江苏'},

    )
    return province_list


# 二级菜单： 市
def show_city():
    city_list = (
        ({'cid': '1-1', 'cname': '西城区'},
         {'cid': '1-2', 'cname': '东城区'},
         {'cid': '1-3', 'cname': '海淀区'},),
        ({'cid': '2-1', 'cname': '石家庄'},
         {'cid': '2-2', 'cname': '保定市'},
         {'cid': '2-3', 'cname': '邢台市'},),
        ({'cid': '3-1', 'cname': '郑州市'},
         {'cid': '3-2', 'cname': '开封市'},
         {'cid': '3-3', 'cname': '洛阳市'},),
        ({'cid': '4-1', 'cname': '武汉市'},
         {'cid': '4-2', 'cname': '宜昌市'},
         {'cid': '4-3', 'cname': '荆门市'},),
    )
    return city_list


# 三级菜单： 区县
def show_area():
    area_list = (
        ({'aid': '1-1-1', 'aname': '阜成门'},{'aid': '1-1-2', 'aname': '长椿街'},{'aid': '1-1-31', 'aname': '宣武门'},),
        ({'aid': '1-2-1', 'aname': '金宝街'},{'aid': '1-2-2', 'aname': '珠市口'},{'aid': '1-2-3', 'aname': '东直门'},),
        ({'aid': '1-3-1', 'aname': '中关村'},{'aid': '1-3-2', 'aname': '西二旗'},{'aid': '1-3-3', 'aname': '肖家河'},),
        ({'aid': '2-1-1', 'aname': '长安区'}, {'aid': '2-1-2', 'aname': '桥东区'}, {'aid': '2-1-3', 'aname': '桥西区'},),
        ({'aid': '2-2-1', 'aname': '新市区'}, {'aid': '2-2-2', 'aname': '北市区'}, {'aid': '2-2-3', 'aname': '南市区'},),
        ({'aid': '2-3-1', 'aname': '邢台县'}, {'aid': '2-3-2', 'aname': '内丘县'}, {'aid': '2-3-3', 'aname': '柏乡县'},),
        ({'aid': '3-1-1', 'aname': '金水区'}, {'aid': '3-1-2', 'aname': '二七区'}, {'aid': '3-1-3', 'aname': '上街区'},),
        ({'aid': '3-2-1', 'aname': '龙亭区'}, {'aid': '3-2-2', 'aname': '南关区'}, {'aid': '3-2-3', 'aname': '开封县'},),
        ({'aid': '3-3-1', 'aname': '老城区'}, {'aid': '3-3-2', 'aname': '西工区'}, {'aid': '3-3-3', 'aname': '新安县'},),
        ({'aid': '4-1-1', 'aname': '江岸区'}, {'aid': '4-1-2', 'aname': '江汉区'}, {'aid': '4-1-3', 'aname': '武昌区'},),
        ({'aid': '4-2-1', 'aname': '宜昌县'}, {'aid': '4-2-2', 'aname': '远安县'}, {'aid': '4-2-3', 'aname': '新山县'},),
        ({'aid': '4-3-1', 'aname': '东宝区'}, {'aid': '4-3-2', 'aname': '京山县'}, {'aid': '4-3-3', 'aname': '沙洋县'},),

    )
    return area_list


# 显示全部的省级菜单
def print_province_menu_all():
    menu_list = show_province()
    for menu in menu_list:
        symbols = "|" + "-" * 2
        print(symbols + "[" + menu['pid'] + "] " + menu['pname'])


# 根据选择的省级菜单编号，显示指定的某个省
def print_province_menu_by_pid(pid):
    menu_list = show_province()
    for menu in menu_list:
        symbols = "|" + "-" * 2
        if menu['pid'] == pid:
            print(symbols + "[" + menu['pid'] + "] " + menu['pname'])
            break


# 打印指定的省编号ID下的所有市名称
def print_city_menu_all(pid_choosed):
    # 显示指定的省
    print_province_menu_by_pid(pid_choosed)
    symbols = "|" + "-" * 4
    for city_list in show_city():
        for city in city_list:
            pid, cid = city['cid'].split('-')
            if pid == pid_choosed:
                print(symbols + '[' + cid + '] ' + city['cname'])

    return True


# 根据用户的选择市ID号显示指定的市
def print_city_menu_by_cid(ppid, ccid):
    print_province_menu_by_pid(ppid)
    symbols = "|" + "-" * 4
    for city_list in show_city():
        for city in city_list:
            pid, cid = city['cid'].split('-')
            if pid ==ppid and cid == ccid:
                print(symbols + '[' + cid + '] ' + city['cname'])

    return True


# 显示指定的省-市下的所有区县
def print_area_all(pid, cid):
    # 显示选中的市
    print_city_menu_by_cid(pid,cid)
    symbols = "|" + "-" * 6
    for area_list in show_area():
        for area in area_list:
            ppid, ccid, aid = area['aid'].split('-')
            if ppid == pid and ccid == cid:
                print(symbols + '[' + aid + '] ' + area['aname'])
    return True


# 判断输入的省编号是否存在（True / False )
def check_pid_is_exists(pid):
    is_exists_flag = False
    for menu in show_province():
        if menu['pid'] == pid:
            is_exists_flag = True
            break
    return is_exists_flag


# 判断选择市是否存在
def check_cid_is_exists(pid,key):
    is_exists_flag = False
    for city_list in show_city():
        for city in city_list:
            if city['cid'] == pid + "-" + key:
                is_exists_flag = True
    return is_exists_flag




#
if __name__ == "__main__":
    pid_choosed = ""    # 选中的省编号
    cid_choosed = ""    # 选中的市编号
    finish_flag = True  # 外层循环标识

    # 外层循环,当二级菜单返回上一级是返回到此
    while finish_flag:
        # 显示1级菜单
        print_province_menu_all()

        # 选择省菜单的编号
        pid = ""
        # 你没有选择编号或者编号不存在? 继续输入吧老兄
        while len(pid) == 0 or not check_pid_is_exists(pid):
            pid = raw_input("选择省编号[exit 退出系统] : ")
            # 你要退出？
            if pid == "exit":
                exit()
        else:
            pid_choosed = pid

        # 内层循环,当三级菜单返回时上一级是返回到此
        city_flag = True  # 内层循环标识
        while city_flag:
            # 打印选定省下的所有2级菜单
            print_city_menu_all(pid_choosed)
            # 选择市级菜单编号
            cid = ""
            while len(cid) == 0:
                cid = raw_input("请选择市编号[quit 返回上级菜单] : ").strip().lower()
            else:
                # 返回上一级菜单,跳出内层循环到外层
                if cid == 'quit':
                    city_flag = False
                    continue
                else:
                    cid_choosed = cid
                    if check_cid_is_exists(pid_choosed,cid_choosed):
                        # 显示三级菜单
                        print_area_all(pid_choosed, cid_choosed)
                        next_choose = raw_input("quit 返回上一级菜单: ")
                        # 返回二级菜单,继续内层循环
                        while next_choose != "quit":
                            next_choose = raw_input("quit 返回上一级菜单: ")
                        else:
                            continue
                    else:
                        print('\n输入错误,不存在对应的市! ')














