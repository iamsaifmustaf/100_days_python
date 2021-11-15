import random
import time
import math
from art import *
from os import system as sys
import blackjack_assets


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_cards = {"dealer_cards": [], "player_cards": []}
total_balance = 0

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
        return 2 : Draw Game
        return 3 : Continue Game'''
   
    if(score2 > 21 or score1 < 21 and abs(score1-21) < abs(score2-21)):
        return 0
    elif (score1 > 21 or score2 < 21 and abs(score2-21) < abs(score1-21)):
        return 1
    elif (score2 == score1):
        return 2
    else:
        return 3

def game_update():
    print(f"\nYour cards are {game_cards['player_cards']}    ====> Total: {str(sum(game_cards['player_cards']))}\n\nThe Dealer cards are [{game_cards['dealer_cards'][0]}] ====> Total: {game_cards['dealer_cards'][0]}\n\n")
    return


def blackjack():
    global total_balance
    sys("cls")
    time.sleep(0.5)
    print(blackjack_assets.black_jack_logo)
    time.sleep(0.5)
    print("             Welcome to BlackJack\n")
    time.sleep(0.5)
    print("             Get Your Money Ready!\n\n\n\n\n")
    time.sleep(1)
    bet_size = int(input("Place Your Bet: $"))
    
    for _ in range(2):
        deal_card('player_cards')
        deal_card('dealer_cards')


    if(calculate_score(game_cards["dealer_cards"]) == 0):
        print(f"\n\nYour cards are {game_cards['player_cards']}    ====> Total: {str(sum(game_cards['player_cards']))}\n\n\nsThe Dealer cards are [{game_cards['dealer_cards']}] ====> Total: {sum(game_cards['dealer_cards'])}\n\n")
        tprint("\n\nDealer Wins\n\n")
        total_balance -= bet_size
        time.sleep(1)
        print(f"Total Balance =====> {total_balance}\n\n")
        time.sleep(3)
        return
    elif (calculate_score(game_cards["player_cards"]) == 0):
        print(f"\n\nYour cards are {game_cards['player_cards']}    ====> Total: {str(sum(game_cards['player_cards']))}\n\nThe Dealer cards are [{game_cards['dealer_cards']}] ====> Total: {sum(game_cards['dealer_cards'])}\n\n")
        tprint("\n\nPlayer Wins\n\n")
        total_balance += bet_size * 2
        time.sleep(1)
        print(f"Total Balance =====> {total_balance}\n\n")
        time.sleep(3)
        return
    else:
        game_update()

    deal_another_card = input("-h- for HIT , -s- for stay: ")

    while deal_another_card == "h":
        deal_card("player_cards")
        if sum(game_cards['player_cards']) > 21:
            break 
        game_update()
        deal_another_card =  input("-h- for HIT , -s- for stay: ")
    

    while (sum(game_cards["dealer_cards"]) < 17):
        deal_card("dealer_cards")

    if(compare_scores(sum(game_cards["dealer_cards"]),sum(game_cards["player_cards"])) == 0):
        print(f"\nYour cards are {game_cards['player_cards']}    ====> Total: {str(sum(game_cards['player_cards']))}\n\nThe Dealer cards are [{game_cards['dealer_cards']}] ====> Total: {sum(game_cards['dealer_cards'])}\n\n")
        time.sleep(1)
        tprint("\n\nDealer Wins\n\n")
        total_balance -= bet_size
        time.sleep(1)
        print(f"Total Balance =====> {total_balance}\n\n")
        time.sleep(3)
    elif (compare_scores(sum(game_cards["dealer_cards"]),sum(game_cards["player_cards"])) == 1):
        print(f"\nYour cards are {game_cards['player_cards']}    ====> Total: {str(sum(game_cards['player_cards']))}\n\nThe Dealer cards are [{game_cards['dealer_cards']}] ====> Total: {sum(game_cards['dealer_cards'])}\n\n")
        time.sleep(1)
        tprint("\n\nPlayer Wins\n\n")
        total_balance += bet_size * 2
        time.sleep(1)
        print(f"Total Balance =====> {total_balance}\n\n")
        time.sleep(3)
    else:
        print(f"\nYour cards are {game_cards['player_cards']}    ====> Total: {str(sum(game_cards['player_cards']))}\n\nThe Dealer cards are [{game_cards['dealer_cards']}] ====> Total: {sum(game_cards['dealer_cards'])}\n\n")
        time.sleep(1)
        tprint("\n\nDRAW\n\n")
        time.sleep(3)

blackjack()
while (input("Do you want to play again? Enter -n- for yes and -y- for no: ") == "y"):
    game_cards = {"dealer_cards": [], "player_cards": []}
    blackjack()

