from tkinter import *
from PIL import Image,ImageTk
root=Tk()
def getvals():
    print(f'The name of person is{Name.get()}')
    print(f'The Sirname of person is{Sirname.get()}')
    print(f'The Phonenumber of person is{Phonenumber.get()}')
    print(f'The Gender of person is{Gender.get()}')
    print(f'The Gender of person is{foodserviceno.get()}')
    root.geometry(f'{Name.get()}x{Sirname.get()}')

    with open('record.txt',mode='a') as f:
        f.write(f'Name of the person is : {Name.get()}\n')
        f.write(f'SirName of the person is : {Sirname.get()}\n')

root.maxsize(1400,210)
root.minsize(750,180)

heading=Label(root,text='Urban dance accademy welcomes you',font="comicsansms 20 bold")
heading.grid(row=0,column=3)
Name=Label(root,text="Enter your name",bg='yellow')
Sirname=Label(root,text="Enter your sirname here",bg='red')
Phonenumber=Label(root,text="Enter your phonenumber here",bg='lightblue')
Gender=Label(root,text="Enter your Gender here",bg='pink')
Emergencyno=Label(root,text="Enter your Emergency Number here",bg='grey')
Name.grid(row=1,column=1)
Sirname.grid(row=2,column=1)
Gender.grid(row=3,column=1)
Emergencyno.grid(row=4,column=1)
Phonenumber.grid(row=5,column=1)
# f1=Frame(root,bg='yellow',borderwidth=3,relief=SUNKEN)
# f1.pack(side=LEFT,fill=X)
# F2=Frame(root,bg='lightblue',borderwidth=2,relief=SUNKEN)
# F2.pack(side=TOP,fill=X)
# l1=Label(f1,text="Left side here",bg='white',padx=44,width=20,fg='green',)
# l1.pack(pady=244,anchor='ne')
# l2=Label(F2,text="Agrawal Cake house",bg='white',padx=100,pady=50,width=20,fg='Black'
#          ,borderwidth=1,relief=SUNKEN,font="Helvetika 72 bold")
# l2.pack(pady=44,anchor='s',padx=40)
# b1=Button(f1,text='Hit here',fg='red',bg='black',width=20,command=hello)
# b1.pack(anchor=NE,pady=40)
Name=StringVar()
Sirname=StringVar()
Gender=StringVar()
Emergencyno=StringVar()
Phonenumber=StringVar()
foodserviceno=IntVar()

Nameyear=Entry(root,textvariable=Name).grid(row=1,column=3)
Sirname=Entry(root,textvariable=Sirname)
Gender=Entry(root,textvariable=Gender)
Emergencyno=Entry(root,textvariable=Emergencyno)
Phonenumber=Entry(root,textvariable=Phonenumber)



Sirname.grid(row=2,column=3)
Gender.grid(row=3,column=3)
Emergencyno.grid(row=4,column=3)
Phonenumber.grid(row=5,column=3)
Button(text='submit',command=getvals).grid(row=7,column=2)

# checkbox and its packing
# foodserivce=Label(text='Have read all terms and conditio')
# foodserivce.grid(row=7,column=3)
foodservice=Checkbutton(text='Have read all terms and condition',variable=foodserviceno)
foodservice.grid(row=7,column=3)
root.mainloop()