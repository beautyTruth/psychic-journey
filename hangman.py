import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from that list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # individual letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # letters that the user has guessed

    # getting the user input
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print(
            f"You have already guessed {user_letter}! Pick another character.")

    else:
        print("Invalid character. Please try again.")
