#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
# import logging
# import logging.config
# CONF_LOG = "../conf/logging.conf"
# logging.config.fileConfig(CONF_LOG)# 采用配置文件
# logger = logging.getLogger("xzs")
# logger.debug("Hello xzs")
#
# logger = logging.getLogger()
# logger.info("Hello root")
#
# ttt='hi everyone'
# logger = logging.getLogger("ttt")
# logger.critical(ttt)
from atm import pay

pay('u','p',100000)