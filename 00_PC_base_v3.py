""" Added 03_measurement_units_v3 to the 00_PC_base_v2.
"""


def check_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("Error – please enter a name.")
        else:
            return response


def check_measurement_units(question, valid_choices):
    unit_choice_error = "Sorry that is not a valid unit"

    choice = input(question).lower()
    for unit in valid_choices:
        if choice in unit:
            choice = unit[0].title()
            return choice

    print(unit_choice_error)
    return check_measurement_units(question, valid_choices)


# initialize comparer loop so that it runs at least once
item_name = ""
count = 0
MAX_ENTRIES = 5


# Main routine
# TO get the name of the user
name = check_blank("What is your name? ")
# Getting the measurement units that are going to be used to compare different
# items
ask_for_unit = "Please enter the measurement unit: "
valid_units = [["kilogram", "kg", "1"], ["litre", "l", "2"]]
print(f"You chose {check_measurement_units(ask_for_unit, valid_units)} "
      f"as the unit")
# To get the name of the products that they are going to compare.
while item_name != "Xxx" and count < MAX_ENTRIES:
    if MAX_ENTRIES - count > 1:
        print(f"\nYou have {MAX_ENTRIES - count} entries left.")
    else:
        # Warns the user there is only one seat left
        print(f"\n***** You have ONLY ONE entry left! *****")
    # get details
    item_name = input("Please enter the name of the item or enter "
                      "'xxx' to quit: ").title()
    if item_name != "Xxx":
        count += 1  # don't want to include escape code in the count

if count < MAX_ENTRIES:
    print(f"\nYou have made {count} entries\nThere are still"
          f" {MAX_ENTRIES - count} entries available")
else:
    print(f"\nYou have made all the available entries")




