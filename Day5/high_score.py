scores = input("\n\nWelcome to Highest Score Finder!\n\nPlease Enter All Your Game Scores Seperated By -SPACE- \n\n").split(" ")
high_score = 0

for score in scores:
    if(int(score) > high_score):
        high_score = int(score)

print(f"\n\nYour High Score is: {high_score}\n\n")