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

def outer(func):
	def inner(*args,**kwargs):
		try:
			s.hi()
			r = func(*args, **kwargs)
			return r
		except:
			print('请登陆！')
	return inner

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
			s.submit()
		elif welcome == '2':
			s_login()
		elif welcome == '3':
			s.show_score()
		elif welcome == '4':
			s.show_classroom()
		elif welcome == 'exit':
			exit()
		else:
			print('错误选项，请重新选择!')

class student_class(object):
	def __init__(self, name):
		self.current_student = Session.query(Student).filter(Student.name==name).first()

	@outer
	def show_score(self):
		course = raw_input('Please input the course:')
		self.course = Session.query(Course).filter(Course.name == course).first()
		print("s",self.current_student.id)
		print("c",self.course.id)
		self.status = Session.query(Status).filter(Status.student_id == self.current_student.id).\
			filter(Status.course_id==self.course.id).first()
		print('Your %s score is %d' %(course, self.status.score))

	@outer
	def show_classroom(self):
		i=0
		self.classroom = Session.query(Classroom).all()
		while i < len(self.classroom):
					print(self.classroom[i].name)
					i+=1

	@outer
	def submit(self):
		self.show_classroom()
		print('提交作业')

	def hi(self): #用来给装饰器验证登陆与否
		print('Hi %s') %(self.current_student.name)