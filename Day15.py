import random

print ("=== Number Guessing Game ===\n")

while True: # Main play-again loop
    #  Set up a new round
    secret_number = random.randint(1, 10)
    guesses = 0
    print("I'm thinking of a number between 1 and 10...")

    while True: # Guessingg loop
        try:

            guess = int(input("Your guess: "))
            guesses += 1

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

        except ValueError:
            print("That's not a number! Please enter a valid integer.")
            continue

        # Now check the guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
                print(f"Correct! You got it in {guesses} guesses!")
                break # Exit the innter guessing loop
        
    # After winning, ask to play again
    while True:
         play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
         if play_again in ['y', 'yes']:
              print("\n" + "="*30 + "\n")
              break
         elif play_again in ['n', 'n']:
              print("Thanks for playing! Goodbye.")
              exit()  #End the entire program
         else:
              print("Please anser with 'y' or 'n'.")


