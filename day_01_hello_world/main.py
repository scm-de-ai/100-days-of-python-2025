# Day 01 - 19 Nov 2025
# Name: scm-de-ai (29 → ₹1 Cr+ mission starts HERE)
# Completed: FULL Day 1 of Angela Yu's 100 Days of Python
# Projects inside:
#   1. Variable swapping (wrote line-by-line myself)
#   2. Band Name Generator (my first interactive program EVER)
# Feeling: Proud AF. First real code of my life.

# ───────────────────────────────
# 1. Variable Swapping Project
# ───────────────────────────────
glass1 = "milk"
glass2 = "juice"
print("Before swapping - Glass1:", glass1, "| Glass2:", glass2)

# Swap without a temporary variable
glass1, glass2 = glass2, glass1

print("After swapping - Glass1:", glass1, "| Glass2:", glass2)
print("\n" + "-"*50 + "\n")


# ───────────────────────────────
# 2. Band Name Generator Project
# ───────────────────────────────
band_name = "Welcome to the Band Name Generator"
print(band_name)
city = input("What's the name of the City you grew up in?\n")
petname = input("What's the pet name?\n")
print("You band name could be: " + city + " " + petname)
