height = input("Welcome to the BMI Calulator 2.0 \nPlease Enter Your Height in Meters: ")
weight = input("Please Enter Your Weight in Kilograms: ")
bmi = round(float(float(weight) / float(height) ** 2))


print(f"Your Current BMI is: {bmi} \nYour Current Classification is : ")

if bmi < 18.5: print("Underweight")
elif bmi > 18.5 and bmi < 25: print("Normal Weight")
elif bmi > 25 and bmi < 30: print("Overweight")
elif bmi > 30 and bmi < 35: print("Obese")
else: print("Clinically Obese")

