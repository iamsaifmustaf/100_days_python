total_bill = input("Welcome to the tip calculator. \nWhat was the total bill? $ ")
number_of_guests = input("How many people to split the bill? # ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? % ")
print("Each person should pay: $" + str(round((float(total_bill)/float(number_of_guests))*(1+(float(tip_percentage)/100)),2)))