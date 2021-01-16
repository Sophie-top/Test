from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

window.fullscreen = True



# create a window
app = Ursina()

player = PlatformerController2d(position = (0, -2),
                                collision = True,
                                )


for i in range(11):
    counter
    for j in range(6):
        tile =  Entity(model = "quad",
                       x = counter,
                       y = 
                       )
        counter += 1


app.run()
