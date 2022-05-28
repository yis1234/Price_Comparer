""" Component 4 version 3 of Price Comparer
In this version, I will calculate the price per unit for each item and then
will print out the price per unit.
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


price_list = []
amount_list = []

# Getting the price and amount of five items.
for i in range(5):
    price = float_checker("What is the price of the item: ")
    amount = float_checker("How many units is the item: ")
    price_list.append(price)
    amount_list.append(amount)

for i in range(5):
    price_unit = price_list[i]/amount_list[i] # Calculating the price per unit.
    print(price_unit)
