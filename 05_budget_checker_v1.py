""" It will check if the price of the item is larger than the budget and if so,
it will print out the items that are affordable and the items that are not.
I will be using a list to store the item prices.
07/06/2022
by Sun Woo Yi
"""


# a float checking function. I took this function from the
# 04_product_comparer_v7.
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


item_price_list = [10, 5, 6, 3.99, 8]
budget = float_checker("What is your budget: ")
for i in item_price_list:
    if i > budget:
        print(f"Item {item_price_list.index(i)+1}: is too expensive.")
    else:
        print(f"Item {item_price_list.index(i)+1}: is affordable.")
