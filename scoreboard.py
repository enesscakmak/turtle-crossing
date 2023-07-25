import turtle
from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(f"Level: {level}", font=FONT)

    def game_over(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.write("Game Over", align="center", font=FONT)

