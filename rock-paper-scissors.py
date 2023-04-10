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
choice = input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")
choice = int(choice)

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print(f"Please re-run and choose a number between 0, 1 or 2")

  
import random
rand = random.randint(0,2)
if rand == 0:
  print(f"Computer chose:\n{rock}")
elif rand == 1:
  print(f"Computer chose:\n{paper}")
else:
  print(f"Computer chose:\n{scissors}")
  

#Decision

if choice == rand:
  print(f"We have a draw!")
if choice == 0 and rand == 1:
  print('You lose!')
if choice == 0 and rand == 2:
  print('You win!')
if choice == 1 and rand == 0:
  print('You win!')
if choice == 1 and rand == 2:
  print('You lose!')
if choice == 2 and rand == 0:
  print('You lose!')
if choice == 2 and rand == 1:
  print('You win!')

