#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version:
@author: ChenWei
"""

import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 下载文件保存路径
DOWNLOAD_FILES_PATH = os.path.join(BASE_DIR, 'downloads')

# 日志路径
LOG_PATH = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = logging.INFO  # 日志级别
LOG_TYPES = {
    'transaction': os.path.join(LOG_PATH, 'transactions.log'),
    'access': os.path.join(LOG_PATH, 'access.log'),
}
