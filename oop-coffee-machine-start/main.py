from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
on = True


while on:
    drink_menu = coffee_menu.get_items()
    choice = input(f"What would you like to drink? >> {drink_menu} >>> ")
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif choice == "off" or choice == "shutdown now":
        print("Powering down....")
        on = False
    else:
        drink = coffee_menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
