import turtle
turtle.reset()
turtle.shape("classic")

def draw_dashed_line(total:int, color:str):
	for i in range(total):
		turtle.fillcolor(color)
		turtle.pendown()
		turtle.fd(10)
		turtle.penup()
		turtle.fd(10)


draw_dashed_line(20, "red")

turtle.mainloop()
