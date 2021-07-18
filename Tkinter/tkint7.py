from tkinter import *

root=Tk()
root.geometry("655x333")

def getvals():
    print("The user name is",uservalue.get())
    print("The password is",passvalue.get())

user=Label(root,text="Username")
password=Label(root,text="Passwrod")

user.grid()
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()