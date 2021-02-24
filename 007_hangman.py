import random

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=======
''','''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=======
''','''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=======
''','''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=======
''','''
  +---+
  |   |
  0   |
  |   |
      |
      |
=======
''','''
  +---+
  |   |
  0   |
      |
      |
      |
=======
''','''
  +---+
  |   |
      |
      |
      |
      |
=======
''']

word_list = [
'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom',
'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini',
'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo',
'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph',
'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri',
'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip',
'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord',
'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled',
'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo',
'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku',
'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot',
'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw',
'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy',
'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk',
'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky',
'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic',
'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx',
'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz',
'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue',
'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb',
'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz',
'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied',
'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript',
'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown',
'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex',
'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy',
'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy',
'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful',
'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']

chosen_word = random.choice(word_list)
lives = 6
display = []
for i in range(0,len(chosen_word)):
    display.append('_')
tried = []

print("\n Welcome to Hangman.\n")
print("Let's play a round\n")
print(display)

end_of_game = False
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    tried.append(guess.upper())
    if guess not in chosen_word:
        print("You guessed " + guess + ". That's not in the word. You lose a life\n")
        lives -= 1
        if lives == 0:
            print("\nYou lose.\n The word was: " + chosen_word)
            end_of_game = True
    else:
        for i in range(len(chosen_word)):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter.upper()

    print(display)
    print(stages[lives])
    print("You tried:")
    print(tried)

    if "_" not in display:
        end_of_game = True
        print("\nYou won\n")
