from turtle import Screen, window_height
import time
import winsound
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Create Screen and set bg color, size and title

def snake_game():
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
            winsound.PlaySound('./sounds/eat_food.wav', winsound.SND_ASYNC)
            food.new_food_location()
            snake.extend()
            scoreboard.increase_score()

        #Detect Collison with Wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail
        for square in snake.snake_body[-1:]:
            if snake.head.distance(square) < 10:
                game_is_on = False
                scoreboard.game_over()

    winsound.PlaySound('./sounds/game_over.wav', winsound.SND_ASYNC)
    scoreboard.game_over()

    screen.exitonclick()

snake_game()
