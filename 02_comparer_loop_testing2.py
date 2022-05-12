""" Component 2 test 2 of Price Comparer
This component makes a loop until 5 items have been entered or the escape code
"xxx" is entered. I made a new version of this component to test which code
out of 02_comaparer_loop_testing1.py and 02_comparer_loop_testing2.py is the
best. In this test I used a function to check if it would be better than the
first test.
by Sun Woo Yi
05/05/2022
"""


def input_items():
    # Initialize variables
    items = []
    item = ""
    # Loop until 5 items have been entered or the exit code "xxx" is entered
    while len(items) < 5 and item != "xxx":
        item = input("Please enter the name of the item: ")
        if item != "xxx":
            items.append(item)
    return items


input_items()
