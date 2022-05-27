""" Component 4 test 2 of Price Comparer
The second test of this component will take the price of the item and the
amount of units of the item and will print them both out and will use a for
statement to get five items. It will print the price and amount next to each
other.
by Sun Woo Yi
24/05/2022
"""

price = []
amount = []

# Getting the price and amount of five items.
for i in range(5):
    price.append(float(input("What is the price of the item: ")))
    amount.append(float(input("How many units is the item: ")))

for i in range(5):
    print(price[i], amount[i])
