from turtle import Turtle, shapesize
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.move_speed = 0.1

    def start_car_sequence(self):
        random_chance = randint(1,5)
        if random_chance == 1:
            car = Turtle()
            car.pu()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(choice(COLORS))
            car.setheading(180)
            rand_y = randint(-250,250)
            car.goto(300,rand_y)
            self.cars.append(car)
                
            

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
            

