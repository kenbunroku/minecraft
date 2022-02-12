from ursina import *

app = Ursina()

test_square = Entity(model='quad', color=color.red, scale = (1,4), position = (5,1))

app.run()
