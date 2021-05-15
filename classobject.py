from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x400')

    # def update(self):
    #     self.var.set('new')
    #     self.update()
    #     import time
    #     time.sleep(2)
    #     self.var.set('hello')
    #     self.update()




    def status(self):
        self.var=StringVar()
        self.var.set('Ready')
        self.statusvar=Label(self,textvar=self.var,relief=SUNKEN,anchor='sw')
        self.statusvar.pack(side=BOTTOM,fill=X)
        # Button(self,text='update',command=update).pack()
    def click(self):
        import tkinter.messagebox as tbgm
        self.var.set('Userless')
        self.statusvar=Label(bg='red',text='hello').pack(side=RIGHT)
        self.statusvar=Label(bg='red',text='hello').pack(side=RIGHT,anchor='sw')
        # tbgm.showinfo('Here','yes finaly clicked')

    def createbutton(self):
        Button(text='clickhere',command=self.click).pack()
if __name__ == '__main__':
    window=GUI()
    window.status()
    window.createbutton()
    window.createbutton()
    window.mainloop()