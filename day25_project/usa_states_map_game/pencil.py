from turtle import Turtle

FONT = ("Arial", 8, "normal")

class Pencil(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state, x, y):
        self.goto(x,y)
        self.write(arg=state, align="center", font=FONT )