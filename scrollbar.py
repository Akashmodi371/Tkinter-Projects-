from tkinter import  *

root=Tk()
root.geometry('800x400')
scrollbar=Scrollbar(root,orient=HORIZONTAL)
scrollbar.pack(side=BOTTOM,fill=X)
i=0
def add():
    global i
    lbx.insert(ACTIVE,f'{i}:-Inserted Here')
lbx=Listbox(root,yscrollcommand=scrollbar.set)
lbx.pack()

lbx.insert(END,'enter here')
Button(root,text='add',command=add).pack()
scrollbar.config(command=lbx.yview)

root.mainloop()