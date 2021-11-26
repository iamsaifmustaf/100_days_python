from turtle import Screen, Turtle
import time

# Create Screen and set bg color, size and title

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


def snake_game():
    #initialize snake body and starting position
    snake_body = []
    starting_postions = [(0, 0), (-20, 0), (-40, 0)]

    #create starting squares 
    for position in starting_postions:
        square = Turtle()
        square.pu()
        square.shape("square")
        square.color("white")
        square.goto(position)
        snake_body.append(square)

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        #moving snake
        for square_num in range(len(snake_body) - 1, 0 , -1):
            snake_body[square_num].goto(snake_body[square_num - 1].pos())
        snake_body[0].forward(20)


snake_game()


screen.exitonclick()
