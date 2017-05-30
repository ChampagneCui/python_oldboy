# Day10 作业
> 作业需求

- [x] 博客
- [x] 流程图
- [x] 使用paramiko模块并利用多线程对远程服务器执行命令

## 博客地址

[陈维Day10博客地址](http://www.cnblogs.com/chen1930/p/6148432.html)

## 使使用paramiko模块并利用多线程对远程服务器执行命令
1、程序说明
实现功能如下:

- [x] 主机分组
- [x] 主机信息配置文件用configparser解析
- [x] 可批量执行命令、发送文件，结果实时返回，执行格式如下 
- [x] batch_run -h h1,h2,h3  -g web_clusters,db_servers -cmd  "df -h"
- [x] 主机用户名密码、端口可以不同
- [x] 执行远程命令使用paramiko模块
- [x] 批量命令需使用multiprocessing并发

2、程序测试账号
测试账号:
```python
无,需要根据环节自行更改db下的hosts.ini和groups.ini文件
```

4、目录结构
```python
./Day10
└── RemoteExeCmd
    ├── bin
    │   ├── __init__.py
    │   └── start.py    # 程序入口
    ├── conf
    │   ├── __init__.py
    │   └── settings.py
    ├── db
    │   ├── groups_db.ini   # 组配置文件
    │   ├── hosts_db.ini    # 主机配置文件
    │   └── __init__.py
    ├── lib
    │   ├── __init__.py
    │   └── tools.py
    ├── model
    │   ├── groups.py
    │   ├── hosts.py
    │   ├── __init__.py
    ├── modules
    │   ├── cmd.py
    │   ├── db_helper.py
    │   ├── __init__.py
    │   └── main.py
    └── ReadMe
        └── README.md
```

5、程序执行入口:
服务器默认监听端口为127.0.0.1，如果需要更改，需要修改conf->setting内的SERVER_IP和PORT端口参数，重启服务即可
```sh
$ cd Day10/RemoteExeCmd/bin
$ python3 start.py -h h1,h2,h3  -g web_clusters,db_servers -cmd  "df -h"
```

6、命令示例如下:
```sh
Commands:
    -h:    host     # host name
    -g:    group    # group name
    -cmd:  cmd      # exe cmd
For example:
    python3 start.py -h h1,h2,h3 -cmd  "df -h"
    python3 start.py -h h1,h2,h3  -g web_clusters,db_servers -cmd  "df -h"
```