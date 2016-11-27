#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

class person:
    def __init__(self,name,sex,role,work,nationality='China',house='None',car='None',asset=0,salary=0):
        self.name=name
        self.sex=sex
        self.role=role
        self.work=work
        self.nationnality=nationality
        self.house=house
        self.car=car
        self.asset=asset
        self.salary=salary

    def fall_in_love(self,mate):
        self.mate=mate
        print("%s and %s are fall in loved! Let\'s congratulations!") %(self.name,self.mate.name)

    def separate(self):
        self.mate=''
        print('%s and %s are break up!') %(self.name,self.mate.name)

    def earn_money(self):
        self.asset+=self.salary
        print("%s earned %d! Now he/she has %d asset!") %(self.name,self.salary,self.asset)

    def talk(self):
        





