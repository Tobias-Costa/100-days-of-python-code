from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    print("\nCOFFEE MACHINE\n")
    user_order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_order == "off":
        print("Turning off...")
        break
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    drink = menu.find_drink(user_order)
    if drink is None:
        continue

    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)  