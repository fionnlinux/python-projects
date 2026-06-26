#!/usr/bin/env python3
"""
dads-number-guessing-game.py
A CLI number guessing game written as a first Python project.

Players guess a random number between 1 and 100.
Includes input validation and a performance rating.

Usage:
    python3 dads-number-guessing-game.py

Requirements: Python 3 (standard library only)

Author: fionnlinux
Date: May 2026
"""

import random


# Functions

def performance_message(attempts):
    """Return a performance message based on number of attempts."""
    if attempts <= 5:
        return "Outstanding! You're a natural!"
    elif attempts <= 10:
        return "Good effort — not bad at all!"
    else:
        return "Keep practising — you'll get faster!"


# Setup

# Ask for name once outside the game loop so it
# doesn't ask again on each playthrough
player_name = input("Before we begin, please tell us your name: ")
print("Welcome to Dad's amazing number guessing game, " + player_name + "!")


# Main game loop

playing = True

while playing:
    # Pick a new random number at the start of each game
    secret = random.randint(1, 100)
    print("\nI have picked a secret number between 1 and 100.")
    print("Guess numbers and I will give you a hint each time!")

    guess = 0
    attempts = 0

    # Keep asking until the player guesses correctly
    while guess != secret:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            # Catches non-numeric input that would crash int()
            print("Oops! Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret:
            print("You got it in", attempts, "guesses! Congratulations " + player_name + "!")
            print(performance_message(attempts))
        elif guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")

    # Play again

    # Keep asking until a valid yes or no answer is given
    while True:
        again = input("\nWould you like to play again? yes or no: ")
        if again == "yes" or again == "no":
            break
        print("Please type yes or no.")

    if again == "no":
        playing = False
        print("Thanks for playing " + player_name + "! See you next time!")
