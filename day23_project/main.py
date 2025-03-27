#Setup
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

#Create objects
turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Listen for the key "Up" press
screen.listen()
screen.onkeypress(turtle.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Create cars and move
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collisin with cars and write game over
    for car in car_manager.car_list:
        if car.distance(turtle) < 25:
            scoreboard.game_over()
            game_is_on = False

    #Detect if turtle reached the final line, increase car speed and update scoreboard level
    if turtle.is_reached_final_line():
        turtle.update_turtle()
        car_manager.increase_move_speed()
        scoreboard.level += 1
        scoreboard.update_scoreboard()

screen.exitonclick()