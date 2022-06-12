"""This component provides the opportunity for new users to find out how the
program is supposed to work
"""


# Function containing instructions
def show_instructions():
    print("**** Price Comparer Instructions ****\n"
          "Instructions go here. They are brief but helpful.\n")


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

instructions = ""
while not instructions:
    instructions = not_blank("Would you like to read the instructions?: ").lower()
    instructions = (get_choice(instructions, valid_yes_no))

if instructions == "Y":
    show_instructions()

print("Program launches...")
