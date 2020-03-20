# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:31:23 2019

@author: tanvi
"""

class student:
    def __init__(self,name):
            self.name=name
            self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("enter marks of %s:%d",(self.marks,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name ,"got", self.marks)
        
s1=student('anisha')
s1.entermarks()
s2=student("shubhi")
s2.entermarks()
s1.display()
s2.display()