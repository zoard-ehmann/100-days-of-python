from art import logo, vs
from game_data import data
from random import choice
from replit import clear

def set_instagrammer(instagrammer, index):
    """Takes an instagrammer dictionary and an index and returns the instagrammer with the assigned index."""
    instagrammer["index"] = index
    return instagrammer

def print_instagrammer(instagrammer):
    """Takes an instagrammer dictionary and prints the content."""
    print(f"{instagrammer['index']}: {instagrammer['name']}, {instagrammer['description']} from {instagrammer['country']}.")

def print_match(a, b):
    """Takes two instagrammer dictionaries and prints out their match."""
    print_instagrammer(a)
    print(vs)
    print_instagrammer(b)

def calc_winner(a, b):
    """Takes two instagrammer dictionaries and returns that who has more followers."""
    if a["follower_count"] > b["follower_count"]:
        return a
    return b

def correct_guess(user_guess, winner):
    """Takes the user guessed index and the actual winner and returns whether the user guessed correctly or not."""
    if user_guess.lower() == winner["index"].lower():
        return True
    return False

def game():
    """Game entry point and variable declarations."""
    score = 0
    a = set_instagrammer(choice(data), "A")
    b = set_instagrammer(choice(data), "B")

    play = True
    while play:
        
        # Check if the 2 randomly selected instagrammers are the same; if so, set 1st with their appropriate index (A - it would be B otherwise) and pick a random for 2nd
        while a["follower_count"] == b["follower_count"]:
            a = set_instagrammer(a, "A")
            b = set_instagrammer(choice(data), "B")

        winner = calc_winner(a, b)

        print(logo)
        print_match(a, b)
        guess = input("\nWho has more followers on Instagram? A or B: ")
        clear()

        if correct_guess(guess, winner):
            score += 1
            a = set_instagrammer(b, "A")
            print(f"That's it! Your score: {score}")
        else:
            print(f"Sorry, that's not correct. Final score: {score}")
            play = False
    
    if input("\nPress 'Enter' to play again or type 'stop' to stop: ").lower() != 'stop':
        clear()
        game()
    print("Bye!")

game()