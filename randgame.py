import random

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You need to guess the number.")
    print("Choose a difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (7 chances)")
    print("3. Hard (5 chances)")
    print("Good luck!")

def set_difficulty(level):
    if level == 'easy':
        return 10
    elif level == 'medium':
        return 7
    elif level == 'hard':
        return 5
    else:
        print("Invalid difficulty level. Defaulting to 'easy'.")
        return 10

def play_game():
    display_welcome_message()
    
    # Choose difficulty
    difficulty = input("Select difficulty level (easy, medium, hard): ").lower()
    attempts = set_difficulty(difficulty)

    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts_remaining = attempts
    guessed_correctly = False

    while attempts_remaining > 0 and not guessed_correctly:
        try:
            guess = int(input(f"You have {attempts_remaining} attempts left. Make a guess: "))
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            attempts_remaining -= 1  # Reduce the number of attempts left

            if guess == number_to_guess:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts - attempts_remaining} attempts.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    if not guessed_correctly:
        print(f"Sorry, you've run out of attempts! The number was {number_to_guess}.")

if __name__ == "__main__":
    play_game()