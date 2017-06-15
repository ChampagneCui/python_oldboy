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
	b1 = Session.query(Course).filter_by(name=course).first()
	student_list=[]
 	for qq in students_qq:
		a = Session.query(Student).filter_by(qq=qq).first()
		student_list.append(a)
 
	b1.student = student_list
 
	#Session.add_all([b1])
	Session.commit()

def add_score(course_id,student_id,score):
	status = Session.query(student_attendance_score).filter(course_id==course_id).filter(student_id==student_id).first()
	print(status.score)
	status.score = score
	Session.commit()
	
	
add_score(7,1,88)
	
#s=[111111,222222,333333]
#add_student_to_course('python222',s)
