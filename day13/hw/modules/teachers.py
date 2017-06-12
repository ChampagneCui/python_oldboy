#_*_coding:utf-8_*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Pass1234@127.0.0.1/course",
					   encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类

class User(Base):
	__tablename__ = 'user'  # 表名
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))


class Couse(Base):
	__tablename__ = 'course'  # 表名
        id = Column(Integer,primary_key=True)
        name = Column(String(32))


Base.metadata.create_all(engine)  # 创建表结构

def add_teacher(name,password):
	Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
	Session = Session_class()  # 生成session实例

	user_obj = User(name=name, password=password)  # 生成你要创建的数据对象

	Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建

	Session.commit()  # 现此才统一提交，创建数据

#add_teacher('leo','1234')

def add_course(name):
	Session_class = sessionmaker(bind=engine)
        Session = Session_class()

        course_obj = Course(name=name)

        Session.add(course_obj) 

        Session.commit()



