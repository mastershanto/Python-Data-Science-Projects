# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 23:37:45 2022

@author: User
"""

from tkinter import Label, Entry, mainloop, Tk
master=Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1= Entry(master)
e2= Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()