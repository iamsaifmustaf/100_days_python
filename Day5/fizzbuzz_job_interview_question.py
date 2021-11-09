list = []
for number in range(1,101):
    if(number % 3 == 0 or number % 5 == 0):
        if(number % 3 == 0 and number % 5 == 0):
            list.append("FizzBuzz")
        elif(number % 3 == 0):
            list.append("Fizz")
        else:
            list.append("Buzz")
    else:
        list.append(number)
print(list)