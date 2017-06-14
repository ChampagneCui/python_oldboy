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

def add_student_to_course():
	#采用反向方式,即写在student列表中的同学为没出勤的同学
	b1 = Course(name="Python222")
 
	a1 = Student(name='leo')
	a2 = Student(name='aaa')
	a3 = Student(qq=111111)
 
	b1.student = [a1,a2,a3]
 
	Session.add_all([b1,a1,a2,a3])
	Session.commit()
	
add_student_to_course()
