import turtle as t
import math

draw_rectangle(-250, , height,  width, line_color, fill_color):
       

def draw_street(line_number , house_number, house_x, house_width, house_height, house_y):
    for i in range(line_number):
        for x in range(house_number):
            draw_house(house_x, house_y, house_width, house_height)
            house_x += house_width * 2
        house_x += -500
        house_y += house_height
        draw_ways()
        house_y += house_height

  


def draw_house(x: int, y: int, width: int, height: int):


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

    


    def draw_foundation():
        #TODO Выделить цвета в переменные
        #line_color, fill_color
        draw_rectangle(x, y, foundation_height, width, foundation_line_color, foundation_fill_color)


        print(f"Нарисовал фундамент в X {x} и Y {y}")


    def draw_walls():
        #x, y, height,  width, line_color, fill_color
        draw_rectangle(x, y + foundation_height,  wall_height, width, wall_line_color, wall_fill_color )



    def draw_roof():
        t.begin_fill()
        t.color(roof_line_color, roof_fill_color)
        t.goto(x, y + foundation_height + wall_height, )
        t.pendown()
        t.fd(roof_width)
        t.goto(x, y + foundation_height + wall_height + roof_height )
        t.goto(x - roof_width, y + foundation_height + wall_height)
        t.goto(x, y + foundation_height + wall_height)
        t.end_fill()
        t.penup()

    draw_foundation()
    draw_walls()
    draw_roof()


draw_street(7, 5, -200, 50, 60, 3)

t.mainloop()