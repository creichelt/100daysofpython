import random, os

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw(user):
    card = random.choice(cards)
    user.append(card)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score,dealer_score):
    if player_score == dealer_score:
        return "Draw."
    elif dealer_score == 0:
        return "You lose, dealer has Blackjack."
    elif player_score == 0:
        return "Blackjack, you win."
    elif player_score > 21:
        return "You went over, you lose."
    elif dealer_score > 21:
        return "Dealer went over, you win."
    elif player_score > dealer_score:
        return "You win."
    else:
        return "You lose."

def game():
    player =[]
    dealer =[]
    is_game_over = False

    print(logo)

    for _ in range(2):
        draw(player)
        draw(dealer)

    while not is_game_over:
        player_score = calc_score(player)
        dealer_score = calc_score(dealer)
        print(f"\n Your cards: {player}, score: {player_score}")
        print(f" Dealer's first card {dealer[0]}\n")

        if player_score == 0 and dealer_score != 0 or player_score > 21:
            is_game_over = True
        else:
            play = input(" Type 'y' if you want to another card: ")
            if play == 'y':
                draw(player)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        draw(dealer)
        dealer_score = calc_score(dealer)

    print(compare(player_score,dealer_score))
    print('')
    print(f"Your final hand is {player}. The Dealer's final hand is {dealer}\n")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") =='y':
    os.system('clear')
    game()
