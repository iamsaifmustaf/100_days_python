year = int(input("Welcome to the Leap Year Checker. \nPlease Enter a year to check: "))

if year % 4 == 0: 
    if year % 100 == 0:
        if year % 400 == 0:
            print("!Leap Year!")
        else: 
            print("Not Leap")
    else: 
        print("!Leap Year!")
else: 
    print("Not Leap")