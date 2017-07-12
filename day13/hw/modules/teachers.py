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
			t.add_teacher()
		elif welcome == '2':
			t_login()
		elif welcome == '3':
			t.add_course()
		elif welcome == '4':
			t.add_classroom()
		elif welcome == '5':
			t.add_student_to_class()
		elif welcome == '6':
			t.show_student()
		elif welcome == '7':
			t.show_classroom()
		elif welcome == '8':
			t.add_student_to_class()
		elif welcome == '9':
			t.add_score()
		elif welcome == 'exit':
			exit()
		else:
			print('错误选项，请重新选择!')


class teacher_class(object):
	def __init__(self,name):
		self.current_teacher = Session.query(Teacher).filter(Teacher.name==name).first()

	@outer
	def add_teacher(self):
		name = raw_input('请输入新教师账号:')
		password = raw_input('请输入新教师密码')
		self.teacher_obj = Teacher(name=name, password=password)
		Session.add(self.teacher_obj)
		Session.commit()

	@outer
	def add_course(self):
		name = raw_input('请输入新课程名:')
		detail = raw_input('请输入注释')
		self.course_obj = Course(name=name, detail=detail)
		Session.add(self.course_obj)
		Session.commit()

	@outer
	def add_classroom(self):
		name = raw_input('请输入新班级名:')
		teacher=Session.query(Teacher).filter_by(name=self.current_teacher).first()
		self.classroom_obj = Classroom(name=name, teacher_id=teacher.id)
		Session.add(self.classroom_obj)
		Session.commit()

	@outer
	def add_student_to_class(self):
		student_qq=raw_input('请输入学员qq号:')
		classroom = raw_input('请输入班级名:')
		self.student = Session.query(Student).filter_by(qq=int(student_qq)).first()
		self.classroom = Session.query(Classroom).filter_by(name=classroom).first()
		self.add_student_to_classroom_obj = StudentInClassroom(student_id=self.student.id, classroom_id=self.classroom.id)
		Session.add(self.add_student_to_classroom_obj)
		Session.commit()

	@outer
	def show_student(self):
		classroom = raw_input('请输入班级名:')
		self.classroom = Session.query(Classroom).filter_by(name=classroom).first()
		# student=Session.query(StudentInClassroom).join(Student).filter(StudentInClassroom.classroom_id==classroom.id).all()
		self.student = Session.query(Student).join(StudentInClassroom).filter(StudentInClassroom.classroom_id == self.classroom.id).all()
		i = 0
		while i < len(self.student):
			print(self.student[i])
			i += 1

	@outer
	def show_classroom(self):
		i = 0
		self.classroom = Session.query(Classroom).all()
		while i < len(self.classroom):
			print(self.classroom[i])
			i += 1

	@outer
	def add_student_to_course(self):
		'''默认是全出勤了，这里选择的是没有出勤的个别同学'''
		course = raw_input('请输入课程名:')
		students_qq = raw_input('请输入未出席的学员qq号,以逗号分隔:')
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

	@outer
	def add_score(self):
		course = raw_input('请输入课程名:')
		student = raw_input('请输入学员名:')
		score = raw_input('请输入分数:')
		course= Session.query(Course).filter(Course.name==course).first()
		student = Session.query(Student).filter(Student.name==student).first()
		self.status = Session.query(Status).filter(Status.course_id == course.id).filter(Status.student_id == student.id).first()
		self.score= Absense(status_id=self.status.id,score=score)
		Session.commit(self.score)

	def hi(self): #用来给装饰器验证登陆与否
		print('Hi %s') %(self.current_teacher.name)