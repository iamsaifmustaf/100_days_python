from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20



class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()


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

        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_right(self):
        self.snake_body[0].setheading(0)
        self.move()
    def move_up(self):
        self.snake_body[0].setheading(90)
        self.move()
    def move_left(self):
        self.snake_body[0].setheading(180)
        self.move()
    def move_down(self):
        self.snake_body[0].setheading(270)
        self.move()