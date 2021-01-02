# programs needed to check the number

def check():
    if withdraw.get() % 50 == 0 or a == True:
        m = int(round(withdraw.get()/50.0)*50.0)
        b.delete(0,END)
        b.insert(END,str(m) + " withdrawn")
        f = open(r"logs.txt","a")
        f.write("Someone Tried to withdraw: " + str(withdraw.get()) + ". at: " + str(datetime.datetime.now()) + ". It was successful.\n")
        f.close()
        withdraw.set("")
    else:
        Label(text="Amount not okay").grid(row=3,column=0)
        f = open(r"logs.txt","a")
        f.write("Someone Tried to withdraw: " + str(withdraw.get()) +  ". at: "  + str(datetime.datetime.now()) + ". It was unsuccessful\n")
        f.close()



def check1(event):
    if withdraw.get() % 50 == 0 or a == True:
        m = int(round(withdraw.get()/50.0)*50.0)
        b.delete(0,END)
        b.insert(END,str(m) + " withdrawn")
        f = open(r"logs.txt","a")
        f.write("Someone Tried to withdraw: " + str(withdraw.get()) + ". at: " + str(datetime.datetime.now()) + ". It was successful.\n")
        f.close()
        withdraw.set("")
    else:
        Label(text="Amount not okay").grid(row=3,column=0)
        f = open(r"logs.txt","a")
        f.write("Someone Tried to withdraw: " + str(withdraw.get()) +  ". at: "  + str(datetime.datetime.now()) + ". It was unsuccessful\n")
        f.close()

# Importing everything
        
from tkinter import *
import os
import datetime
import math
# Basic designs


gui = Tk()
gui.geometry("220x100")
gui.title("Popular lists")
gui.configure(bg="white")

# Label telling the user what he needs

Label(text="Enter the amount you want to withdraw.").grid(row=0,column=0)

# The entry and the binding

withdraw = IntVar()
b = Entry(textvariable=withdraw)
b.grid(row=1,column=0)
b.bind("<Return>",check1)

# The button

Button(text="Withdraw",command=check).grid(row=2,column=0)

a = isinstance(withdraw.get() / 50,float)
b = Listbox(height=1)
b.grid(row=3,column=0)

mainloop()