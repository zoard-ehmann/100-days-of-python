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

#Write your code below this line 👇

terminated = False

possibilities = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if user_choice < 0 or user_choice > 2:
  result = "Invalid"
  terminated = True
elif computer_choice > user_choice:
  result = "Lose"
  if(user_choice == 0 and computer_choice == 2):
    result = "Win"
elif computer_choice == user_choice:
  result = "Draw"
elif computer_choice < user_choice:
  result = "Win"
  if(user_choice == 2 and computer_choice == 0):
    result = "Lose"

if not terminated:
  print(possibilities[user_choice])
  print("Computer chose:")
  print(possibilities[computer_choice])

# Alternative solution for game logic

''' if user_choice == 0:
  if computer_choice == 0:
    result = "Draw"
  elif computer_choice == 1:
    result = "Lose"
  elif computer_choice == 2:
    result = "Win"

if user_choice == 1:
  if computer_choice == 0:
    result = "Win"
  elif computer_choice == 1:
    result = "Draw"
  elif computer_choice == 2:
    result = "Lose"

if user_choice == 2:
  if computer_choice == 0:
    result = "Lose"
  elif computer_choice == 1:
    result = "Win"
  elif computer_choice == 2:
    result = "Draw" '''

print(result)