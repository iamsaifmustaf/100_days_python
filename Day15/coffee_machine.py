from os import system as sys
import time
#from art import *
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
        time.sleep(1)
        total_balance += money_required
        return
    else:
        print("\n\nSorry, your change was not enough to purchase this item. \n\nYour money has been refunded \n\nPlease Try Again!\n\n\n")
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
        time.sleep(3)
        sys('cls')
        return -1
    else:
        water -= water_required
        milk -= milk_required
        coffee -= coffee_required
        return


def coffee_machine():
    global water
    global milk
    global coffee
    global total_balance
    print('WELCOME')
    time.sleep(1)
    print('TO')
    time.sleep(1)
    print(assets.coffee)
    print("Coffee Machine")
    time.sleep(2)

    choice = input("\n\n\nWhat would you like? (espresso/latte/cappuccino): ")

    if(choice == "report"):
        print(f"\n\nWater: {water}\nMilk: {milk}\nCoffee: {coffee}\nTotal Balance: ${float(total_balance)}\n\n\n")
        return
    elif(choice == "off"):
        exit()
    elif(choice == "espresso" or choice == "latte" or choice == "cappuccino"):
        enough_money = handle_payment(choice)
        if enough_money == -1:
            return
        enough_resources = handle_inventory(choice)
        if enough_resources == -1:
            return

        print(f"\nEnjoy Your {choice}!\n\nCome Back Again!")
        time.sleep(2)


coffee_machine()
while (input("Do you want to start again? Enter -n- for yes and -y- for no: ") == "y"):
    sys('cls')
    coffee_machine()
    time.sleep(3)