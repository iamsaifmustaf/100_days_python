import random
import time
from os import system as sys
from art import *
import math


def number_guessing():
    number = random.randint(1,100)
    attempts = 0
    sys('cls')
    tprint("         Welcome to")
    time.sleep(1)
    tprint("Number Guessing")
    time.sleep(1)
    tprint("                           Game")
    time.sleep(2)
    difficulty = input("\n\nPlease Choose Your Difficulty. Enter -easy- or -hard- :  ")
    
    if difficulty == 'hard':
        attempts += 5
    else:
        attempts += 10

    current_guess = int(input("\nMake a guess :  "))

    while attempts != 0:
        if current_guess == number:
            tprint("\nYou got it! \n")
            time.sleep(1)
            tprint("\nGreat Job! \n")
            time.sleep(1.5)
            return
        elif current_guess > number:
            print(f"\nToo High!\n\nTry Again!\n\nAttempts left: {attempts}")
            attempts -= 1
            time.sleep(1.5)
            current_guess = int(input("\nMake a guess :  "))
        elif current_guess < number:
            print("\nToo Low!\nTry Again!")
            attempts -= 1
            time.sleep(1.5)
            current_guess = int(input("\nMake a guess :  "))
        else:
            print("\n\nTry again later!\n\n")
            time.sleep(1.5)
            return

    print(f"\nGame Over, the number was {number}\n")
    time.sleep(1.5)

number_guessing()
while (input("Do you want to play again? Enter -n- for yes and -y- for no: ") == "y"):
    number_guessing()
    
