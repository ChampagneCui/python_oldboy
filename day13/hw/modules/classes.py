#_*_coding:utf-8_*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'  # 表名
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))


class Couse(Base):
	__tablename__ = 'course'  # 表名
        id = Column(Integer,primary_key=True)
        name = Column(String(32))