from tkinter import *
root=Tk()

root.geometry("655x444")
root.title("KV Coding")
root.wm_iconbitmap("icon.ico")
root.config(background="grey")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")

Button(text="Close",command=root.destroy).pack()


root.mainloop()