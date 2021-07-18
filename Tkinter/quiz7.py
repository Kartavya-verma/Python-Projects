from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("455x233")
root.title("Slider")

def rate():
        if(myslider2.get()>5):
            tmsg.showinfo("Thank You",f"You have given {myslider2.get()} stars to our service")
        else:
            tmsg.showinfo("Thank You", f"You have given {myslider2.get()} stars to our service.We will improve our service")

# myslider=Scale(root,from_=0,to=100)
# myslider.pack()

Label(root,text="Please Rate our service").pack()
myslider2=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=1,length=100)
myslider2.set(5)
# myslider2.grid_size(100)
myslider2.pack()

Button(root,text="Submit",pady=10,command=rate).pack()

root.mainloop()