import random

def play_game():
    number_to_guess = random.randint(1, 100)
    max_attempts = 7
    attempts_used = 0

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts_used < max_attempts:
        guess_input = input("Enter your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess_input)
        attempts_used += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts_used} attempts.")
            return

        attempts_remaining = max_attempts - attempts_used
        if attempts_remaining > 0:
            print(f"Attempts left: {attempts_remaining}")

    print(f"Out of attempts! The number was {number_to_guess}.")

def main():
    play_game()
    while True:
        again = input("Play again? (yes/no): ").strip().lower()
        if again == "yes":
            play_game()
        elif again == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()