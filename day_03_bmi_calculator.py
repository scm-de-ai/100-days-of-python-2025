# Day 03 - 21 Nov 2025
# Name: first program that makes decisions
# Project: BMI Calculator with WHO categories + type hints
# Feeling: My code can now THINK

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"\nYour BMI is: {round(bmi, 2)}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
elif bmi < 35:
    print("Category: Obese")
else:
    print("Category: Clinically obese")
