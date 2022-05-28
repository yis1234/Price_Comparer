""" Component 4 version 4 of Price Comparer
In this version, I will ask the user if they want to continue to enter items.
If they say yes, the code will carry on and if they say no, the code will
print the price per units and end.
by Sun Woo Yi
28/05/2022
"""


# a float checking function
def float_checker(question):
    global response
    valid = False
    while not valid:
        try:
            response = float(input(question))
            valid = True
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


price_list = []
amount_list = []
inputs = 0

# Getting the price and amount of five items.
for i in range(5):
    item_input = yes_no_response("Do you have an item to compare (Y or N)? ")
    if item_input:
        price = float_checker("What is the price of the item: ")
        amount = float_checker("How many units is the item: ")
        price_list.append(price)
        amount_list.append(amount)
        inputs += 1
    else:
        if inputs > 0:
            for i in range(len(price_list)):
                price_unit = price_list[i]/amount_list[i] # Calculating the price per unit.
                print(price_unit)
            print("Thank you for using the program.")
            exit()
        else:
            print("Thank you for using the program.")
            exit()


for i in range(5):
    price_unit = price_list[i]/amount_list[i] # Calculating the price per unit.
    print(price_unit)
print("Thank you for using the program.")

