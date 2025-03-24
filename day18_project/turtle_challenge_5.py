# Draw a spyrograph

import turtle as t
from random import choice, randint

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

angle = 0
while angle <= 360:
    tim.pencolor(random_color())
    tim.setheading(angle)
    tim.circle(100)
    angle += 5

screen = t.Screen()
screen.exitonclick()