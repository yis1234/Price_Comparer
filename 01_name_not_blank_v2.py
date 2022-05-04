""" Component 1 version 2 of Price Comparer
This component is a new version of 01_name_not_blank_v1 checks if the name
inputted by the user is not blank and the error message is the 2nd parameter in
the function
by Sun Woo Yi
03/05/2022
"""


def check_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# main routine
name = check_blank("What is your name? ", "Error – you must enter a name.")

