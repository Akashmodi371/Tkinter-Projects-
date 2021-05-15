import turtle






from tkinter import *
import tkinter.messagebox as msgb
root = Tk()
root.geometry("733x566")
root.title("Pycharm")
def myfunc():
   pass

def kholo():
   a= msgb.showinfo('Here is you distance', f'You move {myslider.get()} km distance')
   if a=='ok':
        t=turtle.Turtle()
        turtle.bgcolor('lightblue')

        turtle.pensize(5)

        turtle.speed(22)

        while(True):
            for i in range(6):
                for color in ["blue","magenta","green","yellow","white"]:
                    turtle.color(color)
                    turtle.circle(500)
                    turtle.left(20)

        turtle.hideturtle()
        turtle.mainloop()

   else:
        pass
Label(root, text='slide down how much you want to move').pack()
myslider = Scale(root, from_=0, to=100, orient=HORIZONTAL,tickinterval=50)
myslider.set(30)
myslider.pack()
Button(root,text='move',command=myfunc).pack()
# msgb.showinfo('Here is you distance', f'You move {myslider.get()} km distance')


# a=msgb.askquestion('Questions for you','Do you want to move from here?')
# if a=='yes':


# def kholo():
#    # a= msgb.showinfo('no you are not right','yes we will')
#    # print(a)
#    a=msgb.askquestion('is that right','you work there')
#    print(a)
#
#    if a=='no':
#        print('To krona bhai')
#    else:
#        print('great')
#        d=msgb.showinfo('good','you are nice person who dont work')
#        if d=='ok':
#            msgb.showwarning('right','Abe sidhe re le re')
#            e=msgb.askokcancel('you can do','is it true?')
#            print('value here is ',e)
#        else:
#            print('Chal nikal bete ')

# #Use these to create a non dropdown menu# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


mainmenu = Menu(root)

m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
m1.add_separator()
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Cut", command=myfunc)
m3.add_command(label="Copy", command=myfunc)
m3.add_separator()
m3.add_command(label="Paste", command=myfunc)
m3.add_command(label="Kholo", command=kholo)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="print", menu=m3)
root.mainloop()

