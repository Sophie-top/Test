import turtle as t


def draw_house(x: int, y: int, height: int, width: int):
    """
        Рисует дом в координатах Х и Y;
        X и Y - координаты средней нижней точки фундамента
        height - полная высота дома( фундамент, крыша и стены)
        width - ширина дома 
    """
    t.shape("turtle")
    t.speed("fast")
    t.penup()

    #счет параметров
    foundation_height = height * 0.05
    walls_plus_roof_height = height * 0.95
    wall_height = walls_plus_roof_height * 0.62

    print(f"Дом нарисован в X {x} и Y {y}, высотой {height}, шириной {width}")

    def draw_foundation():
        #TODO
        t.color("#000", "#888")
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.fd(width / 2)
        t.lt(90)
        t.fd(foundation_height)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        t.fd(foundation_height)
        t.lt(90)
        t.fd(width / 2)
        t.end_fill()
        t.penup()

        print(f"Нарисовал фундамент в X {x} и Y {y}")
    
    def draw_walls():
        t.begin_fill()
        t.goto(x, y + foundation_height)
        t.color("#000", "#B73239")
        t.pendown()
        t.fd(width / 2)
        t.lt(90)
        t.fd(wall_height)
        t.lt(90)
        t.fd(width)
        t.lt(90)
        t.fd(wall_height)
        t.lt(width / 2)
        t.end_fill()
        t.penup()


    def draw_roof():
        pass

    draw_foundation()
    draw_walls()

draw_house(0, 0, 300, 500)
t.mainloop()



