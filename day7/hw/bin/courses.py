#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from sys import path
path.append(r'..\modules')
path.append('..\conf')

class teachers:
    def __init__(self,favour,name,age):
        self.favour=favour
        self.name=name
        self.age=age
        self.asset=0

    def accident(self):
        self.asset=self.asset-5

    def gain(self,fee):
        self.asset = self.asset + fee

class courses:
    def __init__(self,name,fee,teacher):
        self.name = name
        self.fee=fee
        self.teacher=teacher

    def lesson(self,experience,course,fee):
        teachers.gain(fee)
        student.st_add_experience(course,fee)

class student:
        def __init__(self,name, age):
            self.name=name
            self.age=age
            self.asset=0
            self.experience=[]


        def st_add_money(self,money):
            self.asset+=money

        def st_add_experience(self,course,fee):
            self.experience.append(course)
            self.asset-=fee

