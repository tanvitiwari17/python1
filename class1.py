# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:14:19 2019

@author: tanvi
"""

import tkinter
import tkMessageBox
#top=tkinter.Tk()
def hello():
    tkMessageBox.showinfo("hello python","hello world")
B=tkinter.Button(top,text="hello",command=hello)
B.pack()
top.mainloop()
help(tkinter)
help(tkmessagebox)

import tkinter
 
window = tkinter.Tk()
 
# to rename the title of the window window.title("GUI")
 
# pack is used to show the object in the window
 
label = tkinter.Label(window, text = "Hello World!").pack()
 
window.mainloop()
