from turtle import Turtle, Screen
from random import randint
from time import sleep
from os import system

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def turtle_race():
    user_bet = screen.textinput(title="Who Will Win This Race?",prompt="Which color turtle you think will win the race? ")
    system('cls')
    green = Turtle()
    red = Turtle()
    black = Turtle()
    purple = Turtle()
    orange = Turtle()
    blue = Turtle()
    turtle_list = [green,red,black,purple,orange,blue]
    color_list = ['green','red','black','purple','orange','blue']
    starting_position_x = -400
    starting_position_y = -300
    current_color = 0
    sleep(2)
    tim.pu()
    tim.goto((300,500))
    tim.pd()
    tim.goto((300,-500))
    tim.write("Referee", True, align="center")
    sleep(2)


    while starting_position_y < 400 and current_color < len(color_list):
        for turtle in turtle_list:
            turtle.shape('turtle')
            turtle.color(color_list[current_color])
            current_color += 1
            turtle.pu()
            turtle.setpos((starting_position_x,starting_position_y))
            starting_position_y += 100
            # turtle.write(turtle.color()[0], True, align="left")

    
    sleep(3)

    while True:
        for turtle in turtle_list:
            turtle.goto(((turtle.xcor()+(randint(1,10))),turtle.ycor()))
            if turtle.xcor() > 300:
                print(f"{str(turtle.color()[0]).upper()} turtle won the race!")
                sleep(1)
                if str(turtle.color()[0]).lower() == user_bet.lower():
                    print('\nYou made the right guess!')
                else:
                    print('\nYou made  the wrong guess!')
                return()
    
        

turtle_race()

# screen.listen()
# screen.onkeypress(key='W', fun=move_forwards)
# screen.onkeypress(key='S', fun=move_backwards)
# screen.onkeypress(key='A', fun=turn_left)
# screen.onkeypress(key='D', fun=turn_right)


screen.exitonclick()