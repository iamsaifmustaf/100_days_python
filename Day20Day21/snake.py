from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            square = Turtle()
            square.pu()
            square.shape("square")
            square.color("white")
            square.goto(position)
            self.snake_body.append(square)

    def move(self):
        for square_num in range(len(self.snake_body) - 1, 0 , -1):
            self.snake_body[square_num].goto(self.snake_body[square_num - 1].pos())

        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() == LEFT:
            return()
        self.head.setheading(RIGHT)
    
    def move_up(self):
        if self.head.heading() == DOWN:
            return()
        self.head.setheading(UP)
                
    def move_left(self):
        if self.head.heading() == RIGHT:
            return()
        self.head.setheading(LEFT)
    
    def move_down(self):
        if self.head.heading() == UP:
            return()
        self.head.setheading(DOWN)
