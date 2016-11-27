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
        print("I am %s. I'm %s from %s. I'm a %s and I'm a %s!")%(self.name,self.sex,self.nationnality,self.work,self.role)

    def fall_in_love(self,mate):
        self.mate=mate
        print("%s and %s are fall in loved! Let\'s congratulations!") %(self.name,self.mate.name)

    def separate(self):
        self.mate=''
        print('%s is alone!') %(self.name)

    def earn_money(self):
        self.asset+=self.salary
        print("%s earned %d! Now he/she has %d asset!") %(self.name,self.salary,self.asset)
        self.role_change()

    def talk(self):
        pass

    def role_change(self):
        if self.asset>=100000:
            self.role='rich man'
        else:
            pass





