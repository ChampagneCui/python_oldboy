#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from classes import person

John=person('John','Male','poor man','student')
Liz=person('Liz','Female','female god','student')
Peter=person('Peter','Male','rich man','student','USA')

print('When they are in college...')
John.talk("I love you! But I haven't money. Do you care it?")
Liz.talk("I love you, I don't care!","happy")
John.fall_in_love(Liz)
Liz.fall_in_love(John)

print('Once they graduated!')
Liz.talk("I want Prada,LV, and you can't give me! This is my birthday surprice that Peter give me!(LV)","sad")
John.separate()
Liz.separate()
Liz.fall_in_love(Peter)
Peter.fall_in_love(Liz)

#John say he will be rich!
John.talk("I wanner be rich!","Angry")

print('5 years away...')
#John rich
John.salary=50000000
John.earn_money()

#Peter say something
Peter.talk("I don't love you any more,Liz!")
Liz.talk('No! I give you my first time!',"Sad")
Peter.talk("Who care?","happy")
Peter.separate()
Liz.separate()

#Liz say to John
Liz.talk("John,I know I'm wrong! Can we be together again?")
#John say something
John.talk("Do you know why I have so much money?","happy")
John.talk("I am Peter's lover now!")
John.fall_in_love(Peter)
Peter.fall_in_love(John)

print('从此John和Peter过上了幸福的生活...')