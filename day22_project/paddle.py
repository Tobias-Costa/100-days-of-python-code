from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
    
    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
