from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("733x566")
root.title("Pycharm")

def myfun():
    print("My Function")

def help():
    print("I will help you!!!")
    a=tmsg.showinfo("Help","KV will help you!!!")

def rate():
    print("Rate us")
    value=tmsg.askquestion("Was your experience Good?","You used this GUI..Was your experience good?")
    if(value=="yes"):
        msg="Great.Rate us on appstore please"
    else:
        msg="Tell us want went wrong.We will call you soon"
    tmsg.showinfo("Experience",msg)

def divya():
    ans=tmsg.askretrycancel("Divya se dosti karlo","Sorry divya nahi banegi aapki dost")
    if ans:
        print("Retry karne par bhi kuch nahi hoga")
    else:
        print("Bohot bhadiya bahi cancel kar diya varna pit-te")

mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New",command=myfun)
m1.add_command(label="Save",command=myfun)
m1.add_separator()
m1.add_command(label="Save As",command=myfun)
m1.add_command(label="Print",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=myfun)
m2.add_command(label="Copy",command=myfun)
m2.add_separator()
m2.add_command(label="Paste",command=myfun)
m2.add_command(label="Find",command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)


m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Befriend Divya",command=divya)
mainmenu.add_cascade(label="Edit",menu=m3)
root.config(menu=mainmenu)

root.mainloop()