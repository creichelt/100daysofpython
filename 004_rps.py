import random

rock = '''
    ________
---'   _____)
      (______)
      (______)
      (_____)
---.__(____)
'''

paper = '''
    ________
---'  ______)____
          _______)
         _________)
        _________)
---.__________)
'''

scissors = '''
    ________
---'   _____)____
          _______)
       ___________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]
computer = random.randint(0,2)

user = int(input("\nLet's play Rock, Paper, Scissors. Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

if user > 2 or user < 0:
    print("Invalid input, you lose.")
else:
    print("\nYou chose: " + images[user])
    print("Computer chose: " + images[computer])
    if user == 0 and computer == 2:
        print("You win.")
    elif computer == 2 and user == 0:
        print("You lose.")
    elif computer > user:
        print("You lose.")
    elif user > computer:
        print("You win.")
    elif computer == user:
        print("It's a draw.")

print('')
