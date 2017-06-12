#_*_coding:utf-8_*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://root:Pass1234@127.0.0.1/course",
					   encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类


class User(Base):
	__tablename__ = 'user'  # 表名
	id = Column(Integer,auto ,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))


Base.metadata.create_all(engine)  # 创建表结构
