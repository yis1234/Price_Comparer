""" Component 2 test 1 of Price Comparer
This component makes a loop until 5 items have been entered or the escape code
"xxx" is entered
by Sun Woo Yi
05/05/2022
"""


item_name = ""
count = 0
MAX_ENTRIES = 5

while item_name != "Xxx" and count != MAX_ENTRIES:
    # get details
    item_name = input("Please enter the name of the item: ").title()
    count += 1
