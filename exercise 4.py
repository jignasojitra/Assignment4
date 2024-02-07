import random


def guess_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    while True:
        # Get user's guess
        guess = int(input("Guess the number between 1 and 10: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Correct!")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


# Call the function to start the game
guess_number()

