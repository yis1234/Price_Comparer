""" I added 04_product_comparer_v7 to 00_PC_base_v4 to get this new code.
In this code, the items will be printed neatly next to the price per unit. It
will also print the price from cheapest to most expensive for all the items.
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


# initialize comparer loop so that it runs at least once
item_list = []
count = 0
MAX_ENTRIES = 5
price_list = []
amount_list = []
price_unit_list = []
original_data_list = [[], [], [], [], []]
inputs = 0

# Main routine
# TO get the name of the user
name = check_blank("What is your name? ")
# Getting the measurement units that are going to be used to compare different
# items
unit = check_measurement_units("Please enter the measurement unit: ",
                               [["kilogram", "kg", "1"], ["litre", "l", "2"]])
print(f"You chose {unit} as the unit")

# To get the name of the products that they are going to compare.
while count < MAX_ENTRIES:
    if MAX_ENTRIES - count > 1:
        print(f"\nYou have {MAX_ENTRIES - count} entries left.")
        for i in range(5):
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
                        price_unit_list = list(
                            np.around(np.array(price_unit_list), 2))
                        original_data_list[i].append(price_unit_list[i])
                        original_data_list[i].append(i + 1)
                    price_unit_list.sort()
                    print("Item prices per unit (cheapest to most expensive):")
                    print("$", end="")
                    print(*price_unit_list, sep="\n$")
                    item_data(price_unit_list, original_data_list, item_list, unit)
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
    print(f"Thank you for using the program {name}.")





