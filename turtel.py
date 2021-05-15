import turtle

t=turtle.Turtle()


turtle.bgcolor('black')

turtle.pensize(2)

turtle.speed(12)

while(True):
    for i in range(6):
        for color in ["red","blue","magenta","green","yellow","white"]:
            turtle.color(color)
            turtle.circle(100)
            turtle.left(10)

turtle.hideturtle()
turtle.mainloop()