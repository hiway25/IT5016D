#  GuessNumber2
#  Author: Helen Thomas
# Date: 11.08.2023

import random

secret_number = random.randint(1, 10)
previous_guess = None

print("Welcome to the Guessing Game!")
print("Try to guess the secret number between 1 and 9.")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the secret number", secret_number, "\n")
        break
    elif guess == previous_guess:
        print("You already guessed that number.")
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    previous_guess = guess