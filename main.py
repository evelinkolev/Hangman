import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in chosen_word:
    display += "_"

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives = 6

is_game_over = False
while not is_game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1. If lives goes down to 0 then
    #  the game should stop and it should print "You lose.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            is_game_over = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        is_game_over = True
        print("You win!")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
    #  remaining.
    print(stages[lives])
