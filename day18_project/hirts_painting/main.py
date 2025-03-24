import turtle as t
from random import choice

turtle = t.Turtle()
turtle.penup()
turtle.speed("fastest")
turtle.hideturtle()
t.colormode(255)
turtle.setx(-250)
turtle.sety(-250)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

y = -250
for _ in range(10): # Linhas
    for _ in range(10): # Colunas
        turtle.dot(20, choice(color_list))
        turtle.forward(50)
    y += 50
    turtle.sety(y)
    turtle.setx(-250)


screen = t.Screen()
screen.exitonclick()