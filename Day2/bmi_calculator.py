height = input("Welcome to the BMI Calulator \nPlease Enter Your Height in Meters: ")
weight = input("Please Enter Your Weight in Kilograms: ")

print("Your Current BMI is: " + str(round(float(float(weight) / float(height) ** 2))))