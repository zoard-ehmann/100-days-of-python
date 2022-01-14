MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

def print_resources():
    """Outputs the coffee machine's resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def choose_menu_item(choice):
    """Takes the user choice and returns the corresponding product."""
    return MENU[choice]


def check_sufficient(selected):
    """Takes the selected product and returns True if the resources are sufficient."""
    for ingredient in selected["ingredients"]:
        if selected["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Prompts for user coins and returns the sum."""
    print("Please insert coins.")
    inserted_money = 0
    inserted_money += int(input("Quarters: ")) * COINS["quarter"]
    inserted_money += int(input("Dimes: ")) * COINS["dime"]
    inserted_money += int(input("Nickels: ")) * COINS["nickel"]
    inserted_money += int(input("Pennies: ")) * COINS["penny"]
    return inserted_money


def check_transaction(selected, inserted_money):
    """Takes the selected product and inserted money and returns True if the money is sufficient."""
    if selected["cost"] > inserted_money:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    print(f"Change: ${(inserted_money - selected['cost']):.2f}")
    return True


def deduct_resources(selected, resources):
    """Takes the selected product and available resources, subtracts the consumed resources and returns the remaining resources."""
    new_resources = {}
    for ingredient in resources:
        if ingredient in selected["ingredients"]:
            new_resources[ingredient] = resources[ingredient] - selected["ingredients"][ingredient]
        else:
            new_resources[ingredient] = resources[ingredient]
    return new_resources


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
machine_is_on = True


while machine_is_on:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "off":
        machine_is_on = False
    elif prompt == "report":
        print_resources()
    else:
        chosen_product = choose_menu_item(prompt)
        if check_sufficient(chosen_product) and check_transaction(chosen_product, process_coins()):
                money += chosen_product["cost"]
                resources = deduct_resources(chosen_product, resources)
                print("Enjoy your coffee!")
    print()