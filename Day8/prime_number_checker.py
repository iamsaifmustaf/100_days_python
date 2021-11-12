from art import *
import time
from os import system


def prime_number_checker():

    tprint("\nWelcome to Prime Number Checker!\n",font="cybermedum")

    number = int(input("Please Enter the Number to Check: "))

    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    if len(factors) > 2:
        print("\nThis is not a prime number")
        time.sleep(3)
        system("cls")

    else:
        print("\nThis is a prime number")
        time.sleep(3)
        system("cls")

            
while True:
    prime_number_checker()
