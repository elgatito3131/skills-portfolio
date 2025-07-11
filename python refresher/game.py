import random

def guess_the_number():
    """
    A simple number guessing game to demonstrate basic Python concepts.
    """
    # The computer generates a random secret number between 1 and 50.
    secret_number = random.randint(1, 50)
    
    # Set the number of allowed guesses.
    max_guesses = 6
    
    print("---------------------------------------")
    print(" I'm thinking of a number between 1 and 50.")
    print(f" You have {max_guesses} tries to guess it.")
    print("---------------------------------------")

    # Loop for the number of guesses the user has.
    for guess_count in range(1, max_guesses + 1):
        try:
            # Prompt the user for their guess.
            guess = int(input(f"Try #{guess_count}: Enter your guess: "))

            # Check if the guess is correct, too low, or too high.
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                # The guess is correct.
                print(f"🎉 You got it! The secret number was {secret_number}.")
                print(f"You guessed it in {guess_count} tries.")
                return # Exit the function since the game is won.

        except ValueError:
            # This handles cases where the user enters text instead of a number.
            print("Oops! That's not a valid number. Try again.")

    # If the loop finishes, the user ran out of guesses.
    print("\nGame over! You ran out of tries.")
    print(f"The secret number was {secret_number}.")

# This line calls the function to start the game when the script is run.
if __name__ == "__main__":
    guess_the_number()