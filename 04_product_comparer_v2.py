""" Component 4 version 2 of Price Comparer
In this version, I will make sure that the user enters a valid number so that
the program will not crash, and I will also make sure that the program does not
crash if the user enters a string instead of a number or there is no input.
by Sun Woo Yi
27/05/2022
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


price_list = []
amount_list = []

# Getting the price and amount of five items.
for i in range(5):
    price = float_checker("What is the price of the item: ")
    amount = float_checker("How many units is the item: ")
    price_list.append(price)
    amount_list.append(amount)

for i in range(5):
    print(price_list[i], amount_list[i])
