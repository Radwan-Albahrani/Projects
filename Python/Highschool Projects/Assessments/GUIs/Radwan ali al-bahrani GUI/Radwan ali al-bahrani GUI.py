users = ["radwan","rayan","ahmed","Radwan","Rayan","Ahmed"]

def user():
    if username.get() in users:
        Label(text=" Welcome ",fg='white',bg='black',font='Aharoni''20').grid(row=5,column=0)
        username.set("")
    else:
        Label(text="Invalid User",fg='white',bg='black',font='Aharoni''20').grid(row=5,column=0)
        username.set("")
def close():
    iqamas.destroy()
    return


from tkinter import *

iqamas = Tk()
iqamas.geometry("600x500")
iqamas.title("Naruto's Fans - Login")
iqamas.iconbitmap(r"icons\url.ico")
iqamas.configure(bg='black')

image = PhotoImage(file=r"Backgrounds\maxresdefault.gif")
Label(image=image).grid(row=0,columnspan=10)

Label(text="Enter your name:",fg='white',bg='black',font='Aharoni''20').grid(row=3,column=0)

username = StringVar()
Entry(textvariable=username).grid(row=3,column=1)

Button(text='Submit',command=user,fg='white',bg='black',font='Aharoni''20').grid(row=4,column=0)
Button(text='close',command=close,fg='white',bg='black',font='Aharoni''20').grid(row=4,column=1)






