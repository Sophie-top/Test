import turtle as t


def draw_house(х: int, y: int, height: int, width: int, ):
'''Рисует дом в координатах Х и Y;
   X и Y - координаты средней нижней точки фундамента
   height - полная высота дома( фундамент, крыша и стены)
   width - ширина дома'''

    print(f"Дом нарисован в X {x} и Y {y}, height {height}, width {width}")
    def draw_foundation():
        foundation_height = height * 0.05
        t.shape("turtle")
        t.speed("fast")
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fd(width / 2)
        t.lt(90)
        t.fd(foundation_height)
        t.lt(90)
        t.fd(width / 2)
        t.lt(90)
        t.fd(foundation_height)
        t.
        t.mainloop()
        print(f"Нарисовал фундамент в X {x} и Y {y}")
    def draw_walls():
        pass
    def draw_roof():
        pass



draw_house(0, 000, 300, 500)