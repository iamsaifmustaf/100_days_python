def average_height():
    list_of_heights = (input("Welcome to Average Height Calculator! \n\nPlease Enter The Heights of All Members, Seperated By -SPACE- \n\n")).split(" ")
    total = 0
    for height in list_of_heights:
        total += int(height)
    print(f"\nAverage Height of Members is: {round(total/len(list_of_heights))}\n\n")

while True:
    average_height()