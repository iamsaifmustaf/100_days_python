from turtle import Screen, Turtle

#Create Screen and set bg color, size and title
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
snake_body = []
x_position = 0


for _ in range (0,3):

    square = Turtle()
    square.color('white')
    square.shape('square')
    square.pensize(10)
    square.setx(x_position)
    x_position -= 20
    snake_body.append(square)

[print(square.color) for square in snake_body]


















screen.exitonclick()