""" Based on 03_measurement_units_v2, this program makes the function more
flexible by allowing reference numbers to be entered to choose the unit.
by Sun Woo Yi
10/05/2022
"""


def check_measurement_units(question, valid_choices):
    unit_choice_error = "Sorry that is not a valid unit"

    choice = input(question).lower()
    for unit in valid_choices:
        if choice in unit:
            choice = unit[0].title()
            return choice

    print(unit_choice_error)
    return check_measurement_units(question, valid_choices)


# Main routine
# temporary input statement – during development
ask_for_unit = "Please enter the measurement unit: "
valid_units = [["kilogram", "kg", "1"], ["litre", "l", "2"]]
for test in range(6):
    print(f"You chose {check_measurement_units(ask_for_unit, valid_units)} "
          f"as the unit")
