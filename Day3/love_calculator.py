print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_name = (name1+name2).lower()

true_count = 0
love_count = 0

true_count += (combined_name).count('r')
true_count += (combined_name).count('u')
true_count += (combined_name).count('e')
true_count += (combined_name).count('t')
love_count += (combined_name).count('l')
love_count += (combined_name).count('o')
love_count += (combined_name).count('v')
love_count += (combined_name).count('e')

combined_score = int(f"{true_count}{love_count}")

print(f"Your Love score  is {combined_score}.")

if(combined_score > 90 or combined_score < 10):
    print("You go together like diet coke and mentos ;)")
elif(combined_score > 40 and combined_score < 50):
    print("You are alright together")
else:
    print(" ")


