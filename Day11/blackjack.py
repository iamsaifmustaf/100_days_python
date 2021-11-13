import time
from os import system as sys
from art import *
import random
import blackjack_assets


game_cards = {
    "Dealer":[],
    "Player":[]
}

def blackjack():
    time.sleep(0.5)
    print(blackjack_assets.black_jack_logo)
    time.sleep(0.5)
    print("Welcome to BlackJack\n")
    time.sleep(0.5)
    print("Get Your Money Ready!\n")
    time.sleep(1)
    bet_size = int(input("Place YOur Bet: $"))
    game_cards["Dealer"].append(random.randint(1,10))
    game_cards["Player"].append(random.randint(1,10)) 
    game_cards["Player"].append(random.randint(1,10))
    
    if (input("-H- for HIT , -S- for stay: ") == "H"):
        game_cards["Player"].append(random.randint(1,10))
    
    
    
    print(game_cards)





blackjack()