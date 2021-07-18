from tkinter import *
root=Tk()

root.geometry("444x233")
root.title("My GUI WITH KV")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title=Label(text="PIL is the Python Imaging Library \nwhich provides the python interpreter with image \nediting capabilities. It was developed by Fredrik \nLundh and several other contributors. Pillow is the \nfriendly PIL fork and an easy to use library \ndeveloped by Alex Clark and other contributors.",bg="red",fg="white",padx=23,pady=94,font=("comicsansms",19,"bold"))

title.pack(side=LEFT,fill=X)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

root.mainloop()
