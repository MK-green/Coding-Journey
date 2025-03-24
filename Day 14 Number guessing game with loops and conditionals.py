import random # We need this to generate a random number

import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

print(f"Secret number is {secret_number}")  # For debugging
while guess != secret_number:
    print(f"Current guess: {guess}")
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess again: "))

print(f"Congratulations! The number was {secret_number}.")