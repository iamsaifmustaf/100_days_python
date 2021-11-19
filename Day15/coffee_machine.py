from os import system as sys
import time
from art import *
import assets

water = 1000
milk = 500
coffee = 200
total_balance = 0

coffee_list = {
    "espresso":{
        "water":50,
        "milk":0,
        "coffee":18,
        "price":1.50
    },
    "latte":{
        "water":200,
        "milk":150,
        "coffee":24,
        "price":2.50
    },
    "cappuccino":{
        "water":250,
        "milk":100,
        "coffee":24,
        "price":3.00
    }
}

def handle_payment(drink):
    global coffee_list
    global total_balance
    quarters = int(input("Please Enter Number of Quarters?  "))
    dimes = int(input("Please Enter Number of Dimes?  "))
    nickles = int(input("Please Enter Number of Nickles?  "))
    pennies = int(input("Please Enter Number of Pennies?  "))
    money_required = coffee_list[drink]['price']
    money_inserted = float((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
    if (money_required - money_inserted) < 0:
        print(f"Here is ${abs(money_required - money_inserted)} in change.") 
        total_balance += money_required
        return
    else:
        return -1

def handle_inventory(drink):
    global water
    global milk
    global coffee
    water_required = coffee_list[drink]['water']
    milk_required = coffee_list[drink]['milk']
    coffee_required = coffee_list[drink]['coffee']
    if(water < water_required or milk < milk_required or coffee < coffee_required):
        print("\n\n\nResources low at this time\nPlease Try Again Later! \nSorry for the Inconvenience!\n\n\n")
        sys('cls')
        return -1
    else:
        water -= water_required
        milk -= milk_required
        coffee -= coffee_required
        return


def coffee_machine():
    tprint('WELCOME')
    time.sleep(1)
    tprint('TO')
    time.sleep(1)
    print(assets.coffee)
    tprint("Coffee Machine")
    time.sleep(2)

    choice = input("\n\n\nWhat would you like? (espresso/latte/cappuccino): ")

    if(choice == "report"):
        print(f"\n\nWater: {water}\nMilk: {milk}\nCoffee: {coffee}\nTotal Balance: ${float(total_balance)}\n\n")
        return
    elif(choice == "off"):
        exit()
    elif(choice == "espresso" or choice == "latte" or choice == "cappuccino"):
        enough_resources = handle_inventory(choice)
        enough_money = handle_payment(choice)
        if enough_resources == -1 or enough_money == -1:
            return
        print(f"Enjoy Your {choice}!\nCome Back Again!")
    elif(handle_payment(choice) == 1):
        print("\n\nSorry, your change was not enough to purchase this item. \n\n Your money has been refunded \n\nPlease Try Again!")
        return


coffee_machine()
while (input("Do you want to start again? Enter -n- for yes and -y- for no: ") == "y"):
    sys('cls')
    coffee_machine()
    time.sleep(3)