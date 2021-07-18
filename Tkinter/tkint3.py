from tkinter import *
from PIL import Image,ImageTk
root=Tk()

root.geometry('755x344')

#For PNG
#photo=PhotoImage(file="earth.png")

#For JPG
image=Image.open("1.jpg")
photo=ImageTk.PhotoImage(image)

label=Label(image=photo)
label.pack()


root.mainloop()