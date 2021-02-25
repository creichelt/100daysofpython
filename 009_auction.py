import os, operator

print('Welcome to the auction!\n')

# simple way
def highest_bidder(dict):
    high = 0
    winner = ''
    for i in record:
        if dict[i] > high:
            high = dict[i]
            winner = i
    print(f"The winner is {winner} with a bid of ${high}")

bids = {}

while True:
    name = input("What is you name? ")
    bid = input("What is your bid? $")

    bids[name] = bid

    more_bidders = input("Are there other bidders?")
    os.system('clear')
    if more_bidders == 'no':
        # simple way:
        highest_bidder(bids)
        # advanced way only needs below line, no function, no call:
        # print(f"{max(bids.items(), key=operator.itemgetter(1))[0]} is the winner!")
        break
