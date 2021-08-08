import random
import math
from Words import Words
# Main Function


def __main__():
    disect_word()
    guess_word()
    return disect_word()


def get_word():  # gets random word from Words.py
    word = random.choice(Words)
    return word


def disect_word():  # disects a random word selected into its individual letters
    word_disect = word
    word_letters = list(word_disect)
    # print(word_letters)
    return word_letters
    # print(word_letters)


def guess_word():  # player types into terminal
    guess = input("Please type a letter to guess: ")
    guess = guess[0]
    # print(guess)

    for i in disect_word():
        if (guess == i):
            guessed_letters.add(guess)
            correct_letters.append(guess)

        for letter in correct_letters:
            if (letter == i):
                print(letter)

        else:
            guessed_letters.add(guess)
            print("_")

    print("Letters that you've guessed: " + str(guessed_letters))

    print("To continue playing, press 'enter', or type EXIT to end")
    inp_enter = input("")
    if inp_enter != "EXIT":
        guess_word()


word = get_word()
guessed_letters = set()
correct_letters = list()

__main__()