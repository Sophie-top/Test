import turtle as t


def draw_house(x: int, y: int, height: int, width: int):
    """
        Рисует дом в координатах Х и Y;
        X и Y - координаты средней нижней точки фундамента
        height - полная высота дома( фундамент, крыша и стены)
        width - ширина дома 
    """
    t.shape("turtle")
    t.speed("")
    t.penup()

    #счет параметров
    foundation_height = height * 0.05
    foundation_line_color = "#000"
    foundation_fill_color = "#ff0000"
    #стены
    wall_plus_roof_height = height * 0.95
    wall_height = wall_plus_roof_height * 0.62
    wall_line_color = "#000"
    wall_fill_color = "#00ff00"
    #крыша
    roof_height = wall_plus_roof_height * 0.38
    roof_width = width / 2 * 1.3
    roof_line_color = "#000"
    roof_fill_color = "#0000ff"
    print(f"Дом нарисован в X {x} и Y {y}, высотой {height}, шириной {width}")

    def draw_rectangle(x, y, height,  width, line_color, fill_color):
        """
        TODO
        """
        t.color(line_color, fill_color)
        t.goto(x, y)
        t.pendown()
        t.fd(width / 2)
        t.lt(90)
        t.fd(height)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        t.fd(height)
        t.lt(90)
        t.fd(width / 2)
        t.end_fill()
        t.penup()
        

    def draw_foundation():
        #TODO Выделить цвета в переменные
        #line_color, fill_color
        draw_rectangle(0, 0, foundation_height, width, foundation_line_color, foundation_fill_color)


        print(f"Нарисовал фундамент в X {x} и Y {y}")

    
    def draw_walls():
        #x, y, height,  width, line_color, fill_color
        draw_rectangle(x, y + foundation_height,  wall_height, width, wall_line_color, wall_fill_color )



    def draw_roof():
        t.color(roof_line_color, roof_fill_color)
        t.goto(x, y + foundation_height + wall_height, )
        t.pendown()
        t.fd(roof_width)

        t.penup()

    draw_foundation()
    draw_walls()
    draw_roof()

draw_house(0, 0, 300, 500)
t.mainloop()