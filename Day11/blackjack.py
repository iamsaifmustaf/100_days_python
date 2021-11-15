import time
from os import system as sys
#from art import *
import random
import math
import blackjack_assets


game_cards = {"dealer_cards": [], "player_cards": []}


def add_card(str):
    game_cards[str].append(random.randint(2, 11))


def game_status():
    print(game_cards)
    print(game_cards['dealer_cards'][-1])
    print(
        f"Your cards are {game_cards['player_cards']} with a total of {sum(game_cards['player_cards'])}\nDealer cards are {list(game_cards['dealer_cards'][0])} with a total of {sum(game_cards['dealer_cards'] - game_cards['dealer_cards'][-1])}"
    )
    time.sleep(3)
    check_game()


def check_game():
    if sum(game_cards["player_cards"]) == 21 and sum(game_cards["dealer_cards"]) != 21:
        #tprint("\n\nPlayer Wins\n\n")
        time.sleep(3)
        blackjack()

    elif sum(game_cards["dealer_cards"]) == 21 and sum(game_cards["player_cards"]) != 21:
        #tprint("\n\nDealer Wins\n\n")
        time.sleep(3)
        blackjack()

    elif (sum(game_cards["player_cards"]) > 21) or (abs(sum(game_cards["player_cards"]) - 21) > abs(sum(game_cards["dealer_cards"]))):
        #tprint("\n\nDealer Wins\n\n")
        time.sleep(3)
        blackjack()

    elif (sum(game_cards["dealer_cards"]) > 21) or (
        abs(sum(game_cards["player_cards"]) - 21) < abs(sum(game_cards["dealer_cards"]))
    ):
        #tprint("\n\nPlayer Wins\n\n")
        time.sleep(3)
        blackjack()
    elif abs(sum(game_cards["player_cards"]) - 21) == (
        abs(sum(game_cards["dealer_cards"])) - 21
    ):
        #tprint("\n\nDRAW\n\n")
        time.sleep(3)
        blackjack()
    else:
        return


def blackjack():
    sys("cls")
    time.sleep(0.5)
    print(blackjack_assets.black_jack_logo)
    time.sleep(0.5)
    print("Welcome to BlackJack\n")
    time.sleep(0.5)
    print("Get Your Money Ready!\n")
    time.sleep(1)
    bet_size = int(input("Place YOur Bet: $"))
    add_card("dealer_cards")
    add_card("dealer_cards")
    add_card("player_cards")
    add_card("player_cards")
    check_game()

    if input("-H- for HIT , -S- for stay: ") == "H" or "h":
        add_card("player_cards")
        game_status()
        check_game()


blackjack()
