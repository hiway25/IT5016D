#  GuessMyNumber.py
#  Author: Helen Thomas
#  Date: 10.08.2023

import random

secret_number = random.randint(1, 100)
previous_guess = None
attempts = 0

print("Welcome to the Guessing Game!")
print("Try to guess the secret number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed the secret number", secret_number, "in", attempts, "attempts.")
        break
    elif guess == previous_guess:
        print("You already guessed that number.")
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    previous_guess = guess
