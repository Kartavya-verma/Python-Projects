from tkinter import *
root=Tk()
root.geometry("733x566")
root.title("Pycharm")

def myfun():
    print("My Function")

# Used to create a non dropdown menu
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myfun)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

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


root.mainloop()