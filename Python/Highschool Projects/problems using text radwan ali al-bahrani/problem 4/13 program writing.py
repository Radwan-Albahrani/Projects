#programs needed to check the chosen activity

def checker():
    f = open(r"logs.txt","a")
    f.write("Someone chose: " + Activities.get() + ". he did that at: " + str(datetime.datetime.now()) + "\n")
    f.close()
    Label(text="Thank you for your cooperation, you can quit now.",bg="white").grid(row=3,column=0)

#importing everything needed

from tkinter import *
import os
import datetime

#basic GUI design

gui = Tk()
gui.geometry("445x100")
gui.title("Popular lists")
gui.configure(bg="white")

# A quick Label

Label(text="Please choose your favorite activity (the program will save it automaically)",bg="white").grid(row=0,column=0)

# An options menu

activities = ['Sports','Movie making','Metal melting','Art','Boxing']
Activities = StringVar()
drop = OptionMenu(gui,Activities,*activities)
drop.grid(row=1,column=0) 

# a button

Button(text='check',bg="white",command=checker).grid(row=2,column=1,sticky=E)



