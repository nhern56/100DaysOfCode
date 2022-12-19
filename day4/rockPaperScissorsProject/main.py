import random



input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

map = [rock, paper, scissors]

choice = map[input-1]

computer = random.choice(map)


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


print(choice)

print(computer)

