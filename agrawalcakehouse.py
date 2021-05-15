from tkinter import *
from PIL import Image,ImageTk
from datetime import time
root=Tk()

root.geometry('1200x1200')
root.title('Agrawal Cake House Barwaha 451115')

f0=Frame(root,width=800,height=40).pack(padx=50
                                        )
Label(f0,text='Agrawal Cake House Barwaha',font="Courier 40 bold",padx=20).pack()
Label(f0,text='We Provide Cake & Delicious Ice Cream at any',font='BatangChe 20 bold',bg='lightblue',padx=500).pack(pady=10)
texts=[]
photos=[]
for i in range(0,2):
    with open(f'{i+1}.txt') as f:
        text=f.read()
        texts.append(text)
    image = Image.open(f'{i + 1}.jpg')
    # TODO: Resize image
    image = image.resize((200, 200), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))


f1=Frame(root,width=200,heigh=200)
Label(f1,image=photos[0],anchor="n",pady=400).pack(side=TOP,anchor='s',padx=20,pady=5)
Label(f1,text=texts[0]).pack()
f1.pack(side=LEFT,anchor="nw")

f2=Frame(root,width=400,heigh=200)
Label(f2,image=photos[1],anchor="n",pady=400).pack(side=TOP,anchor='s',padx=20,pady=5)
Label(f2,text=texts[0]).pack()
f2.pack(side=LEFT,anchor="nw")


f3=Frame(root,width=800,heigh=400)
Label(f3,image=photos[0],anchor="n",pady=400).pack(side=TOP,anchor='s',padx=20,pady=5)
Label(f3,text=texts[0]).pack()
f3.pack(side=LEFT,anchor="nw")


f4=Frame(root,width=800,heigh=400)
Label(f4,image=photos[1],anchor="n",pady=400).pack(side=TOP,anchor='s',padx=20,pady=5)
Label(f4,text=texts[1]).pack()
f4.pack(side=LEFT,anchor="nw")


root.mainloop()