import random
import math
from Words import Words
# Main Function

def __main__():
    disect_word()
    print("Welcome to Hangman by Maya and Josh! Your word is " + str(len(word)) + " letters long")
    guess_word()
    return disect_word()


def get_word():  # gets random word from Words.py
    word = random.choice(Words)
    return word


def disect_word():  # disects a random word selected into its individual letters
    word_disect = word
    word_letters = list(word_disect)
    return word_letters


def guess_word():  # player types into terminal
    guess = input("Please type a letter to guess: ")
    guess = guess[0] #guess should just be 1 letter, if it isn't then this shortens it to first characters

    for i in disect_word():
        won = False #Sets win condition to false
        l_printed = False #Sets if a correct letter has been printed to false
        if (guess == i):
            guessed_letters.add(guess)
            correct_letters.add(guess)

        incorrect_letters = (guessed_letters - correct_letters) #Compares guessed and correct letters to create a list of incorrect letters, used to calculate lives.

        for letter in correct_letters:
            if (letter == i):
                print(letter)
                l_printed = True #Hi mims!!! Idk if you'll see this but this is here as a boolean expression to only print the '_' when a word isn't guessed correctly!

        else:
            guessed_letters.add(guess)
            if l_printed == False: # I'm actually so smart
                print("_")

    print("Letters that you've guessed: " + str(guessed_letters))

    lives = slives - len(incorrect_letters) #takes number of letters wrong away from lives

    print("You have " + str(lives) + " Lives remaining")

    if set(disect_word()) == correct_letters: #Win condition
            print("You have won!")
            won = True

    if won == True:
        return

    if lives == 0:
        print("Game over, the word was " + str(word) + "!")
        return

    print("To continue playing, press 'enter', or type EXIT to end")
    inp_enter = input("")
    if inp_enter != "EXIT":
        guess_word()


word = get_word()
slives = len(word) + 2
guessed_letters = set()
correct_letters = set()
incorrect_letters = set()

__main__()
