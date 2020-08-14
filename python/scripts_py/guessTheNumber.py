#!/usr/local/bin/python3
# This is a guess the number game.

import random


secretNum = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Allow player to guess 6 times
for chance in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    if guess < secretNum:
        print("Too low")
    elif guess > secretNum:
        print("Too high")
    else:
        break
    print("")

if guess == secretNum:
    print("Congrats! You've guessed the number in " + str(chance) + " guesses!")
else:
    print("You did not guess the number. It was " + str(secretNum))
