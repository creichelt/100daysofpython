print("Welcome to Treasure Island!\n")
print("\nYour mission is to find the treasure...|")

print("\nWARNING: not intended for children!\n")

cross = input("You're at a cross road. Do you want to take 'left' or 'right'? ").lower()

if cross == 'left':
    lake = input("You came to a lake. There is an island in the middle. Do you want to 'wait' for a boat or 'swim' across? ").lower()
    if lake == 'wait':
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one green. Which color do you choose? ").lower()
        if color == 'yellow':
            print("You found the treasure!")
            print("You win!")
        elif color == 'green':
            print("You get showered wih acid...")
            print("Game over!")
        elif color == 'red':
            print("Blades come crashing down on you...")
            print("Game over!")
    elif lake == 'swim':
        print("A sea monster grabs your leg....")
        print("Game over!")
elif cross == 'right':
    print("You fall into a pit...")
    print("Game over!")
