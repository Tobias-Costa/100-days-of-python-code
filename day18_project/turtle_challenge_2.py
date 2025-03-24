# Draw a dashed line

import turtle as t

tim = t.Turtle()
tim.shape("turtle")

for i in range(30):
    if i % 2 == 0:
        tim.pu()
    else:
        tim.pd()
    tim.fd(10)

screen = t.Screen()
screen.exitonclick()