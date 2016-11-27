#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from classes import person

John=person('John','Male','poor man','student')
Liz=person('Liz','Female','female god','student')
Peter=person('Peter','Male','rich man','student','USA')

print('When they are in college...')
#表白
John.fall_in_love(Liz)
Liz.fall_in_love(John)
#Liz I love you, even if you havn't money...

print('Once they graduated!')
#say something
John.separate()
Liz.separate()
#Peter say something
Liz.fall_in_love(Peter)
Peter.fall_in_love(Liz)

