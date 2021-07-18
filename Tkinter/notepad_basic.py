from tkinter import *

root=Tk()
root.geometry("455x233")
root.title("NotePad Basic")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

text=Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)

root.mainloop()