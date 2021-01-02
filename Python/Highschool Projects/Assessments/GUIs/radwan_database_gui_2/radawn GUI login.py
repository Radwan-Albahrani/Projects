
# Importing everything needed

from pbkdf2 import crypt
import datetime
import sqlite3        
from tkinter import *

# a program that binds the <enter> button to the cpassword.

def event(event):
        result = messagebox.askquestion(title="Check",message="Are you sure you want to Sign-Up",icon="question")
# A program that helps the add button work after checking the fields.

def login():
        result = messagebox.askquestion(title="Check",message="Are you sure you want to Sign-Up",icon="question")
# GUI Setup for design.

gui = Tk()
gui.geometry("320x200")
gui.title("Hashing program Login")
gui.configure(bg="white")

# Info about what you need to do.

Label(text="Please enter all data below",bg="white").grid(row=1,column=1,sticky=W,pady=10)

# Last name label and entry for that.

Label(text="Email: ",bg="white").grid(row=2,column=0,sticky=E,pady=10)
email = StringVar()
Entry(textvariable=email,width=40).grid(row=2,column=1,sticky=W,pady=10)

# First name label and entry for that.

Label(text="Password: ",bg="white").grid(row=3,column=0,sticky=E,pady=10)
password = StringVar()

# Binding Password with Enter

binding = Entry(textvariable=password,width=40,show="*")
binding.grid(row=3,column=1,sticky=W,pady=10)
binding.bind("<Return>",event)

# A button to add to the database.

Button(text='Login',bg="white",command=login).grid(row=4,column=1,sticky=E)

