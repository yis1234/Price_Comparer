"""This component is based on v1
Puts the component into its own function
This version includes actual instructions
"""


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = not_blank("Would you like to read the "
                                 "instructions?: ").lower()
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
    print("Program launches...")


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Checks that the ticket name is not blank
def not_blank(question):
    valid = ""
    while not valid:
        response = input(question).title()

        # If the name is blank, it shows this error message
        if not response.isalpha():
            print("\nYou can't include digits or leave this blank...")
        else:
            return response  # but if name is not blank, program continues


# Main Routine
# Valid options for any yes/no questions
valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)
