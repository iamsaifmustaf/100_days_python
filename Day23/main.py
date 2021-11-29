import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.start_car_sequence()
    car_manager.move_cars()

    #Increase Level
    if player.ycor() > 290:
        player.reset_player()
        scoreboard.increase_level()
        car_manager.move_speed *= 0.95

    #Detect Collision With Car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            scoreboard.current_level = 0
            player.reset_player()
            car_manager.move_speed = 0.1


    




screen.exitonclick()
