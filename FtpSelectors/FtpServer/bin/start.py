#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: ChenWei
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from modules import ftp_server

if __name__ == '__main__':
    ftp_server.FtpServer(sys.argv)
