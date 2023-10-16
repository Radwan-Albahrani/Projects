# Importing everything needed

import datetime
import sqlite3        
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# A program that puts all students into the list.
def selectoriginal():
    if password.get() == "password":
        sel_list.delete(0,END)
        connection_v = sqlite3.connect(r"my_data\users.db")
        cursor_v = connection_v.cursor()
        All_list1 = cursor_v.execute("select * from Users")
        connection_v.commit()
        for allitems in All_list1:
            sel_list.insert(END,allitems)
def selectoriginal1(event):
    if password.get() == "password":
        sel_list.delete(0,END)
        connection_v = sqlite3.connect(r"my_data\users.db")
        cursor_v = connection_v.cursor()
        All_list1 = cursor_v.execute("select * from Users")
        connection_v.commit()
        for allitems in All_list1:
            sel_list.insert(END,allitems)
    else:
        messagebox.showinfo("Wrong","Wrong Password")
            
        return
def selectall():
    c = 1
    sel_list.delete(0,END)
    connection_v = sqlite3.connect(r"my_data\users.db")
    cursor_v = connection_v.cursor()
    All_list2 = cursor_v.execute("select * from Users")
    connection_v.commit()
    for allitems in All_list2:
        sel_list.insert(END, str(c) + ". " + "Name: " + allitems[1] + " " + allitems[0][0] + "; Time Registered: " + allitems[3][0:10] + ";" + allitems[3][10:16]) 
        c = c + 1
    return

# A program that makes the user browse for images.

def Proimage():
    filedialog.askopenfilename()
    return

# a program that binds the <enter> button to the student id.

def event(event):
        result = messagebox.askquestion(title="Check",message="Are you sure you want to add this student?",icon="question")
        if result == "yes":
            item_1 = firstname.get()
            item_2 = lastname.get()
            item_3 = student_id.get()
            if item_1 == "" or item_2 == "" or item_3 == "":
                info = messagebox.showinfo("Requirements","Please Fill All Required Fields")
            else:
                info2 = messagebox.showinfo("Confirmed","Preorder added to database")
                connect = sqlite3.connect(r"my_data\users.db")
                cursor = connect.cursor()
                cursor.execute("insert into users (lname, fname, studentid,timestamp) values (?,?,?,?)", (lastname.get(), firstname.get(), student_id.get(),datetime.datetime.now()))
                connect.commit()
                firstname.set("")
                lastname.set("")
                student_id.set("")
        else:
            noinfo1 = messagebox.showinfo("Canceled","Operation Canceled") 
        return

# A program that helps the add button work after checking the fields.

def add():
        result = messagebox.askquestion(title="Check",message="Are you sure you want to preorder this game?",icon="question")
        if result == "yes":
            item_1 = firstname.get()
            item_2=lastname.get()
            item_3 = student_id.get()
            if item_1 == "" or item_2 == "" or item_3 == "":
                info = messagebox.showinfo("Requirements","Please Fill All Required Fields")
            else:
                info2 = messagebox.showinfo("Confirmed","preorder added to database")
                
                connect = sqlite3.connect(r"my_data\users.db")
                cursor = connect.cursor()
                cursor.execute("insert into users (lname, fname, studentid, timestamp) values (?,?,?,?)", (lastname.get(), firstname.get(), student_id.get(),datetime.datetime.now()))
                connect.commit()
                firstname.set("")
                lastname.set("")
                student_id.set("")
        else:
            noinfo1 = messagebox.showinfo("Canceled","Operation Canceled") 
        return


# A program That deletes A selected student from the Database.

def delete():
    result2 = messagebox.askquestion(title="Check",message="Are you sure you want to cancel this preorder?",icon="question")
    if result2 == "yes":
        again = messagebox.askquestion(title="Are you sure?",message="This preorder will be canceled permenantly, are you still sure you want to cancel this preorder?",icon="question")
        if again == "yes":
            again2 = messagebox.askquestion(title="No turning back",message="Are you sure you want to cancel this preorder permenantly?",icon="warning")
            if again2 == "yes":
                info2 = messagebox.showinfo("confirmed","preorder Canceled permenantly")
                connect = sqlite3.connect(r"my_data\users.db")
                cursor = connect.cursor()
                listitems = sel_list.get(ACTIVE)


                cursor.execute("DELETE from users where lname=? and fname=? and studentid=? and timestamp=?", (listitems[0],listitems[1],listitems[2],listitems[3]))
                connect.commit()
                cursor.close()
                c = 1
                sel_list.delete(0,END)
                connection_v = sqlite3.connect(r"my_data\users.db")
                cursor_v = connection_v.cursor()
                All_list2 = cursor_v.execute("select * from Users")
                connection_v.commit()
                for allitems in All_list2:
                    sel_list.insert(END, str(c) + ". " + "Name: " + allitems[1] + " " + allitems[0][0] + ". Time Registered: " + allitems[3][0:10] + "; " + allitems[3][10:16]) 
                    c = c + 1
            else:
                noinfo = messagebox.showinfo("Canceled","Operation canceled")
        else:
            noinfo2 = messagebox.showinfo("Canceled","Operation canceled")
    else:
        noinfo3 = messagebox.showinfo("Canceled","Operation canceled")
    return



# GUI Setup for design.

gui = Tk()
gui.geometry("390x685")
gui.title("Fan Game Preorder Sign-up")
gui.iconbitmap(r"icons\index.ico")
gui.configure(bg="white")

# Image inserting on to the GUI.

image = PhotoImage(file=r"Backgrounds\image.gif")
Label(image=image,bg="white").grid(row=0,columnspan=2)

# Info about what you need to do.

Label(text="Please enter all data below",bg="white").grid(row=1,column=1,sticky=W,pady=10)

# Last name label and entry for that.

Label(text="Last Name: ",bg="white").grid(row=2,column=0,sticky=E,pady=10)
lastname = StringVar()
Entry(textvariable=lastname,width=40).grid(row=2,column=1,sticky=W,pady=10)

# First name label and entry for that.

Label(text="First Name: ",bg="white").grid(row=3,column=0,sticky=E,pady=10)
firstname = StringVar()
Entry(textvariable=firstname,width=40).grid(row=3,column=1,sticky=W,pady=10)

# Student ID label and entry for that.

Label(text="PSN/Xbox ID: ",bg="white").grid(row=4,column=0,sticky=E,pady=10)
student_id = StringVar()

# Binding te id with enter

binding = Entry(textvariable=student_id,width=40)
binding.grid(row=4,column=1,sticky=W,pady=10)
binding.bind("<Return>",event)

# A button to add to the database.

Button(text='Preorder',bg="white",command=add).grid(row=6,column=1,sticky=E)

# The Show all preorders original button

Label(text="Show original password: ",bg="white",).grid(row=5,column=0,sticky=E,pady=10)

#Binding in the password entry

password = StringVar()
binding2 = Entry(textvariable=password,width=40,show="*")
binding2.grid(row=5,column=1,sticky=W,pady=10)
binding2.bind("<Return>",selectoriginal1)

# A button that shows original

Button(text="Show original Preorders",bg="white",command=selectoriginal).grid(row=6,column=0,pady=10)

# A listbox showing what is on the database.

sel_list = Listbox(width=57)
sel_list.grid(row=8,columnspan=2,pady=10)

# A Button to deletes a selected student from the database.

Button(text="Cancel Preorder (must show original)",bg="white",command=delete).grid(row=9,column=1,sticky=E,pady=10)

# A Button to Show all Students in the database.

Button(text="Show All Preorders",bg="white",command=selectall).grid(row=9,column=0,pady=10)

mainloop()
