""" Added some extra details to the program to make it more user-friendly.
The program has got more information on where the user inputs their information
and the feedback the user gets.
"""

import numpy as np


def check_blank(question):
    while True:
        response = input(question).title()
        if " " in response:
            if response.count(" ") == 1:
                if response.index(" ") == 0 or response.index(" ") == len(
                        response) - 1:
                    print("Please do not use a space at the beginning or end "
                          "of your input")
                    continue
                else:
                    return response
        if not response.isalpha():
            print("Error – please enter a name.")
        else:
            return response


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = check_blank("Would you like to read the "
                                   "instructions (Y or N)? ").lower()
        instructions = (get_choice(instructions, valid_responses))
    if instructions == "Y":
        print("**********************************************************\n"
              "\n\t\t**** Price Comparer Instructions ****\n"
              "\nYou will be asked your name and then you will be shown how\n"
              "many entries are still available for use.\n"
              "You will then be asked if you have an item to compare/calculate"
              "\nthe price per unit of.\n"
              "Then it will ask you to enter the name of the item.\n"
              "After that it will ask for the price of the item\n"
              "then followed by the amount of units the item is.\n"
              "\nThis process keeps repeating until either all five entries\n"
              "have been successfully made or if you have no more items to\n"
              "compare/calculate.\n"
              "\nOn exit, a summary will be printed in order of:\n"
              "1. Prices per unit from cheapest to most expensive\n"
              "2. The names of the item followed by the price per unit\n"
              "3. Your budget\n"
              "4. The names of the items that are affordable and not\n"
              "5. The average price per unit for all the items\n"
              "6. The cheapest and most expensive item affordable with your "
              "budget\n"
              "7. The cheapest and most expensive item\n"
              "8. The cheapest and most expensive item regardless of your "
              "budget\n"
              "9. The recommended item to purchase\n"
              "10. A farewell message\n"
              "******************************************************\n")


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
            if response <= 0:
                print("Error – you must enter a number greater than 0.")
                valid = False
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


def budget_checker(budget, item_price, item_name, price_per_unit, item_unit):
    unit_list = []
    print(f"\nYour budget is ${budget}\n")
    items = zip(item_price, item_name)
    for price, name in items:
        if price > budget:
            print(f"{name} is too expensive.")
        elif price <= budget:
            print(f"{name} is affordable.")
    price_ppu = zip(item_price, price_per_unit)
    for cost, unit in price_ppu:
        if cost <= budget:
            unit_list.append(unit)
    if len(unit_list) == 0:
        print("\nSorry, no items are affordable with your budget.")
    else:
        print(f"\nThe average price per {item_unit} for your items is "
              f"${np.mean(price_per_unit):.2f}")
        print(f"\nThe cheapest item affordable with your budget is "
              f"{item_name[price_per_unit.index(min(unit_list))]} at "
              f"${min(unit_list)} per {item_unit}")
        print(f"The most expensive item affordable with your budget is "
              f"{item_name[price_per_unit.index(max(unit_list))]} at "
              f"${max(unit_list)} per {item_unit}")
    print(f"\nThe cheapest item is "
          f"{item_name[item_price.index(min(item_price))]} at "
          f"${min(item_price)}")
    print(f"The most expensive item is "
          f"{item_name[item_price.index(max(item_price))]} at "
          f"${max(item_price)}")
    print(f"\nThe cheapest item per {item_unit} is "
          f"{item_name[price_per_unit.index(min(price_per_unit))]} at "
          f"${min(price_per_unit)}")
    print(f"The most expensive item per {item_unit} is "
          f"{item_name[price_per_unit.index(max(price_per_unit))]} at "
          f"${max(price_per_unit)}")
    if len(unit_list) > 0:
        print(f"\nThe recommended item to purchase is "
              f"{item_name[price_per_unit.index(min(unit_list))]}")


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
valid_yes_no = [["y", "yes"], ["n", "no"]]

# Main routine
# TO get the name of the user
show_instructions(valid_yes_no)
name = check_blank("What is your name? ")
# Getting the measurement units that are going to be used to compare different
# items
unit = check_measurement_units("Please enter the measurement unit (kg, l, g, "
                               "ml): ", [["kilogram", "kg", "1"],
                                         ["litre", "l", "2"],
                                         ["gram", "g", "3"],
                                         ["millilitre", "ml", "4"]])
print(f"You chose {unit} as the unit")
budget = float_checker("What is your budget: $")

# To get the name of the products that they are going to compare.
while count < MAX_ENTRIES:
    if MAX_ENTRIES - count > 1:
        for i in range(5):
            print(f"\nYou have {MAX_ENTRIES - count} entries left.")
            item_input = yes_no_response(
                "Do you have an item to compare (Y or N)? ")
            if item_input:
                item_name = check_blank("Please enter the name of the"
                                        " item: ").title()
                count += 1
                item_list.append(item_name)
                price = float_checker("What is the price of the item: $")
                amount = float_checker(f"How many {unit}(s) is the item: ")
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
                    print(f"\nItem prices per {unit} "
                          f"(cheapest to most expensive):")
                    print("$", end="")
                    print(*price_unit_list, sep="\n$")
                    print()
                    print(f"The price per {unit} for each item is:")
                    item_data(price_unit_list, original_data_list, item_list,
                              unit)
                    budget_checker(budget, price_list, item_list,
                                   original_price_unit_list, unit)
                    print(f"Thank you for using the program {name}.")
                    exit()
                else:
                    print(f"Thank you for using the program {name}.")
                    exit()
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
    print("Item prices per unit (cheapest to most expensive):")
    print("$", end="")
    print(*price_unit_list, sep="\n$")
    print()
    print(f"The price per {unit} for each item is:")
    print(f"{item_list[0]}: ${original_data_list[0][0]:.2f} per {unit}")
    print(f"{item_list[1]}: ${original_data_list[1][0]:.2f} per {unit}")
    print(f"{item_list[2]}: ${original_data_list[2][0]:.2f} per {unit}")
    print(f"{item_list[3]}: ${original_data_list[3][0]:.2f} per {unit}")
    print(f"{item_list[4]}: ${original_data_list[4][0]:.2f} per {unit}")
    budget_checker(budget, price_list, item_list, original_price_unit_list,
                   unit)
    print(f"Thank you for using the program {name}.")
