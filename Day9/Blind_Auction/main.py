from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
input("Welcome to the blind auction! Press 'enter' to start.")

run = True
licits = {}

while run:
    clear()
    name = input("Type your name: ")
    bid = float(input("Type your bid: $"))

    licits[name] = bid

    prompt = input("Are there any more bidders? Y or N: ").lower()

    if prompt == "n":
        run = False

highest_bid = 0

for name in licits:
    licit_amount = licits[name]
    if licit_amount > highest_bid:
        winner = name
        highest_bid = licit_amount

print(f"The winner is {winner} with ${highest_bid}.")

