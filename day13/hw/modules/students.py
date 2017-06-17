#_*_coding:utf-8_*_
from sys import path
path.append('..\conf')
from settings import *
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from classes import *
from logins import login

engine = create_engine("mysql+pymysql://root:Pass1234@127.0.0.1/course",
					   encoding='utf-8', echo=True)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()


def s_login():
	global s
	username = raw_input('请输入账号:')
	password = raw_input('请输入密码')
	if login(username, password,'s') == 0:
		s=student_class(username)
		print('%s, welcome login!' %(s.current_student.name))
	else:
		print('Wrong username or password!')

def s_main():
	while 1:
		welcome = raw_input(S_WELCOME_MSG) #上传、登陆、查看
		if welcome == '1':
			try:
				s.submit()
			except:
				print('Please login')
		elif welcome == '2':
			s_login()
		elif welcome == '3':
			try:
				course_name=raw_input('Please input the course:')
				s.show_score(course_name)
			except:
				print('Please login')
		elif welcome == '4':
			s.show_classroom()
		else:
			print('错误选项，请重新选择!')

class student_class(object):
	def __init__(self, name):
		self.current_student = Session.query(Student).filter(Student.name==name).first()

	def show_score(self, course):
		self.course = Session.query(Course).filter(Course.name == course).first()
		aa= Session.query(Status).all()
		self.status = Session.query(Status).filter(Status.student_id == 2).\
			filter(Status.course_id==2).first()
		print('Your %s score is %d' %(course, self.status.score))

	def show_classroom(self):
		i=0
		self.classroom = Session.query(Classroom).all()
		while i < len(self.classroom):
					print(self.classroom[i].name)
					i+=1

	def submit(self):
		self.show_classroom()
		print('提交作业')