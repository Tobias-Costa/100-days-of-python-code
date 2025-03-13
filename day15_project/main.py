from data import MENU, resources
from art import plug, coffee

def turn_off():
    print("Turning off...")
    print(plug)

def report():
    for resource, value in resources.items():
        if resource == "water" or resource == "milk":
            print(f"{resource.title()}: {value}ml")
        elif resource == "coffee":
            print(f"{resource.title()}: {value}g")
        elif resource == "money":
            print(f"{resource.title()}: ${value}")

def format_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return water, milk, coffee

def format_ingredients(order):
    water = MENU[order]["ingredients"]["water"]
    milk = MENU[order]["ingredients"]["milk"]
    coffee = MENU[order]["ingredients"]["coffee"]
    return water, milk, coffee

def check_resources(order):
    water_rs, milk_rs, coffee_rs = format_resources()
    water_ing, milk_ing, coffee_ing = format_ingredients(order)
    resource_lack = []

    if water_rs < water_ing:
        resource_lack.append("water")
    if milk_rs < milk_ing:
        resource_lack.append("milk")
    if coffee_rs < coffee_ing:
        resource_lack.append("coffee")
    
    if len(resource_lack) != 0:
        return False, resource_lack

    return True, None
    
def update_resources(order, money):
    water_ing, milk_ing, coffee_ing = format_ingredients(order)
    resources["water"] -= water_ing
    resources["milk"] -= milk_ing
    resources["coffee"] -= coffee_ing
    resources["money"] += money

print(coffee)
while True:
    print(f"\nCOFFEE MACHINE\n")

    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        turn_off()
        break
    elif user_order == "report":
        report()
        continue
    elif not user_order in MENU:
        print("Sorry! That is not in our menu.")
        continue


    is_resources_sufficient, resource_lack = check_resources(user_order)

    if not is_resources_sufficient:
        if len(resource_lack) == 1:
            print(f"Sorry, there is not enough {resource_lack[0]}")
        elif len(resource_lack) == 2:
            print(f"Sorry, there is not enough {resource_lack[0]} and {resource_lack[1]}")
        elif len(resource_lack) == 3:
            print(f"Sorry, there is not enough {resource_lack[0]}, {resource_lack[1]} and {resource_lack[2]}")
        continue 

    try:
        quarters = int(input("Insert the quarters($0.25) coins quantity: ")) * 0.25
        dimes = int(input("Insert the dimes($0.10) coins quantity: ")) * 0.1
        nickles = int(input("Insert the nickles($0.05) coins quantity: ")) * 0.05
        pennies = int(input("Insert the pennies($0.01) coins quantity: ")) * 0.01
    except ValueError:
        print("Invalid input. Please enter an integer quantity.")
        continue

    total_money = quarters + dimes + nickles + pennies
    coffee_price = MENU[user_order]["cost"]

    if total_money < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        continue
    elif total_money > coffee_price:
        change = round(total_money - coffee_price, 2)
        print(f"Here is ${change} dollars in change.")

    update_resources(user_order, coffee_price)
    print(f"Here is your {user_order}. Enjoy!")

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


# TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.


# TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.