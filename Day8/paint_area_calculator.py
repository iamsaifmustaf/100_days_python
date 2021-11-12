import math
from art import *
from os import system
import time


def paint_area_calculator():
    tprint("\n\nWelcome to Paint Area Calculator!\n\n")

    current_height = int(input("\nPlease enter the height of the area being painted: "))
    current_width = int(input("\nPlease enter the width of the area being painted: "))
    current_coverage = 5
    print(f"\nYou need to buy --{math.ceil(paint_can_calc(height = current_height, width = current_width, coverage = current_coverage))}-- cans of paint\n")
    time.sleep(3)
    

def paint_can_calc(height, width, coverage):
    return (height * width) / coverage

while True:
    system('cls')
    paint_area_calculator()