#!/usr/bin/env python2.7
#_*_coding:utf-8_*_
from classes import person

job={1:['study',10000], 2:['go to company',30000], 3:['go abroad',50000]}

def road():
    for x in job.keys():
        print ('%s,%s') % (x, job[x][0])
    choose = raw_input('Which choose?')
    #if choose.isdigit() == 'True' and choose in ['1','2','3']:
    if choose in ['1', '2', '3']:
        print('John will %s !') %(job[int(choose)][0])
        John.salary = job[int(choose)][1]
        John.earn_money()
        print('1 year away...')
    else:
        road()

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

#屌丝逆袭史
i=0
while i < 3 :
        road()
        i+=1

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