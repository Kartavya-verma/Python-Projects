from tkinter import *

root=Tk()
root.geometry("655x333")

def getvals():
    print("It works")

Label(root,text="Welcome to KV Travels",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
payment=Label(root,text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymententry=Entry(root,textvariable=paymentmodevalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#Checkbox & packing it
foodservice=Checkbutton(text="Want to prebook your meal ?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

#Button & packing it & assigning it a command
Button(text="Submit to KV travels",command=getvals).grid(row=7,column=3)

root.mainloop()