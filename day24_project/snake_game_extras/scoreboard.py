from turtle import Turtle
ALIGNMENT =  "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", encoding="utf-8") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0,260)
        self.write_scoreboard()
    
    def write_scoreboard(self):
        self.write(arg=f"Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
        with open("data.txt", mode="w", encoding="utf-8") as data:
            data.write(str(self.high_score))

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score += 1
        self.write_scoreboard()