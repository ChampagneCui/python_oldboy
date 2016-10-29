#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

class teachers:
    def __init__(self):
        name = raw_input('name:')
        passwd = raw_input('password:')
        age = raw_input('age:')
        favour = raw_input('favour:')
        self.name=name
        self.password=passwd
        self.age=age
        self.asset=0
        self.favour = favour

    def grade(self,point):
        if int(point)>=3:
            print('Thx! Have a nice lessons!')
        else:
            self.asset=self.asset-5

    def gain(self,fee):
        self.asset = self.asset + int(fee)

class courses:
    def __init__(self):
        name = raw_input('Please enter a course you want create:')
        fee = raw_input('How much:')
        self.name = name
        self.fee=fee

    def course_bonding(self,teacher):
        self.teacher=teacher

    def lessons(self,point):
        self.teacher.gain(self.fee)
        self.teacher.grade(point)

class students:
        def __init__(self,name,passwd,age):
            self.name=name
            self.password=passwd
            self.age=age
            self.asset=0
            self.experience=[]
            self.course=[]

        def choose_course(self,course):
            self.course.append(course)

        def st_add_money(self,money):
            self.asset=int(self.asset)+int(money)

        def have_lesson(self,num):
            num=int(num)
            self.experience.append(self.course[num].name)
            self.asset=self.asset-int(self.course[num].fee)
            point=raw_input('Please input grade point to teacher[1-5]:')
            self.course[num].lessons(point)

class managers:
        def __init__(self,name,passwd):
            self.name=name
            self.password=passwd
