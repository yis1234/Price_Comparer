""" Component 4 version 2 of Price Comparer
In this version, I will make sure that the user enters a valid number so that
the program will not crash.
by Sun Woo Yi
27/05/2022
"""


# float checker
def float_checker(test):
    while True:
        try:
            float(test)
            return True
        except ValueError:
            return False


# Check for valid string
def string_checker(test):
    while True:
        to_test = test
        if to_test.isalpha():
            return True
        else:
            return False


amount_list = []
price_list = []
entry = 0

error = "Invalid entry. Must be the price of the item followed by the " \
        "amount of units of the item.\n"
result = ""
while result != "X" and entry != 5:
    result = input("Please enter the price of the item followed by the amount"
                   " of units of the item: ")
    if result == "X":
        break
    else:
        result = result.strip()
        result = result.split()
        result_1 = result[0]
        result_2 = result[-1]
        result_1 = float(result_1)
        result_2 = float(result_2)

        if len(result) < 2:
            print(error)
            continue

        elif float_checker(result_1) and float_checker(result_2):
            amount = result[-1]
            amount_list.append(amount)

            if float_checker(result_1):
                price = result[0]
                print(f"Item: ${price} and {amount} units")
                price_list.append(price)
                entry += 1
            else:
                print(error)
                continue

        else:
            print(error)
            continue

for i in range(5):
    print(f"${price_list[i]}, {amount_list[i]} units")
