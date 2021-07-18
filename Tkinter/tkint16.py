from tkinter import *

root=Tk()
root.geometry("455x233")
root.title("List Box Button")

i=0
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"Fisrt item of list box")

Button(root,text="Add Item",command=add).pack()

root.mainloop()