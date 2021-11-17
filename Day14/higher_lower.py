import random
import math
import time
from art import *
from os import system as sys
import assets
import game_data

def compare_followers(follower1,follower2):
    if follower1 > follower2:
        return 1
    else:
        return 0


def higher_lower():
    score = 0
    tprint("WELCOME")
    time.sleep(1)
    tprint("TO")
    time.sleep(1)
    print(assets.logo)
    time.sleep(2)
    choices = [random.choice(game_data.data),random.choice(game_data.data)]
    while True:
        sys('cls')
        print(f"Your Current Score is : {score}\n\n")
        print(f"\n\nCompare A: {choices[0]['name']}, {choices[0]['description']} from {choices[0]['country']}")
        time.sleep(2)
        print(assets.vs)
        print(f"\n\nAgainst B: {choices[1]['name']}, {choices[1]['description']} from {choices[1]['country']}")
        winner = compare_followers(choices[0]['follower_count'],choices[1]['follower_count'])
        time.sleep(2)
        player_pick = input("\n\nWho has more followers? 'a' or 'b'? ")

        if (player_pick == 'a' and winner == 1 or player_pick == 'b' and winner == 0):
            score += 1
            print(f"\n\nYou Guessed Right! Your Current Score is: {score}")
            time.sleep(1)
            choices[0] = choices[1]
            choices[1] = random.choice(game_data.data)
        else:
            print(f"\n\nYou Guessed Wrong!\n\nYour Score was: {score}\n\n")
            time.sleep(1)
            tprint("Game Over!")
            time.sleep(2)
            break

higher_lower()
while (input("Do you want to play again? Enter -n- for yes and -y- for no: ") == "y"):
    sys('cls')
    higher_lower()