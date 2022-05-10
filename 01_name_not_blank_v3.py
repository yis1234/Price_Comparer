""" Component 1 version 3 of Price Comparer
This component is a new version of 01_name_not_blank_v2 checks if the name
inputted by the user is not blank and uses the .alpha() method so that spaces
won't be accepted and the program will only accept letters.
by Sun Woo Yi
03/05/2022
"""


def check_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("Error – please enter a name.")
        else:
            return response


# main routine
name = check_blank("What is your name? ")
