from turtle import *

shape("turtle")
wheel=400
bgcolor("yellow")
pensize(4)


colors = ['red', 'purple', 'blue', 'green', 'purple', 'pink', 'orange']
for x in range(wheel):
    pencolor(colors[x % 6])
    forward(100)
    left(90)
    forward(100)
    right(200)
    forward(400)
    home()
   
