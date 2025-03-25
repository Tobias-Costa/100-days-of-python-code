from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim_angle = tim.heading()
    tim.setheading(tim_angle-10)

def turn_left():
    tim_angle = tim.heading()
    tim.setheading(tim_angle+10)

def clear_screen():
    tim.reset()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
