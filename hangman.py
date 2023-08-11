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

    lives = 6

    # getting the user input
    while len(word_letters) > 0 and lives > 0:
        # letters used

        # " ".join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have ', lives,
              'left and have used the following letters: ', " ".join(used_letters))

        # what the current word is based on correctly guessed letters
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # take away one life if wrong guess

        elif user_letter in used_letters:
            print(
                f"You have already guessed {user_letter}! Pick another character.")

        else:
            print("Invalid character. Please try again.")
    # it gets to here when len(word_letters) == 0 *or* when lives == 0
    if lives == 0:
        print('Sorry, you died. The word was', word)
    else:
        print('You guessed the word,', word, '!!')


hangman()
