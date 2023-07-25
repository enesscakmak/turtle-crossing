import turtle
from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
is_game_on = True


class CarManager:
    def __init__(self, level):
        self.car_list = []
        self.create_cars()
        self.movement(level)

    def create_cars(self):
        turtle.tracer(0)
        for _ in range(20):
            car = Turtle("square")
            car.color(choice(COLORS))
            car.shapesize(1, 3, 1)
            car.penup()
            car.goto(randint(-280, 280), randint(-220, 240))
            car.setheading(180)
            self.car_list.append(car)

    def movement(self, level):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)
            if car.xcor() <= -310:
                car.hideturtle()
                car.goto(320, randint(-220, 240))
                car.color(choice(COLORS))
                car.showturtle()
