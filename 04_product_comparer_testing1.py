""" Component 4 test 1 of Price Comparer
The first test of this component will take the price of the item and the
amount of units of the item and will print them both out.
by Sun Woo Yi
23/05/2022
"""

price = []
amount = []

# Getting the price and amount of six items.
for i in range(5):
    price.append(float(input("What is the price of the item: ")))
    amount.append(float(input("How many units is the item: ")))

for i in range(5):
    print(price[i], amount[i])
