from art import *
from os import system as sys
import time

bids = {}

def save_bids():
    bidder_name = input("Please Enter Your Name: ")
    bidder_amount = input("Please Enter Your Bid: $")
    bids[str(bidder_name)] = int(bidder_amount)
    more_bidders = input("Enter -Y- for more bidders and -N- if you are the final bidder: ")
    if more_bidders == "y" or more_bidders == "Y":
        sys('cls')
        save_bids()
    else:
        max_value = max(list(bids.values()))
        max_bidder = list(bids.keys())[(list(bids.values())).index(max_value)]
        print(f"Max Bid was Placed by {max_bidder} for the amount of {max_value}")
        time.sleep(3)
        sys('cls')


def silent_auction():
    tprint("The Silent Auction")
    time.sleep(1.5)
    print("Welcome to the Silent Auction")
    time.sleep(1.5)
    save_bids()
    

while True:
    silent_auction()