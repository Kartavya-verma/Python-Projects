from tkinter import *

root=Tk()
root.title("KV's GUI")
root.geometry("644x334")

def kv(event):
    print(f"You clicked on the button at {event.x},{event.y}")

widget=Button(root,text="Click me")
widget.pack()

widget.bind('<Button-1>',kv)
widget.bind('<Double-1>',quit)


root.mainloop()