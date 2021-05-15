from tkinter import *
from PIL import Image,ImageTk
root=Tk()
def change():
    # print(f'The width of new window is :-{width.get()}')
    print(f'The height of new window is :-{heightvalue.get()}')
    print(f'The width of new window is :-{widthvalue.get()}')
    root.geometry(f'{widthvalue.get()}x{heightvalue.get()}')

    # return root.geometry(f'{canvas_width}x{canvas_heigt}')
width=Label(root,text='canvas_width',pady=10,font='helvatika 16 bold').grid(row=1,column=0)
height=Label(root,text='canvas_height',pady=30,padx=40,font='helvatika 16 bold').grid(row=3,column=0)

# canvas_widget=Canvas(root,width=400,height=300).grid()
# canvas_widget.pack()

widthvalue=StringVar()
heightvalue=StringVar()

width=Entry(root,textvariable=widthvalue).grid(row=1,column=1)
height=Entry(root,textvariable=heightvalue).grid(row=3,column=1)

Button(text="Chagewindowsize",command=change).grid()

root.mainloop()