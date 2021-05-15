from tkinter import  *

root=Tk()
i=0
def add():
    global i
    lbx.insert(ACTIVE,f'{i}:-Inserted Here')
lbx=Listbox(root)
lbx.pack()

lbx.insert(END,'enter here')
Button(root,text='add',command=add).pack()
root.geometry('800x400')

root.mainloop()