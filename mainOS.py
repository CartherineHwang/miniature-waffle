# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:16:05 2023

@author: HFY
"""
from tkinter import *
from tkinter.messagebox import *
import subprocess
global filename

'''
def working():
    
    if eval(e1.get())==1:
       import drawpic1
'''
     
def login():
    name = e1.get()
    ID = e2.get()
    mainroot = Tk()
    mainroot.title("Tools Menu")
    mainroot.geometry("600x600")
    button_calculator = Button(mainroot, text="Calculator", width=20, command=calculator)
    button_calculator.place(x=20,y=60)
    button_learning = Button(mainroot, text="Learning", width=20, command=learning)
    button_learning.place(x=20,y=100)
    button_qrcode = Button(mainroot, text="Qrcode", width=20, command=Qrcode)
    button_qrcode.place(x=20,y=140)
    button_polardrawpic = Button(mainroot, text="Polardrawpic", width=20, command=polardrawpic)
    button_polardrawpic.place(x=20,y=180)
    mainroot.mainloop()
    
def calculator():
    import calculator
    
    
    
def learning():
    import learning
    
def Qrcode():
    import Qrcode
    
def polardrawpic():
    import polardrawpic
    
root=Tk()
root.title("Tool bag to stupid éduidiants:D")
root.geometry("600x600")


L1=Label(root,text='Please enter your name in the first box and your id in the second box')
L1.place(x=10,y=50)
e1=Entry(root,width=20)
e1.place(x=20,y=80)
e2=Entry(root,width=20)
e2.place(x=20,y=110)

L2=Label(root,text='Please enter the name of your file')
L2.place(x=10,y=140)
e3=Entry(root,width=20)
e3.place(x=20,y=170)
namefile=e3.get()
button_login=Button(root,text='log in',width=20,command=login)
button_login.place(x=250,y=400)
root.mainloop()












