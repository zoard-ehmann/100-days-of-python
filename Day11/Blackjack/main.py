from art import logo
from replit import clear
import random

def start():
    """Main entry point for the Blackjack game."""
    if input("Do you want to play Blackjack? Y or N: ").lower() == 'y':
        blackjack()
    else:
        print("Bye!")

def blackjack():
    """Set up variables and initial state, define helper functions,
    then run the game itself."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    players = [
        {
            "name": "computer",
            "cards": [],
            "score": 0,
        },
        {
            "name": "user",
            "cards": [],
            "score": 0,
        }
    ]
    computer = players[0]
    user = players[1]

    def calculate_score(player):
        """Calculates and returns player score."""
        return sum(player["cards"])

    def calculate_ace(player):
        """Takes the player dictionary, then calculates and sets the appropriate ace value based on the player score."""
        if calculate_score(player) > 21:
            player["cards"].remove(11)
            player["cards"].append(1)

    def draw_card(player):
        """Takes the player dictionary and assigns a random card and
        the corresponding score to them."""
        player["cards"].append(random.choice(deck))
        if 11 in player["cards"]:
            calculate_ace(player)
        player["score"] = calculate_score(player)

    def check_blackjack():
        """Checks all the players for Blackjack hand."""
        for player in players:
            if player["score"] == 21:
                return True
        return False

    def calculate_result():
        """Calculates and outputs the result of the game."""
        if user["score"] > 21:
            print("You went through 21. You lose.")
        elif computer["score"] > 21:
            print("The dealer went through 21. You win!")
        elif user["score"] == computer["score"]:
            print("It's a draw.")
        elif user["score"] > computer["score"]:
            print("You win!")
        else:
            print("You lose.")

    def end_of_game():
        """Outputs the final hands, calls the result calculation
        and restarts the game."""
        print(f"\tYour final hand: {user['cards']}, Final score: {user['score']}")
        print(f"\tComputer's final hand: {computer['cards']}, Final score: {computer['score']}")
        calculate_result()
        start()

    clear()
    print(logo)
    for _ in range(2):
        draw_card(computer)
        draw_card(user)

    has_blackjack = check_blackjack()

    while computer["score"] < 17:
        draw_card(computer)

    play = True

    while play:
        print(f"\tYour cards: {user['cards']}, Current score: {user['score']}")
        print(f"\tComputer's first card: {computer['cards'][0]}")

        if has_blackjack or user["score"] > 21 or input("Would you like to draw another card? Y or N: ").lower() == "n":
            play = False
            end_of_game()
        
        draw_card(user)

start()
