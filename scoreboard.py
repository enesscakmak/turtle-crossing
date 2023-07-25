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
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over", font=FONT)

