import random

# Function
def get_guess(max_number):

    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {max_number}: "))

            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_number}.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Main Game Loop
while True:

    print("\n===== NUMBER GUESSING GAME =====")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = int(input("Choose difficulty (1-3): "))

    if choice == 1:
        max_number = 50
        max_attempts = 10

    elif choice == 2:
        max_number = 100
        max_attempts = 7

    elif choice == 3:
        max_number = 200
        max_attempts = 5

    else:
        print("Invalid choice!")
        continue

    number = random.randint(1, max_number)

    guess = get_guess(max_number)

    attempts = 1

    while guess != number and attempts < max_attempts:

        if guess > number:
            print("Too high!")

        else:
            print("Too low!")

        guess = get_guess(max_number)

        attempts += 1

    if guess == number:
        print("Correct! 🎉")
        print("You guessed it in", attempts, "attempts.")

    else:
        print("Game Over! ❌")
        print("The number was:", number)

    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing! 👋")
        break