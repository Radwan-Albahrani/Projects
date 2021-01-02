#programs needed to check the password
def check():
    if password.get() == "123":
        f = open(r"logs.txt","a")
        f.write("One successful Login Attempt at: " + str(datetime.datetime.now()) + "\n")
        f.close()
        Label(text="     Correct password      ",bg="white").grid(row=2,column=1,sticky=W,pady=10)
    else:
        f = open(r"logs.txt","a")
        f.write("One Failed Login Attempt at: " + str(datetime.datetime.now()) + "\n")
        f.close()
        Label(text="     Wrong password     ",bg="white").grid(row=2,column=1,sticky=W,pady=10)

def check1(events):
    if password.get() == "123":
        f = open(r"logs.txt","a")
        f.write("One successful Login Attempt at: " + str(datetime.datetime.now()) + "\n")
        f.close()
        Label(text="     Correct password      ",bg="white").grid(row=2,column=1,sticky=W,pady=10)
    else:
        f = open(r"logs.txt","a")
        f.write("One Failed Login Attempt at: " + str(datetime.datetime.now()) + "\n")
        f.close()
        Label(text="     Wrong password     ",bg="white").grid(row=2,column=1,sticky=W,pady=10)

#importing everything needed.
     
import os
from tkinter import *
import datetime

#quick designs of the GUI

c = Tk()
c.title("Password checker")
c.geometry("300x100")
c.configure(bg="white")
Label(text="password: ",bg="white").grid(row=0,column=0,sticky=E,pady=10)

# the entry and the binding

password = StringVar()
binding = Entry(textvariable=password,show="*")
binding.grid(row=0,column=1,sticky=W,pady=10)
binding.bind("<Return>",check1)

#the button to check the password

Button(text="Check",bg="white",command=check).grid(row=1,column=1,sticky=E)



