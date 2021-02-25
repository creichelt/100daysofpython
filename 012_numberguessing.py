import random

logo = """
 _   _                 _               _____                     _
| \ | |               | |             |  __ \                   (_)
|  \| |_   _ _ __ ___ | |__   ___ _ __| |  \/_   _  ___  ___ ___ _ _ __   __ _
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | __| | | |/ _ \/ __/ __| | '_ \ / _` |
| |\  | |_| | | | | | | |_) |  __/ |  | |_\ \ |_| |  __/\__ \__ \ | | | | (_| |
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|   \____/\__,_|\___||___/___/_|_| |_|\__, |
                                                                          __/ |
                                                                         |___/
"""

EASY = 10
HARD = 5
answer = random.randint(1,100)

def check(limit):
    count = limit
    while count > 0:
        print(f"You have {count} attempts remaining to guess the number!")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print("WINNER")
            count = 0
        elif guess > answer:
            print("too high\n")
        else:
            print("too low\n")
        count -=1

def game():
    print("\nWelcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    difficulty = input("\nChoose a difficulty: Type 'easy' or 'hard': ")
    print("")

    if difficulty == 'easy':
        check(EASY)
    elif difficulty == 'hard':
        check(HARD)

print(logo)
game()
