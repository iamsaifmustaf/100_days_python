import random
def banker_roulette():
    names_string = input("Welcome to Banker Roulette!\nPlease Enter The Names of all Participants, seperated by a comma. ")
    names = names_string.split(", ")
    print(f"\n{names[random.randint(0, len(names) - 1)]} is going to buy the meal today! \n\n")

while True:
    banker_roulette()