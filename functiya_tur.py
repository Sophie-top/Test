def snowman(color:str, lumps:int, lower:int ):
    for i in range(lumps):
        if lumps <= 20:
            break
        turtle.pencolor(color)
        turtle.begin_fill()
        turtle.circle(lower -= 20)
        turtle.end_fill()