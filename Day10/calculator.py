from art import *
from os import system as sys
import time

result = 0

def calculator(num1 = 0):
    tprint("Calculator")
    time.sleep(1)
    if num1 == 0:
        print("Welcome to Calculator!\n")
        first_number = input("Please Enter Your First Number: ")
        operation = input("Please Enter Operation: \n\n/\n*\n+\n-\n\n")
        second_number = input("Please Enter Your Second Number: ")
    else:
        first_number = str(num1)
        operation = input("Please Enter Operation: \n\n/\n*\n+\n-\n\n")
        second_number = input("Please Enter Your Second Number: ")

    global result
    result = eval(first_number+operation+second_number)
    print("\nThe result of your calculation is " + str(result))
    time.sleep(2)
    continue_operation = input("\nEnter -Y- to continue working with that nnumber or -N- to start a new calculation : ")
    if continue_operation == "Y" or continue_operation == "y":
        sys('cls')
        calculator(result)
    else:
        result = 0
        sys('cls')
        calculator()

calculator()
    