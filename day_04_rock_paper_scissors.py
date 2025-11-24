# Day 04 - 23 Nov 2025
# PROJECT: Rock Paper Scissors 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Your brilliant idea – list of art
game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!\n")

you_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

you = int(you_choose)

if you >2 or you < 0:
    print("You can't make a move!")
elif you == 0:
    print(game_images[you])
elif you == 1:
    print(game_images[you])
else:
    print(game_images[you])

# print("Computer chose")
computer_choose = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choose])
#
if you == computer_choose:
    print("It's a draw!")
elif (you == 0 and computer_choose == 2) or (you == 1 and computer_choose == 0) or (you == 2 and computer_choose == 1):
    print("You win!")
else:
    print("You lose!")
