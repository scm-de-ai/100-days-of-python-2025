# Day 02 - 20 Nov 2025
# Name: scm_de_ai - fixing bugs like a pro
# Project: Python Pizza Deliveries – 100% correct logic, no duplicate prints
# Feeling: I debugged like a senior dev today

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Base price
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size! Taking $20 as default.")
    bill = 20

# Pepperoni
if pepperoni == "Y":
    bill += 2 if size == "S" else 3

# Extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
