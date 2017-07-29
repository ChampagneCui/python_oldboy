#!/usr/bin/env python
#_*_coding:utf-8_*_

from modules import models
from modules.db_conn import engine,session
from sqlalchemy.sql.expression import func
from conf.settings import init_msg


def wisdom():
	wisdom_obj=session.query(models.Wisdom).order_by(func.random()).limit(1).all()
	if wisdom_obj:
		print(wisdom_obj.sentence)
	else:
		print(init_msg)