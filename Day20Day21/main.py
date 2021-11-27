from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Create Screen and set bg color, size and title

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with Food
    if snake.head.distance(food) < 15:
        food.new_food_location()
        scoreboard.increase_score()

screen.exitonclick()
