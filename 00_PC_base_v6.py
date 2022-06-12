""" I added 05_budget_checker_v3 to 00_PC_base_v5 to get this new code.
In this code, the items will be printed neatly next to the price per unit. It
will also print the price from cheapest to most expensive for all the items.
It will also print the cheapest item and the most expensive item per unit that
the user can afford with their budget. It will also print the cheapest item
and the most expensive item per unit regardless of the users budget and it
will also print the cheapest item and the most expensive item according to
price.
"""

import numpy as np


def check_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():
            print("Error – please enter a name.")
        else:
            return response


def check_measurement_units(question, valid_choices):
    unit_choice_error = "Sorry that is not a valid unit"
    global choice
    choice = input(question).lower()
    for unit in valid_choices:
        if choice in unit:
            choice = unit[0].title()
            return choice

    print(unit_choice_error)
    return check_measurement_units(question, valid_choices)


# a float checking function
def float_checker(question):
    global response
    valid = False
    while not valid:
        try:
            response = float(input(question))
            valid = True
        except ValueError:
            print("Error – you must enter a number.")
    return response


def yes_no_response(question):
    error_message = "Please answer 'Y' or 'N'"
    valid_responses = ['y', 'n', 'yes', 'no']
    y_n = input(question).lower()
    while y_n not in valid_responses:
        print(error_message)
        y_n = input(question).lower()

    if y_n[0] == 'n':
        return False
    else:
        return True


def item_data(item_info, item_place, item, unit):
    if len(item_info) == 1:
        print(f"{item[0]}: ${item_place[0][0]:.2f} per {unit}")
    elif len(item_info) == 2:
        print(f"{item[0]}: ${item_place[0][0]:.2f} per {unit}")
        print(f"{item[1]}: ${item_place[1][0]:.2f} per {unit}")
    elif len(item_info) == 3:
        print(f"{item[0]}: ${item_place[0][0]:.2f} per {unit}")
        print(f"{item[1]}: ${item_place[1][0]:.2f} per {unit}")
        print(f"{item[2]}: ${item_place[2][0]:.2f} per {unit}")
    elif len(item_info) == 4:
        print(f"{item[0]}: ${item_place[0][0]:.2f} per {unit}")
        print(f"{item[1]}: ${item_place[1][0]:.2f} per {unit}")
        print(f"{item[2]}: ${item_place[2][0]:.2f} per {unit}")
        print(f"{item[3]}: ${item_place[3][0]:.2f} per {unit}")


def budget_checker(budget, item_price, item_name, price_per_unit):
    unit_list = []
    print(f"Your budget is ${budget}")
    items = zip(item_price, item_name)
    for price, name in items:
        if price > budget:
            print(f"{name}: is too expensive.")
        elif price <= budget:
            print(f"{name}: is affordable.")
    price_ppu = zip(item_price, price_per_unit)
    for cost, unit in price_ppu:
        if cost <= budget:
            unit_list.append(unit)
    if len(unit_list) == 0:
        print("Sorry, no items are affordable with your budget.")
    else:
        print(f"Average price per unit is ${np.mean(unit_list):.2f}")
        print("Cheapest item affordable with your budget is:", item_name[price_per_unit.index(min(unit_list))])
        print("Most expensive item affordable with your budget is:", item_name[price_per_unit.index(max(unit_list))])
    print("Cheapest item is:", item_name[item_price.index(min(item_price))])
    print("Most expensive item is:", item_name[item_price.index(max(item_price))])
    print("Cheapest item per unit is:", item_name[price_per_unit.index(min(price_per_unit))])
    print("Most expensive item per unit is:", item_name[price_per_unit.index(max(price_per_unit))])
    if len(unit_list) > 0:
        print(f"Recommended item is {item_name[price_per_unit.index(min(unit_list))]}")

# initialize comparer loop so that it runs at least once
item_list = []
count = 0
MAX_ENTRIES = 5
price_list = []
amount_list = []
price_unit_list = []
original_data_list = [[], [], [], [], []]
inputs = 0
item_price_list = []
original_price_unit_list = []

# Main routine
# TO get the name of the user
name = check_blank("What is your name? ")
# Getting the measurement units that are going to be used to compare different
# items
unit = check_measurement_units("Please enter the measurement unit: ",
                               [["kilogram", "kg", "1"], ["litre", "l", "2"]])
print(f"You chose {unit} as the unit")
budget = float_checker("What is your budget: ")


# To get the name of the products that they are going to compare.
while count < MAX_ENTRIES:
    if MAX_ENTRIES - count > 1:
        for i in range(5):
            print(f"\nYou have {MAX_ENTRIES - count} entries left.")
            item_input = yes_no_response(
                "Do you have an item to compare (Y or N)? ")
            if item_input:
                item_name = input("Please enter the name of the item: ").title()
                count += 1
                item_list.append(item_name)
                price = float_checker("What is the price of the item: ")
                amount = float_checker("How many units is the item: ")
                price_list.append(price)
                amount_list.append(amount)
                inputs += 1
            else:
                if inputs > 0:
                    for i in range(len(price_list)):
                        price_unit = price_list[i] / amount_list[
                            i]  # Calculating the price per unit.
                        price_unit_list.append(price_unit)
                        original_price_unit_list.append(round(price_unit, 2))
                        price_unit_list = list(
                            np.around(np.array(price_unit_list), 2))
                        original_data_list[i].append(price_unit_list[i])
                        original_data_list[i].append(i + 1)
                    price_unit_list.sort()
                    print("Item prices per unit (cheapest to most expensive):")
                    print("$", end="")
                    print(*price_unit_list, sep="\n$")
                    item_data(price_unit_list, original_data_list, item_list, unit)
                    budget_checker(budget, price_list, item_list, original_price_unit_list)
                    print(f"Thank you for using the program {name}.")
                    exit()
                else:
                    print(f"Thank you for using the program {name}.")
                    exit()

if count < MAX_ENTRIES:
    print(f"\nYou have made {count} entries\nThere are still"
          f" {MAX_ENTRIES - count} entries available")
else:
    print(f"\nYou have made all the available entries")
    for i in range(5):
        price_unit = price_list[i] / amount_list[
            i]  # Calculating the price per unit.
        price_unit_list.append(price_unit)
        original_price_unit_list.append(round(price_unit, 2))
        price_unit_list = list(np.around(np.array(price_unit_list), 2))
        original_data_list[i].append(price_unit_list[i])
        original_data_list[i].append(i + 1)
        price_unit_list.sort()
    print("$", end="")
    print(*price_unit_list, sep="\n$")
    print(f"{item_list[0]}: ${original_data_list[0][0]:.2f} per {unit}")
    print(f"{item_list[1]}: ${original_data_list[1][0]:.2f} per {unit}")
    print(f"{item_list[2]}: ${original_data_list[2][0]:.2f} per {unit}")
    print(f"{item_list[3]}: ${original_data_list[3][0]:.2f} per {unit}")
    print(f"{item_list[4]}: ${original_data_list[4][0]:.2f} per {unit}")
    budget_checker(budget, price_list, item_list, original_price_unit_list)
    print(f"Thank you for using the program {name}.")





