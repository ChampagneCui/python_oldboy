#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_
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



def login(u,p,role):
	if role=='s':
		try:
			student=Session.query(Student).filter(Student.name==u).first()
			if student.password == p:
				return 0
		except:
			print('Wrong password!')
			return 1
	elif role=='t':
		try:
			teacher = Session.query(Teacher).filter(Teacher.name == u).first()
			if teacher.password == p:
				return 0
		except:
			print('Wrong password!')
			return 1