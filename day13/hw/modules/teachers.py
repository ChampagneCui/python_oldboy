#_*_coding:utf-8_*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from classes import *

engine = create_engine("mysql+pymysql://root:Pass1234@127.0.0.1/course",
					   encoding='utf-8', echo=True)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

def add_teacher(name,password):
	user_obj = User(name=name, password=password)
	Session.add(user_obj)
	Session.commit()

#add_teacher('leo','1234')

def add_course(name):
	course_obj = Course(name=name)
	Session.add(course_obj)
	Session.commit()



