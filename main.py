import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Continue until the user guesses correctly
    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
    
    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

# Start the game
guess_the_number()
