users = ["radwan","rayan","ahmed","Radwan","Rayan","Ahmed"]
from tkinter import *

iqamas = Tk()
iqamas.geometry("210x170")
iqamas.title("Login")
iqamas.iconbitmap(r"icons\url.ico")

frame1 = Frame(height=30,width=210,bg="dark gray").grid(row=0,columnspan=10)

frame2 = Frame(height=190,width=210).grid(rowspan=10,columnspan=10)

Label(frame1,text=" Sign-up ",font='Aharoni''20').grid(row=0,columnspan=5)

Label(frame2,text="Username:",font='Aharoni''20').grid(row=1,column=0)

username = StringVar()
Entry(frame2,textvariable=username).grid(row=1,column=1)

Label(frame2,text="Password:",font='Aharoni' '20').grid(row=2,column=0)

Password = StringVar()
Entry(frame2,textvariable=Password).grid(row=2,column=1)



def user():
    if username.get() in users:
        Label(frame2,text=" Welcome ",font='Aharoni''20').grid(row=4,column=1)
        username.set("")
        Password.set("")
    else:
        Label(frame2,text="Invalid User",font='Aharoni''20').grid(row=4,column=1)
        username.set("")
        Password.set("")
def close():
    iqamas.destroy()
    return

Button(frame2,text='Login',command=user,font='Aharoni' '20').grid(row=3,column=1)








