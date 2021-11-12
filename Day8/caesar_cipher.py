from typing import final
from art import *
import time
from os import system

def caesar_cipher():
    final_message = []
    tprint("\nWelcome to Caesar's Cipher",font="cybermedum")
    print("\nThe Powerful Encoder and Decoder!\n\n\n")

    initial_message = input("Enter 'e' to encrypt message, enter 'd' to decrypt message: \n")

    if (initial_message == "e"):
        input_message = input("\nPlease Enter The Message You want to Encrypt\n")
        steps = int(input("\nPlease Enter The number of Shifts for Encryption\n"))

        for c in list(input_message):
            final_message.append(chr(ord(c) + steps))

        print(f"Your encrypted message is as follows:")
        print(''.join(final_message))


    elif (initial_message == "d"):
        input_message = input("\nPlease Enter The Message You want to Decrypt\n")
        steps = int(input("\nPlease Enter The number of Shifts for Decryption\n"))

        for c in list(input_message):
            final_message.append(chr(ord(c) - steps))
        
        print(f"\nYour decrypted message is as follows:")
        print(''.join(final_message))

    else:
        print("Please Enter a valid string")
        time.sleep(3)
        caesar_cipher()


while True:
    time.sleep(5)
    system('cls')
    caesar_cipher()