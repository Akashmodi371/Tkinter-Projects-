from tkinter import *

root=Tk()
canvas_heigt=500
canvas_width=900

root.geometry(f'{canvas_width}x{canvas_heigt}')

canvas_widget=Canvas(root,width=900,height=466)
canvas_widget.pack()



canvas_widget.create_rectangle(80,80,200,300 , fill='lightblue')

# canvas_widget.create_text(120,90,text='yes i am here')
# canvas_widget.create_oval(170,200,100,100,fill='red')

canvas_widget.create_arc(-40,80,200,515,fill='pink')
canvas_widget.create_line(20,20,100,100)
root.mainloop()