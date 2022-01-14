from art import logo
from replit import clear
import random

def game():
    """Main entry point of the game. Its dependencies declared within."""

    def set_difficulty(chosen_difficulty):
        """Takes user input and returns the lives accordingly."""
        if chosen_difficulty == "easy":
            return 10
        return 5

    def correct_guess(guess):
        """Takes a guess as a parameter. Returns 'True' if the guess equals to the goal."""
        if guess == goal:
            return True
        elif guess > goal:
            print("\tToo high.")
        else:
            print("\tToo low.")

        return False

    print(logo)
    print("Welcome to the Guess The Number game!")
    print("I'm guessing a number between 1-100.")

    goal = random.randint(1, 100)
    lives = set_difficulty(input("Type 'easy' for easy difficulty, otherwise press 'Enter': ").lower())
    
    end_of_game = False
    while not end_of_game:
        print(f"\tRemaining guesses: {lives}")

        if not correct_guess(int(input("Make a guess: "))):
            lives -= 1
            if lives == 0:
                print("You've run out of guesses. You lose.")
                end_of_game = True
        else:
            print(f"You got it, the number was {goal}!")
            end_of_game = True
    
    if input("\nType 're' to start another game: ").lower() == "re":
        clear()
        game()

    print("Bye!")

game()