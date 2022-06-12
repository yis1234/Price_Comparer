""" It will check if the price of the item is larger than the budget and if so,
it will print out the items that are affordable and the items that are not.
I will be using a list to store the item prices. It wil also allow the user to
input the price of the item.
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


item_price_list = []
item_input = 0
while item_input != 5:
    item_price = float_checker("What is the price of the item: ")
    item_price_list.append(item_price)
    item_input += 1
budget = float_checker("What is your budget: ")
for i in item_price_list:
    if i > budget:
        print(f"Item {item_price_list.index(i)+1}: is too expensive.")
    else:
        print(f"Item {item_price_list.index(i)+1}: is affordable.")
