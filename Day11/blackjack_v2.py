import random
import time
import math
from os import system as sys
import blackjack_assets


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_cards = {"dealer_cards": [], "player_cards": []}

def deal_card(str):
    game_cards[str].append(random.choice(cards))
    return 

def calculate_score(cards):
    if (11 in cards and sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    
    if(sum(cards) == 21):
        return 0

    return sum(cards)

def compare_scores(score1,score2):
    '''Takes 2 Scores To Compare.
        Dealer Score Passed First.
        Player Score Passed Second
        
        return 0 : Dealer Wins
        return 1 : Player Wins
        return 2 : Draw Game'''
   
    if(score1 > 21 or score1 < 21 and (abs(score1)-21) < (abs(score2)-21)):
        return 0

    elif (score2 > 21 or score2 < 21 and (abs(score2)-21) < (abs(score1)-21)):
        return 1
    else:
        return 2

def game_update():
    print(f"\nYour cards are {game_cards['player_cards']}    ====> Total: {str(calculate_score(game_cards['player_cards']))}\n\nThe Dealer cards are [{game_cards['dealer_cards'][0]}] ====> Total: {game_cards['dealer_cards'][0]}\n\n")
    if calculate_score(game_cards['player_cards']) > 21:
        return 0
    return 1


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
    for _ in range(2):
        deal_card('player_cards')
        deal_card('dealer_cards')


    if(calculate_score(game_cards["dealer_cards"]) == 0):
        print("\n\nDealer Wins\n\n")
        time.sleep(3)
        blackjack()
    elif (calculate_score(game_cards["player_cards"]) == 0):
        print("\n\nPlayer Wins\n\n")
        time.sleep(3)
        blackjack()        
    else:
        print(f"\nYour cards are {game_cards['player_cards']}    ====> Total: {str(calculate_score(game_cards['player_cards']))}\n\nThe Dealer cards are [{game_cards['dealer_cards'][0]}] ====> Total: {game_cards['dealer_cards'][0]}\n\n")

    if input("-h- for HIT , -s- for stay: ") == "h":
        deal_card("player_cards")
        game_update()

    else:
        while (calculate_score(game_cards["dealer_cards"]) < 17):
            deal_card("dealer_cards")

    if(compare_scores(calculate_score(game_cards["dealer_cards"])),calculate_score(game_cards["player_cards"])) == 0:
        print("\n\nDealer Wins\n\n")
        time.sleep(3)
        blackjack()
    elif (compare_scores(calculate_score(game_cards["dealer_cards"])),calculate_score(game_cards["player_cards"]) ) == 1:
        print("\n\nPlayer Wins\n\n")
        time.sleep(3)
    else:
        print("\n\nDRAW\n\n")
        time.sleep(3)
        blackjack()

blackjack()
while (input("Do you want to play again? Enter -n- for yes and -y- for no: ") == "y"):
    blackjack()

