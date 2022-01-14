from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    prompt = input(f"What would you like? ({menu.get_items()}): ")
    if prompt == "off":
        is_on = False
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
