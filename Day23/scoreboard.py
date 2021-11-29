from turtle import Turtle, Screen
import sys
import time
import random

ALIGNTMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.current_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0,270)
        self.write(f"LEVEL: {self.current_level}", align=ALIGNTMENT, font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNTMENT, font=FONT)
        time.sleep(2)
        self.clear()
        self.current_level = 1
        self.update_scoreboard()