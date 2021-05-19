from tkinter import *
import time

def times():
    current_time=time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

root=Tk()
root.config(background='black')
root.geometry('540x265')

clock=Label(root,font='times 50 bold',bg='black',fg='blue')
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text='DIGITAL CLOCK',font='times 24 bold',bg='black',fg='grey')
digi.grid(row=0,column=2)

nota=Label(root,text='Hour,Minute,seconds',font='helvetika 24 bold',bg='black',fg='yellow')
nota.grid(row=3,column=2)
created=Label(root,text='Created By :- Aakash Modi',font='Fixedsys 24 bold',bg='black',fg='grey')
created.grid(row=4,column=2)
root.mainloop()