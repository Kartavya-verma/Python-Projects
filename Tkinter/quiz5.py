from tkinter import *
root=Tk()

root.geometry("655x333")

def f1():
    print("Hello 1")

def f2():
    print("Hello 2")

def f3():
    print("Hello 3")

def f4():
    print("Hello 4")

frame=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame,bg="red",text="Hello",command=f1)
b1.pack(side=LEFT)

b2=Button(frame,bg="pink",text="Hello",command=f2)
b2.pack(side=LEFT)

b3=Button(frame,bg="orange",text="Hello",command=f3)
b3.pack(side=LEFT)

b4=Button(frame,bg="green",text="Hello",command=f4)
b4.pack(side=LEFT)


root.mainloop()