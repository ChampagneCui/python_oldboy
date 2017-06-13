#_*_coding:utf-8_*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import PrimaryKeyConstraint

Base = declarative_base()

class Teacher(Base):
	__tablename__ = 'teacher'  # 表名
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))


class Course(Base):
	__tablename__ = 'course'  # 表名
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	detail = Column(VARCHAR(128))
	classroom_id = Column(Integer,ForeignKey('classroom.id'))
	classroom = relationship("Classroom",backref="course")

class Student(Base):
	__tablename__ = 'student'
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))
	qq = Column(Integer)

class Classroom(Base):
	__tablename__ = 'classroom'
	id = Column(Integer, primary_key=True)
	name = Column(String(32))
	teacher_id = Column(Integer,ForeignKey('teacher.id'))
	teacher = relationship("Teacher",backref="classroom")


class Status(Base):
	__tablename__ = 'status'
	__table_args__ = (	PrimaryKeyConstraint('course_id', 'student_id'),)
	course_id = Column(Integer,ForeignKey('course.id'))
	course = relationship("Course",backref="status")
	student_id = Column(Integer,ForeignKey('student.id'))
	student = relationship("Student",backref="status")
	attendance = Column(Integer)
	score = Column(Integer)

class StudentInClassroom(Base):
	__tablename__ = 'student_in_classroom'
	__table_args__ = (	PrimaryKeyConstraint('classroom_id', 'student_id'),)
	classroom_id = Column(Integer,ForeignKey('classroom.id'))
	classroom = relationship("Classroom",backref="student_in_classroom")
	student_id = Column(Integer,ForeignKey('student.id'))
	student = relationship("Student", backref="student_in_classroom")