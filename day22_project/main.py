from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE_POSITION = (350,0)
LEFT_PADDLE_POSITION = (-350,0)

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

#Create and move paddle
r_paddle = Paddle(RIGHT_PADDLE_POSITION)
l_paddle = Paddle(LEFT_PADDLE_POSITION)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

#Create the ball and make it move
ball = Ball()

#Create a scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #Detect when left paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()