import random

toss = random.random()

if toss < 0.5:
    print("Heads")
else:
    print("Tails")

print("Toss was: {}".format(toss))

print('')

names_string = input("Enter a list of names, seperated by comma: ")
names = names_string.split(", ")

print(random.choice(names) + " has to pay the bill")
