from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("455x233")
root.title("Radio Button")

def order():
    tmsg.showinfo("Order Received", f"You have received your order for {var.get()}.Thanks for Ordering")


# var=IntVar()
# var.set(1)
var=StringVar()
var.set("Radio")

Label(root,text="What would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()

radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio=Radiobutton(root,text="Idli",padx=14,variable=var,value="Idli").pack(anchor="w")
radio=Radiobutton(root,text="Sambhar",padx=14,variable=var,value="Sambhar").pack(anchor="w")
radio=Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack(anchor="w")

Button(text="Order Now",command=order).pack()

root.mainloop()