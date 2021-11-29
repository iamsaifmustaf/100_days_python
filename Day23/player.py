from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(0,new_y)

    def reset_player(self):
        self.goto(STARTING_POSITION)    

