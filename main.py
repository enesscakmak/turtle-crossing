import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

level = 0
game_is_on = True

player = Player()
screen = Screen()
cars = CarManager(level)
scoreboard = Scoreboard(level)

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeypress(player.move, "w")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.movement(level)
    if player.ycor() == 270:
        level += 1
        scoreboard.update_level(level)

    for car in cars.car_list:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
