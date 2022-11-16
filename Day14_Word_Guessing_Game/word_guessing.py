# --- coding: utf-8 ---
# @FileName  :word_guessing.py
# @Time      :11/16/2022 10:47 PM
# @Author    :Abraham
# @Software  :PyCharm

import random

words = ["Amazing", "beautiful", "confident", "Development", "Ecstatic", "Field", "Great", "honest", "illustrate",
         "japan", "kind", "Lovely", "machine", "native", "obtain", "programmer", "quality", "rare", "safe", "teacher",
         "unique", "vacation", "wonderful", "x-mass", "yummy", "zeal"]

# Here the user will be asked to enter their name first
name = input("What is your NAME ? ")
print("Best of Luck! ", name)
word = random.choice(words)
# print(word)
print("Please guess the characters: ")
guesses = ''
# we can use any number of turns here
turns = len(word)
while turns > 0:
    # counting the number of times a user is failed to guess the right character
    failed = 0
    # all the characters from the input word will be taken one at a time.
    for char in word:
        # here, we will comparing that input character with the character in guesses
        if char in guesses:
            print(char)
        else:
            print("_")
            # for every failure of the user 1 will be incremented in failed
            failed += 1
    if failed == 0:
        # user will win the game if failure is 0 and 'Congratulations you won!!' will be given as output
        print("Congratulations you won!!")

        # this will print the correct word
        print("The correct word is: ", word)
        break
    # if the user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("Guess another character:")
    # every input character will be stored in guesses
    guesses += guess
    # here, it will check input with the character in word
    if guess not in word:
        turns -= 1
        print("Wrong Guess")
        # this will print the number of turns left for the user
        print("You have ", + turns, 'turns left ')
        if turns == 0:
            print("Sorry, you lose!!")
