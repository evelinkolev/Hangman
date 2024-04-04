import random
import hangman_words
from hangman_art import stages, logo
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py.
chosen_word = random.choice(hangman_words.word_list)

is_game_over = False
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in chosen_word:
    display += "_"

while not is_game_over:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the
        #  word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            is_game_over = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        is_game_over = True
        print("You win!")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
