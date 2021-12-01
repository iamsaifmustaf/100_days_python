from turtle import Screen, Turtle, mainloop
import cv2
import time
import pandas as pd

#Create Screen and find background image dimensions using OpenCV
screen = Screen()
screen.title("U.S. States Quiz")
image = "./blank_states_img.gif"
cv_image = cv2.imread(image)
height,width,c = cv_image.shape
screen.setup(height=height,width=width)
screen.addshape(image)

us_image = Turtle()
us_image.shape(image)
writer = Turtle()
writer.pu()
writer.hideturtle()

#Importing Data
states_data_path = './50_states.csv'
data = pd.read_csv(states_data_path)
states = data['state']
states = states.str.lower()
states = states.tolist()
x_cor = data['x'].tolist()
y_cor = data['y'].tolist()

#Game Loop
game_is_on = True
completed_states = []
while game_is_on:

    user_answer = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    user_answer = user_answer.lower()

    if user_answer in states and user_answer not in completed_states:
        index = states.index(user_answer)
        writer.goto(x_cor[index], y_cor[index])
        writer.write(data['state'][index])
        completed_states.append(user_answer)
        time.sleep(1)
    else:
        print("Try Again!")

    if len(states) == len(completed_states):
        game_is_on = False

mainloop()