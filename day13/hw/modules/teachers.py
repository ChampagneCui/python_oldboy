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

def	add_student_to_class(student_qq,classroom):
	student= Session.query(Student).filter_by(qq=student_qq).first()
	classroom=  Session.query(Classroom).filter_by(name=classroom).first()
	add_student_to_classroom_obj = StudentInClassroom(student_id=student.id,classroom_id=classroom.id)
	Session.add(add_student_to_classroom_obj)
	Session.commit()

def show_student(classroom):
	classroom=Session.query(Classroom).filter_by(name=classroom).first()
	student=Session.query(StudentInClassroom).filter_by(classroom_id=classroom.id).all()
	print(student)
	#print(Session.query(Student.id,Student.name,Student.qq).all())


show_student('python')