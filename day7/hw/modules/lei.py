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
        self.asset = self.asset + fee

class courses:
    def __init__(self):
        name = raw_input('Please enter a course you want create:')
        fee = raw_input('How much:')
        self.name = name
        self.fee=fee

    def course_bonding(self,teacher):
        self.teacher=teacher

    def lessons(self,experience,course,fee):
        teachers.gain(fee)
        students.st_add_experience(course,fee)

class students:
        def __init__(self,name,passwd,age):
            self.name=name
            self.password=passwd
            self.age=age
            self.asset=0
            self.experience=[]

        def st_add_money(self,money):
            self.asset+=money

        def st_add_experience(self,course,fee):
            self.experience.append(course)
            self.asset-=fee

class managers:
        def __init__(self,name,passwd):
            self.name=name
            self.password=passwd
