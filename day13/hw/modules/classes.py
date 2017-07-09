#_*_coding:utf-8_*_
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column, Integer, String,VARCHAR
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

'''
Status = Table('status', Base.metadata,
						id = Column(Integer,primary_key=True),
						Column('course_id',Integer,ForeignKey('course.id'),primary_key=True),
						Column('student_id',Integer,ForeignKey('student.id'),primary_key=True),
				)
'''

class Status(Base):
	__tablename__ = 'status'
	__table_args__ = (PrimaryKeyConstraint('course_id', 'student_id'),)
	id = Column(Integer, autoincrement=True)
	course_id = Column(Integer,ForeignKey('course.id'))
	course = relationship("Course",backref="status")
	student_id = Column(Integer,ForeignKey('student.id'))
	student = relationship("Student",backref="status")

class Absence(Base):
	__tablename__ = 'absence' # 表名
	status_id =Column(Integer,ForeignKey('status.id'),primary_key=True)
	status = relationship("Status", backref='absense')
	absence = Column(Integer)

class Score(Base):
	__tablename__ = 'score'  # 表名
	status_id = Column(Integer, ForeignKey('status.id'),primary_key=True)
	status = relationship("Status", backref='score')
	score = Column(Integer)


class Course(Base):
	__tablename__ = 'course'  # 表名
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	detail = Column(String(128))
	classroom_id = Column(Integer,ForeignKey('classroom.id'))
	classroom = relationship("Classroom",backref="course")
	#student = relationship('Student',secondary=Status,backref='course')

class Student(Base):
	__tablename__ = 'student'
	id = Column(Integer,primary_key=True)
	name = Column(String(32))
	password = Column(String(64))
	qq = Column(Integer)

	def __repr__(self):
			return "<Student(id='%s',name='%s',qq='%s')>" % (self.id,self.name,self.qq)

class Classroom(Base):
	__tablename__ = 'classroom'
	id = Column(Integer, primary_key=True)
	name = Column(String(32))
	teacher_id = Column(Integer,ForeignKey('teacher.id'))
	teacher = relationship("Teacher",backref="classroom")

	def __repr__(self):
				return "<Student(id='%s',name='%s')>" % (self.id,self.name)



class StudentInClassroom(Base):
	__tablename__ = 'student_in_classroom'
	__table_args__ = (	PrimaryKeyConstraint('classroom_id', 'student_id'),)
	classroom_id = Column(Integer,ForeignKey('classroom.id'))
	classroom = relationship("Classroom",backref="student_in_classroom")
	student_id = Column(Integer,ForeignKey('student.id'))
	student = relationship("Student", backref="student_in_classroom")
