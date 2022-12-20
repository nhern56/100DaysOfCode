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

import random

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

map = [rock, paper, scissors]

print(map[input])

computer = random.randint(0,2)

print(map[computer])

if input == 0:
  if computer == 1:
    print("computer wins")
  if computer == 2: 
    print("you win")
  elif input == computer:
    print("its a draw")
elif input == 1:
  if computer == 0:
    print("you win")
  if computer == 2: 
    print("computer wins")
  elif input == computer:
    print("its a draw")
elif input == 2: 
  if computer == 0:
    print("you win")
  if computer == 1: 
    print("computer wins")
  elif input == computer:
   print("its a draw")
  
