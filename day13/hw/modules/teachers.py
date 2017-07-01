# _*_coding:utf-8_*_
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
			t.hi()
			r = func(*args, **kwargs)
			return r
		except:
			print('请登陆！')
	return inner

def t_login():
	global t
	username = raw_input('请输入账号:')
	password = raw_input('请输入密码')
	if login(username, password, 't') == 0:  # login函数公用
		t = teacher_class(username)
		print('%s, welcome login!' % (t.current_teacher))
	else:
		print('Wrong username or password!')


def t_main():
	while 1:
		welcome = raw_input(T_WELCOME_MSG)  # 上传、登陆、查看
		if welcome == '1':
			try:
				t.add_teacher()
			except:
				print('Please login')
		elif welcome == '2':
			t_login()
		elif welcome == '3':
			try:
				t.add_course()
			except:
				print('Please login')
		elif welcome == '4':
			t.add_classroom()
		else:
			print('错误选项，请重新选择!')


class teacher_class(object):
	def __init__(self, name):
		self.current_teacher = name

	def add_teacher(self):
		name = raw_input('请输入新教师账号:')
		password = raw_input('请输入新教师密码')
		self.teacher_obj = Teacher(name=name, password=password)
		Session.add(self.teacher_obj)
		Session.commit()

	def add_course(self):
		name = raw_input('请输入新课程名:')
		detail = raw_input('请输入注释')
		self.course_obj = Course(name=name, detail=detail)
		Session.add(self.course_obj)
		Session.commit()

	def add_classroom(self,name):
		# teacher_id=
		self.classroom_obj = Classroom(name=name, teacher_id='xxx')
		Session.add(self.classroom_obj)
		Session.commit()

	def add_student_to_class(self,student_qq, classroom):
		self.student = Session.query(Student).filter_by(qq=student_qq).first()
		self.classroom = Session.query(Classroom).filter_by(name=classroom).first()
		self.add_student_to_classroom_obj = StudentInClassroom(student_id=self.student.id, classroom_id=self.classroom.id)
		Session.add(add_student_to_classroom_obj)
		Session.commit()

	def show_student(self,classroom):
		self.classroom = Session.query(Classroom).filter_by(name=classroom).first()
		# student=Session.query(StudentInClassroom).join(Student).filter(StudentInClassroom.classroom_id==classroom.id).all()
		self.student = Session.query(Student).join(StudentInClassroom).filter(StudentInClassroom.classroom_id == self.classroom.id).all()
		i = 0
		while i < len(self.student):
			print(self.student[i])
			i += 1

	def show_classroom(self):
		i = 0
		self.classroom = Session.query(Classroom).all()
		while i < len(self.classroom):
			print(self.classroom[i])
			i += 1


	def add_student_to_course(self,course, students_qq):
		'''默认是全出勤了，这里选择的是没有出勤的个别同学'''
		self.c1 = Session.query(Course).filter_by(name=course).first()
		absence_list = []
		for qq in students_qq:
			a = Session.query(Student).filter_by(qq=qq).first()
			absence_list.append(a)

		self.total_student = Session.query(Student).join(StudentInClassroom).filter(StudentInClassroom.classroom_id == self.b1.classroom_id).all()
		student_list = list(set(self.total_student) - set(absence_list))

		#self.b1.student = student_list
		for x in student_list:
			print x

		# Session.add_all([b1])
		Session.commit()


	def add_score(self,course_id, student_id, score):
		self.status = Session.query(Status).filter(course_id == course_id).filter(student_id == student_id).first()
		self.status.score = score
		Session.commit()

	def hi(self): #用来给装饰器验证登陆与否
		print('Hi %s') %(self.current_teacher.name)