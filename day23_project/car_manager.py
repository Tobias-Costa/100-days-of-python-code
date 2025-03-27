from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.car_list = []
        self.move_speed = STARTING_MOVE_DISTANCE
    
    def create_cars(self):
        if randint(1,6) == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, randint(-250,250))
            self.car_list.append(new_car)
            
    def move_cars(self):
        for car in self.car_list:
            car.backward(self.move_speed)

    def increase_move_speed(self):
        self.move_speed += MOVE_INCREMENT