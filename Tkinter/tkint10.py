from tkinter import *

root=Tk()

canvas_width=800
canvas_height=400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("KV's GUI")

can_widget= Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

#line (x1,x2,y1,y2)
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

# Order=coordinates of top left & coordinates of bottom right
can_widget.create_rectangle(3,5,700,300,fill="green")

can_widget.create_text(200,200,text="Python")

#we give coordinates of a rectangle for oval
can_widget.create_oval(344,233,244,355)

root.mainloop()