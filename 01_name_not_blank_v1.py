""" Component 1 of Price Comparer
This component checks if the name inputted by the user is not blank
by Sun Woo Yi
03/05/2022
"""


def check_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("Error – you must enter a name.")
        else:
            return response


# main routine
name = check_blank("What is your name? ")
