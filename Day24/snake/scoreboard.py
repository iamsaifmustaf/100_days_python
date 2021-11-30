from turtle import Turtle
import random
import time

ALIGNTMENT = "center"
FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        file = open("my_file.txt","r")
        contents = file.read()
        self.high_score = int(contents)
        file.close()
        self.score = 0
        self.pu()
        self.color("white")
        self.goto(0,270)
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.clear()
        self.goto((0,270))
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=ALIGNTMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_file.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
    
    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def try_again(self):
        self.goto(0,0)
        self.write(f"TRY AGAIN!", align=ALIGNTMENT, font=FONT)
        self.reset()            
        time.sleep(2)
        self.clear()
        self.update_score_board()