# Draw different shapes

import turtle as t
from random import choice

tim = t.Turtle()
tim.shape("turtle")
color_list = ["blue","red","green","orange","yellow","purple","pink","aquamarine", "CadetBlue", "DarkSeaGreen"]

def draw_shape(faces):
    color_choice = choice(color_list)
    tim.color(color_choice)
    color_list.remove(color_choice)
    angle = 360 / faces
    for _ in range(faces):
        tim.right(angle)
        tim.forward(100)

draw_shape(3)
draw_shape(4)
draw_shape(5)
draw_shape(6)
draw_shape(7)
draw_shape(8)
draw_shape(9)
draw_shape(10)


screen = t.Screen()
screen.exitonclick()