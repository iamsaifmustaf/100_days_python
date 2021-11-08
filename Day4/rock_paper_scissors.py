import random
from art import *

def rock_paper_scissors():
    list_of_options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.randint(0 , len(list_of_options) - 1)

    choice = int(input("Welcome to Rock Paper Scissors, Where you are playing a game against the computer! \nWhat do you choose? Type 0 For Rock, 1 For Paper or 2 For Scissors. \n"))

    if(choice == 0):
        if(computer_choice == 2):
            print(f"\nYou chose \n\n   {list_of_options[choice]} \n\nComputer chose \n\n   {list_of_options[computer_choice]} \n\nYou Win!\n\n")
        else:
            print(f"\nYou chose \n\n   {list_of_options[choice]} \n\nComputer chose \n\n   {list_of_options[computer_choice]} \n\nYou Lose!\n\n")

    if(choice == 1):
        if(computer_choice == 0):
            print(f"\nYou chose \n\n   {list_of_options[choice]} \n\nComputer chose \n\n   {list_of_options[computer_choice]} \n\nYou Win!\n\n")
        else:
            print(f"\nYou chose \n\n   {list_of_options[choice]} \n\nComputer chose \n\n   {list_of_options[computer_choice]} \n\nYou Lose!\n\n")
            
    if(choice == 2):
        if(computer_choice == 1):
            print(f"\nYou chose \n\n   {list_of_options[choice]} \n\nComputer chose \n\n   {list_of_options[computer_choice]} \n\nYou Win!\n\n")
        else:
            print(f"\nYou chose \n\n   {list_of_options[choice]} \n\nComputer chose \n\n   {list_of_options[computer_choice]} \n\nYou Lose!\n\n")

while True:
    rock_paper_scissors()