

with open("./Input/Names/invited_names.txt", mode="r") as letter_names:
    names = (letter_names.read()).split('\n')

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_content:
    letter = letter_content.read()

for name in names:
    file = open("./Output/"+name.lower()+"_letter.txt", "w")
    new_letter = letter.replace("[name]" , name)
    file.write(new_letter)
