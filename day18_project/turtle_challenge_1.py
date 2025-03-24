#Draw a square

from turtle import Turtle, Screen

turtle =  Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("green")

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

screen.exitonclick()