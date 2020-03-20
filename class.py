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
            m=int(input("enter marks of %s in %d" %(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name ,"got", self.marks)
        
s1=student('anisha')
s1.entermarks()
s2=student("shubhi")
s2.entermarks()
s1.display()
s2.display()

import datetime
today=datetime.date.today()
today
datetime.datetime.strptime(input ("enter date:mm/dd/yy"),'%m/%d/%y')

class fraction:
    def getdata(self):
        self.__num=int(input("enter the numerator:"))
        self.__deno=int(input("enter the denominator:"))
        if(self.__deno==0):
            print("denominator cannot be zero")
            exit()
    def display(self):
        self.__simplify()
        print(self.__num,"/",self.__deno)
    def __simplify(self):
        print("simplified:")
        common_div=self.__gcd(self.__num,self.__deno)
        self.__num=self.__num/common_div
        self.__deno=self.__num/common_div
    def __gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.__gcd(b,a%b)
f=fraction()
f.getdata()
f.display()

class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    @classmethod
    def square(cls,side):
        return cls(side,side)
    
r=rectangle.square(10)
print("area=",r.area())

