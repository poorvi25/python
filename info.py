from Tkinter import *
from tkMessageBox import*
root=Tk()
Label(root,text="Name:Poorvi shrivastav",font="times 20 bold italic").grid(row=1,column=0)
Label(root,text="Batch=BY/B-5",font="times 20 bold italic").grid(row=2,column=0)
Label(root,text="Er. No.:161B142",font="times 20 bold italic").grid(row=3,column=0)
Label(root,text="Project name:PROJECT ON SALES MANAGEMENT M.P.",font="times 20 bold italic").grid(row=4,column=0)
def fun():
    showinfo("project info","Project based on sales management of M.P...the amount of particular tea sold by an employee based on their empoylee i.d.") 
Button(root,text="PROJECT INFO",command=fun).grid(row=5,column=0)
root.mainloop()

