""" Added 01_name_not_blank_v3 to this base code
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
