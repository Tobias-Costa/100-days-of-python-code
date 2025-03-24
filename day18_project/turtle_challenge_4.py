# Draw a random walk

import turtle as t
from random import choice, randint

tim = t.Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)


for _ in range(200):
    direction = choice([0,90,180,270])
    tim.pencolor(random_color())
    tim.setheading(direction)
    tim.forward(30)



screen = t.Screen()
screen.exitonclick()