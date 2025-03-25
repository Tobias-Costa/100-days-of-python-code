from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green","blue","purple"]
all_turtles = []    

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=(-70 +(index*30)))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winner_color =  turtle.pencolor()
            
            if user_bet.lower() == winner_color.lower():
                print(f"You've won! The winner is the {winner_color} turtle")
            else:
                print(f"You've lost. The winner is the {winner_color} turtle")

        rand_distance = randint(0,10)
        turtle.forward(rand_distance)
        
screen.exitonclick()