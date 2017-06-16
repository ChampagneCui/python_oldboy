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


def t_login():
	global t
	username = raw_input('请输入账号:')
	password = raw_input('请输入密码')
	if login(username, password,'t') == 0: #login函数公用
		t=teacher_class(username)
		print('%s, welcome login!' %(t.current_student))
	else:
		print('Wrong username or password!')

def t_main():
    while 1:
        welcome = raw_input(T_WELCOME_MSG) #上传、登陆、查看
        if welcome == '1':
			try:
            	t.submit()
			except:
				print('Please login')
        elif welcome == '2':
            t_login()
        elif welcome == '3':
			try:
            	t.show_score()
			except:
				print('Please login')
        else:
            print('错误选项，请重新选择!')

def add_teacher(name,password):
	teacher_obj = Teacher(name=name, password=password)
	Session.add(teacher_obj)
	Session.commit()

def add_course(name,detail):
	course_obj = Course(name=name, detail=detail)
	Session.add(course_obj)
	Session.commit()

def add_classroom(name):
	#teacher_id=
	classroom_obj = Classroom(name=name,teacher_id='xxx')
	Session.add(classroom_obj)
	Session.commit()

def add_student_to_class(student_qq,classroom):
	student= Session.query(Student).filter_by(qq=student_qq).first()
	classroom=  Session.query(Classroom).filter_by(name=classroom).first()
	add_student_to_classroom_obj = StudentInClassroom(student_id=student.id,classroom_id=classroom.id)
	Session.add(add_student_to_classroom_obj)
	Session.commit()

def show_student(classroom):
	classroom=Session.query(Classroom).filter_by(name=classroom).first()
	#student=Session.query(StudentInClassroom).join(Student).filter(StudentInClassroom.classroom_id==classroom.id).all()
	student=Session.query(Student).join(StudentInClassroom).filter(StudentInClassroom.classroom_id==classroom.id).all()
	i=0
	while i < len(student):
		print(student[i])
		i+=1


def show_classroom():
	i=0
	classroom=Session.query(Classroom).all()
        while i < len(classroom):
                print(classroom[i])
                i+=1

def add_student_to_course(course,students_qq):
	'''默认是全出勤了，这里选择的是没有出勤的个别同学'''
	b1 = Session.query(Course).filter_by(name=course).first()
	absence_list=[]
 	for qq in students_qq:
		a = Session.query(Student).filter_by(qq=qq).first()
		absence_list.append(a)

	total_student=Session.query(Student).join(StudentInClassroom).filter(StudentInClassroom.classroom_id==b1.classroom_id).all()
	student_list=list(set(total_student)-set(absence_list))

	b1.student = student_list
 
	#Session.add_all([b1])
	Session.commit()

def add_score(course_id,student_id,score):
	status = Session.query(student_attendance_score).filter(course_id==course_id).filter(student_id==student_id).first()
	status.score = score
	Session.commit()
	
	
#add_score(2,2,88)
	
#s=[111111,]
#add_student_to_course('python2',s)
