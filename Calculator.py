from tkinter import *
from tkinter import font
root=Tk()

root.geometry('450x640')
root.maxsize(450,640)
root.minsize(450,640)
root.title('CALCULATOR')
myFont = font.Font(family = 'Helvetica', size = 20)
root.wm_iconbitmap('2..ico')
root.configure(background='grey')

def click(event):
    text=event.widget.cget('text')
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                value="error"
        scvalue.set(value)
        Screen.update()
    elif text=='C':
        scvalue.set('')
        Screen.update(scvalue)
    else:
        scvalue.set(scvalue.get() + text)
        Screen.update()
scvalue=StringVar()
scvalue.set('')
Screen=Entry(root,textvar=scvalue,font='lucida 20 bold',bg='lightyellow').pack(fill=X,ipadx=30,ipady=30,pady=10,padx=20)
#TODO:ButtonsHere(7-8-9-4-5-6)
f0=Frame(root,bg='lightblue')
b=Button(f0,text='7',padx=10,pady=10,font='lucida 20 bold',relief=FLAT)
b.pack(padx=10,side=LEFT)
b.bind('<Button-1>',click)

b=Button(f0,text='8',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT)
b.bind("<Button-1>",click)

b=Button(f0,text='9',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT)
b.bind("<Button-1>",click)

b=Button(f0,text='*',padx=20,font='lucida 25 bold',relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT,fill=X)
b.bind('<Button-1>',click)

b=Button(f0,text='+',padx=10,pady=5,font='lucida 20 bold',relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT)
b.bind("<Button-1>",click)

f0.pack(pady=10)

f0=Frame(root,bg='lightblue')
b=Button(f0,text='4',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT)
b.bind('<Button-1>',click)

b=Button(f0,text='5',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT)
b.bind("<Button-1>",click)

b=Button(f0,text='6',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT)
b.bind('<Button-1>',click)

b=Button(f0,text='/',padx=20,font='lucida 25 bold',relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT,fill=X)
b.bind('<Button-1>',click)

b=Button(f0,text='-',padx=10,pady=5,font='lucida 20 bold',relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT)
b.bind("<Button-1>",click)
f0.pack(pady=10)
#TODO:ButtonsHere(1-2-3-0-.)
f0=Frame(root,bg='lightblue')
b=Button(f0,text='1',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT,anchor='nw')
b.bind('<Button-1>',click)

b=Button(f0,text='2',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT,anchor='nw')
b.bind("<Button-1>",click)

b=Button(f0,text='3',padx=10,pady=10,font='lucida 20 bold',height=1,relief=FLAT)
b.pack(padx=10,pady=20,side=LEFT,anchor='nw')
b.bind("<Button-1>",click)

b=Button(f0,text='0',padx=20,pady=0,font=myFont)
b.pack(padx=10,pady=20,side=LEFT,fill=X)
b.bind('<Button-1>',click)

b=Button(f0,text='.',padx=10,pady=5,font='lucida 20 bold')
b.pack(padx=10,pady=20,side=LEFT)
b.bind("<Button-1>",click)

f0.pack(pady=10)


f0=Frame(root,bg='lightblue')
b=Button(f0,text='Enter',padx=20,pady=10,font='lucida 10 bold',relief=RAISED,bd=4)
b.pack(padx=20,pady=5,side=LEFT,fill=X,anchor='sw')
b.bind('<Button-1>',click)

b=Button(f0,text='C',padx=20,pady=10,font='lucida 10 bold',relief=SUNKEN,bd=5,bg='yellow')
b.pack(padx=20,pady=5,side=LEFT,fill=X,anchor='sw')
b.bind('<Button-1>',click)

b=Button(f0,text='=',padx=20,pady=10,font='lucida 20 bold',relief=RAISED,bg='grey')
b.pack(padx=30,pady=5,side=LEFT,fill=X,anchor='sw')
b.bind('<Button-1>',click)

f0.pack(pady=10)
f2=Frame(root,bg='black')
a=Label(root,text='Created BY:- Aakash Modi',font='lucida 12 italic',fg='white',bg='black')
a.pack(fill=X,anchor='se',side=RIGHT)
f2.pack()




root.mainloop()