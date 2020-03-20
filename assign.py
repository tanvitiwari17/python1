# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 00:08:09 2019

@author: tanvi
"""
x=float(input("enter a number:"))
y=x
rev=0
while(x>0):
    z=x%10
    rev=rev*10+z
print(rev)
if (rev==x):
    print("palindrome")
else:
    print("not palindrome")
