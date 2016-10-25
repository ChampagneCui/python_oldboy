#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
import pickle
from sys import path
path.append(r'..\modules')
path.append('..\conf')

class teachers:
    def __init__(self):
        favour = raw_input('favour:')
        name = raw_input('name:')
        age = raw_input('age:')
        self.favour=favour
        self.name=name
        self.age=age
        self.asset=0

    def print_info(self):
        print(self.name,self.asset,self.age,self.asset)

    def grade(self,point):
        if int(point)>=3:
            print('Thx! Have a nice lessons!')
        else:
            self.asset=self.asset-5

    def gain(self,fee):
        self.asset = self.asset + fee

class courses:
    def __init__(self,name,fee,teacher):
        name = raw_input('Please enter a course you want create:')
        fee = raw_input('How much:')
        teacher = raw_input('Which teacher?')
        self.name = name
        self.fee=fee
        self.teacher=teacher

    def lessons(self,experience,course,fee):
        teachers.gain(fee)
        students.st_add_experience(course,fee)

class students:
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

#
a=teachers()
a.print_info()
f=file('%s.txt','w') %(a.name)
pickle.dump(a,f)
f.close()

# f=file('1.txt')
# b=pickle.load(f)
# f.close()
# print(b.name)
# b.print_info()