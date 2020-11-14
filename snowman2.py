import turtle
turtle.shape("turtle")
turtle.speed("fastest")
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()


def draw_circle(circles: 10, lower: int, firts_color:int):
    for i in range(circles):
        turtle.colormode(255)
        turtle.color(0, 0, firts_color)
        turtle.begin_fill()
        turtle.circle(lower)
        turtle.penup()
        turtle.lt(90)
        turtle.forward(lower * 2)
        turtle.pendown()
        turtle.rt(90)
        lower *= 0.75
        firts_color += 40
        turtle.end_fill()
    turtle.forward(lower)
    turtle.lt(110)
    turtle.fd(lower * 1.5)
    turtle.lt(70)
    turtle.fd(lower)
    turtle.lt(70)
    turtle.fd(lower * 1.5)
    turtle.lt(110)
    turtle.fd(lower)



draw_circle(3, 100, 90)
turtle.mainloop()    