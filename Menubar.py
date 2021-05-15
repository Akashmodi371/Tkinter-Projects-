from tkinter import *

root=Tk()

root.title('mymenu')
root.geometry('800x400')

filemenu=Menu(root)

filemenu.add_command(label='file',command=quit)

root.config(menu=filemenu)
root.mainloop()