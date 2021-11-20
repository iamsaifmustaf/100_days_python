from os import system as sys
import time
#from art import *
import assets


class CoffeeMaker:
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
        quarters = int(input("Please Enter Number of Quarters?  "))
        dimes = int(input("Please Enter Number of Dimes?  "))
        nickles = int(input("Please Enter Number of Nickles?  "))
        pennies = int(input("Please Enter Number of Pennies?  "))
        money_required = getattr(CoffeeMaker,'coffee_list')[drink]['price']
        money_inserted = float((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
        if (money_required - money_inserted) < 0:
            print(f"Here is ${abs(money_required - money_inserted)} in change.") 
            time.sleep(1)
            setattr(CoffeeMaker,'total_balance', setattr(CoffeeMaker,'total_balance') + money_required)
            return
        else:
            print("\n\nSorry, your change was not enough to purchase this item. \n\nYour money has been refunded \n\nPlease Try Again!\n\n\n")
            return -1

    def handle_inventory(drink):
        global water
        global milk
        global coffee
        water_required = getattr(CoffeeMaker,'coffee_list')[drink]['water']
        milk_required = getattr(CoffeeMaker,'coffee_list')[drink]['milk']
        coffee_required = getattr(CoffeeMaker,'coffee_list')[drink]['coffee']
        if(getattr(CoffeeMaker,'water') < water_required or getattr(CoffeeMaker,'milk') < milk_required or getattr(CoffeeMaker,'coffee') < coffee_required):
            print("\n\n\nResources low at this time\nPlease Try Again Later! \nSorry for the Inconvenience!\n\n\n")
            time.sleep(3)
            sys('cls')
            return -1
        else:
            setattr(CoffeeMaker,'water', getattr(CoffeeMaker,'water') + water_required)
            setattr(CoffeeMaker,'milk', getattr(CoffeeMaker,'milk') + milk_required)
            setattr(CoffeeMaker,'coffee', getattr(CoffeeMaker,'coffee') + coffee_required)
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
            print(f"\n\nWater: {getattr(CoffeeMaker,'water')}\nMilk: {getattr(CoffeeMaker,'milk')}\nCoffee: {getattr(CoffeeMaker,'coffee')}\nTotal Balance: ${float(getattr(CoffeeMaker,'total_balance'))}\n\n\n")
            return
        elif(choice == "off"):
            exit()
        elif(choice == "espresso" or choice == "latte" or choice == "cappuccino"):
            enough_money = CoffeeMaker.handle_payment(choice)
            if enough_money == -1:
                return
            enough_resources = CoffeeMaker.handle_inventory(choice)
            if enough_resources == -1:
                return

            print(f"\nEnjoy Your {choice}!\n\nCome Back Again!")
            time.sleep(2)

coffee_machine_1 = CoffeeMaker()


coffee_machine_1.coffee_machine()
while (input("Do you want to start again? Enter -n- for yes and -y- for no: ") == "y"):
    sys('cls')
    coffee_machine_1.coffee_machine()
    time.sleep(3)