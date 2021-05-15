from tkinter import *
import tkinter.messagebox as msgb

root=Tk()
def submit():
    with open('record.txt',mode='w') as f:
        f.write(f"The experience user is {var.get()}")
        print(f"The experience user is")
root.geometry('500x300')
Label(root,text='How was you experice').pack()
var=StringVar()
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=1)
myslider.pack()
Button(root,text='submit',command=submit).pack()


root.mainloop()