def treasure_map():
    row1 = ["⚜️","⚜️","⚜️"]
    row2 = ["⚜️","⚜️","⚜️"]
    row3 = ["⚜️","⚜️","⚜️"]
    map = [row1,row2,row3]

    choice = input("Please Enter The Row And Column Numbers Where You Think The Treasure Is Located! \n")
    v_position = int(choice[0])
    h_position = int(choice[1])

    selected_row = map[v_position - 1]
    selected_row[h_position - 1] = "X"

    print(f"{row1}\n{row2}\n{row3}\n\n")

while True:
    treasure_map()