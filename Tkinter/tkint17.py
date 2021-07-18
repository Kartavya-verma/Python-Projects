from tkinter import *

root=Tk()
root.geometry("455x233")
root.title("Scroll Bar")

#For connecting a scrollbar to a widget
#1.widget(yscrollcommand=scrollbar.set)
#2.scrollbar.config(command=widget.yview)

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item{i}")

listbox.pack(fill=BOTH,padx=22)
scrollbar.config(command=listbox.yview)

root.mainloop()