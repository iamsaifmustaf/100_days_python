size = input("Welcome to Python Pizza Deliveries! \nPlease choose the size pizza you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")
total = 0

if(size == "S"):
    total += 15
elif(size == "M"):
    total += 20
elif(size == "L"):
    total += 25
else:
    print("Wrong Choice, Please Try Again!")

if(add_pepperoni == "Y"):
    total += 2
if(extra_cheese == "Y"):
    total += 1

print(f"Your final bill is : ${total}")


