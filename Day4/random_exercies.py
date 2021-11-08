import random
def coin_toss():
    print("\nWelcome to Coin Toss!! \n")
    first_name = input("Please Enter Your First Name: ")
    last_name = input("Please Enter Your Last Name: ")

    random_integer = int(f"{len(first_name)}{len(last_name)}") * random.randint(1,5000)

    if(random_integer % 2 == 0):
        print("Heads!")
    else:
        print("Tails!")

while True:
    coin_toss()