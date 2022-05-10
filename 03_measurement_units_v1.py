""" Component 3 of Price Comparer
This component will check if the measurement units inserted by the user
are valid
by Sun Woo Yi
09/05/2022
"""


def check_measurement_units():
    unit_choice_error = "Sorry that is not a valid unit"
    valid_units = [["kilogram", "kg"], ["litre", "l"]]
    unit_choice = input("Please enter the measurement unit: ").lower()
    for unit in valid_units:
        if unit_choice in unit:
            unit_choice = unit[0].title()
            return unit_choice

    print(unit_choice_error)
    return check_measurement_units()


# Main routine
# temporary input statement – during development
for test in range(4):
    print(f"Unit: {check_measurement_units()}")
