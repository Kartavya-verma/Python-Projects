from tkinter import *
root=Tk()

def change():
    root.geometry(f"{width_value.get()}x{height_value.get()}")

#widht x height
root.geometry("200x100")
root.title("KV GUI")

width=Label(root,text="Enter Width")
height=Label(root,text="Enter Height")

width.grid(row=0,column=2)
height.grid(row=1,column=2)

width_value=StringVar()
height_value=StringVar()

width_entry=Entry(root,textvariable=width_value)
height_entry=Entry(root,textvariable=height_value)

width_entry.grid(row=0,column=3)
height_entry.grid(row=1,column=3)

b1=Button(text="Click to change",command=change).grid(row=2,column=3)

root.mainloop()