from turtle import Turtle, Screen
from colorgram import extract
from random import choice, randrange
from time import sleep

from colorgram.colorgram import Rgb

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")
timmy_the_turtle.color("green")
timmy_the_turtle.pensize(2)
timmy_the_turtle.setheading(0)
timmy_the_turtle.speed(0)
timmy_the_turtle.pensize(1)
timmy_the_turtle.pu()
timmy_the_turtle.goto((0,0))
timmy_the_turtle.pd()

screen = Screen()
screen.colormode(255)

def dashed_line(l,a):
    '''
    l ---> length of sides
    a ---> angle to turn
    
    
    '''
    timmy_the_turtle.forward(l)
    timmy_the_turtle.pu()
    timmy_the_turtle.forward(l)
    timmy_the_turtle.right(a)
    timmy_the_turtle.pd()

def different_shapes(l,s):
    '''
    l ---> length of sides
    s ---> number of sides
    
    
    '''
    sides = 3
    while sides < s + 1:
        for _ in range(0,sides):
            timmy_the_turtle.forward(l)
            timmy_the_turtle.right(360/sides)
        sides += 1
        color = [(randrange(0, 255), randrange(0, 255), randrange(0, 255)) for _ in range(2)]
        timmy_the_turtle.pencolor(choice(color))

def random_walk(l):
    '''
    l ---> length of side
    
    
    '''
    directions = [timmy_the_turtle.right, timmy_the_turtle.left]
    while True:
        timmy_the_turtle.forward(l)
        choice(directions)(choice([45,90,180]))
        color = [(randrange(0, 255), randrange(0, 255), randrange(0, 255)) for _ in range(2)]
        timmy_the_turtle.pencolor(choice(color))

def spirograph(c,r):
    '''
    c ---> number of circles
    r ---> radius of circle
    
    
    '''
    current_circle = 0
    while current_circle < c+1:
        timmy_the_turtle.circle(r)
        current_circle += 1
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + (360/c))
        color = [(randrange(0, 255), randrange(0, 255), randrange(0, 255)) for _ in range(2)]
        timmy_the_turtle.pencolor(choice(color))

def damien_hirst(l,w,c,radius = 20):
    '''
    l ---> length (Number of Dots)
    w ---> width (Number of Dots)
    c ---> colors (Number of Colors)
    r ---> radius (Radius of Circles) Default: 20
    '''
    timmy_the_turtle.pu()
    rgb_colors = []
    length = 0
    width = 0
    colors = extract('hirst.JPG', c)
    timmy_the_turtle.goto((-400,-400))
    starting_position_x = timmy_the_turtle.xcor()
    starting_position_y = timmy_the_turtle.ycor()

    for color in colors:
        r= color.rgb.r
        g= color.rgb.g
        b= color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    
    while length < l:

        while width < w:
            timmy_the_turtle.color(choice(rgb_colors))
            timmy_the_turtle.begin_fill()
            timmy_the_turtle.circle(radius)
            timmy_the_turtle.end_fill()
            width += 1
            timmy_the_turtle.pu()
            timmy_the_turtle.forward(radius*2)

        width = 0
        timmy_the_turtle.goto((starting_position_x,starting_position_y + 50))
        starting_position_y += 50
        length += 1
    





for _ in range(0,100):
    #dashed_line(20,45)
    # different_shapes(60,500)
    # random_walk(20)
    # spirograph(500,200)
    damien_hirst(20,20,50,25)


screen.exitonclick()
