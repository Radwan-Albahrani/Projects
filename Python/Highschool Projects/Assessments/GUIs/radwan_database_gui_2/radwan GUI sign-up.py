
# Importing everything needed

from pbkdf2 import crypt
import datetime
import sqlite3        
from tkinter import *

# a program that binds the <enter> button to the cpassword.

def event(event):
        result = messagebox.askquestion(title="Check",message="Are you sure you want to Sign-Up",icon="question")
        if result == "yes":
            item_1 = email.get()
            item_2 = password.get()
            item_3 = cpassword.get()
            if item_1 == "" or item_2 == "" or item_3 == "":
                info = messagebox.showinfo("Requirements","Please Fill All Required Fields")
            elif item_2 != item_3:
                    info = messagebox.showinfo("Requirements","Passwords don't match")

            else:
                info2 = messagebox.showinfo("Confirmed","Sign-Up Completed")
                a = StringVar()
                a.set(crypt(password.get()))
                connect = sqlite3.connect(r"my_data\users.db")
                cursor = connect.cursor()
                cursor.execute("insert into users (email, password, timestamp) values (?,?,?)", (email.get(), a.get(),datetime.datetime.now()))
                connect.commit()
                f = open(r"logs\logs.txt","a")
                f.write(email.get() + " Signed up at: " + str(datetime.datetime.now()) + "\n")
                f.close()
                email.set("")
                password.set("")
                cpassword.set("")
        else:
            noinfo1 = messagebox.showinfo("Canceled","Operation Canceled") 
        return

# A program that helps the add button work after checking the fields.

def add():
        result = messagebox.askquestion(title="Check",message="Are you sure you want to Sign-Up",icon="question")
        if result == "yes":
            item_1 = email.get()
            item_2 = password.get()
            item_3 = cpassword.get()
            if item_1 == "" or item_2 == "" or item_3 == "":
                info = messagebox.showinfo("Requirements","Please Fill All Required Fields")
            elif item_2 != item_3:
                    info = messagebox.showinfo("Requirements","Passwords don't match")

            else:
                info2 = messagebox.showinfo("Confirmed","Sign-Up Completed")
                a = StringVar()
                a.set(crypt(password.get()))
                connect = sqlite3.connect(r"my_data\users.db")
                cursor = connect.cursor()
                cursor.execute("insert into users (email, password, timestamp) values (?,?,?)", (email.get(), a.get(),datetime.datetime.now()))
                connect.commit()
                f = open(r"logs\logs.txt","a")
                f.write(email.get() + " Signed up at: " + str(datetime.datetime.now()) + "\n")
                f.close()
                email.set("")
                password.set("")
                cpassword.set("")
        else:
            noinfo1 = messagebox.showinfo("Canceled","Operation Canceled") 
        return

# GUI Setup for design.

gui = Tk()
gui.geometry("390x200")
gui.title("Hashing program Sign-up")
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
Entry(textvariable=password,width=40,show="*").grid(row=3,column=1,sticky=W,pady=10)

# Student ID label and entry for that.

Label(text="Confirm password: ",bg="white").grid(row=4,column=0,sticky=E,pady=10)
cpassword = StringVar()

# Binding te id with enter

binding = Entry(textvariable=cpassword,width=40,show="*")
binding.grid(row=4,column=1,sticky=W,pady=10)
binding.bind("<Return>",event)

# A button to add to the database.

Button(text='Sign-Up',bg="white",command=add).grid(row=6,column=1,sticky=E)

