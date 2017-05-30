#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version:
@author: ChenWei
"""

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 服务端地址
SERVER_IP = "127.0.0.1"
PORT = 9999

# 服务端上传文件保存路径
UPLOAD_FILES_PATH = os.path.join(BASE_DIR, 'uploads')

# 数据库文件路径
DB_PATH = os.path.join(BASE_DIR, 'db')

# 配置文件路径
CONF_PATH = os.path.join(BASE_DIR, 'conf')

# 日志路径
LOG_PATH = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = logging.INFO  # 日志级别
LOG_TYPES = {
    'transaction': os.path.join(LOG_PATH, 'transactions.log'),
    'access': os.path.join(LOG_PATH, 'access.log'),
}

# 备份路径
BACKUP_PATH = os.path.join(BASE_DIR, 'backup')

# 临时文件
TMP_PATH = os.path.join(BASE_DIR, 'tmp')

DATABASES = {
    'ENGINE': 'file_store',
    'DB_NAME': os.path.join(DB_PATH, 'user_db.ini'),
}
