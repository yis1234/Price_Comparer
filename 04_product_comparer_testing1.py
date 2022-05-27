""" Component 4 test 1 of Price Comparer
The first test of this component will take the price of the item and the
amount of units of the item and will print them both out and will use the
while loop to get five items. It will print out the price and amount separately
by Sun Woo Yi
23/05/2022
"""

price = []
amount = []
question = 0

# Getting the price and amount of five items.
while question != 5:
    price.append(float(input("What is the price of the item: ")))
    amount.append(float(input("How many units is the item: ")))
    question += 1

print(price)
print(amount)
