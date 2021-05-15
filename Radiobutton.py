from tkinter import *
import tkinter.messagebox as msgb
root=Tk()

root.geometry("500x500")
def order():
    msgb.showinfo('You order', f"You had order for {var.get()}")

Label(root,text='Order for you food').pack()
var=StringVar()
var.set('radio')
radio=Radiobutton(root,text='dosa',variable=var,value='dosa').pack()
radio=Radiobutton(root,text='paratha',variable=var,value='paratha').pack()
radio=Radiobutton(root,text='khamand',variable=var,value='khamand').pack()
radio=Radiobutton(root,text='khamand',variable=var,value='khamand').pack()
Button(root,text='order now',command=order).pack()


root.mainloop()