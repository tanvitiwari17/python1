# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:27:15 2020

@author:
"""

#list
l=[1,2,3,'a'] #mutable/can be altered(appened)
l
type(l)
l.append('b')
l.append('hi')
l.append(5)

#dictionaries
d={1:"apple",2:"banana"}
d
type(d)
d[2]            #returns value
d.get(1)         #returns value
d[1]="cherry"   #update(mutable)
d[2]="papaya"
d

#set
s1=set([1,2,3])
type(s1)
s3=set([1,2,4,3,2,2,1])
s3
s2=set([4,5]) #creating another set to update set s1
s1.update(s2)   #sets are mutable
s1


#frozenset
fs=frozenset([3,1,5])
fs.update(s2)   #frozensets are immutable,error occurs
fs


#tuple
t=(1,2,5) #tuples require commas
type(t)
t1=(7)
type(t1)
t2=(8,)
type(t2)


#Strings
s1='this is string 1'
s1
type(s1)
s2="this is string 2"
s2
s3="""this is string 3"""
type(s3)
s4="she's not afraid of the dark"
s4
