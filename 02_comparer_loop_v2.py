""" Component 2 of Price Comparer
I chose test 1 as I believed that a function was not needed for the code and
thought that test 1 would be better to develop than test 2.
This component is a new version of 02_comparer_loop_testing1 which makes a loop
until 5 items have been entered or the escape code "xxx" is entered. In this
new version, I used if statements to print out the amount of items entered
after the user has entered an item name.
by Sun Woo Yi
05/05/2022
"""


# initialize loop so that it runs at least once
item_name = ""
count = 0
MAX_ENTRIES = 5

while item_name != "Xxx" and count != MAX_ENTRIES:
    # get details
    item_name = input("Please enter the name of the item: ").title()
    if item_name != "Xxx":
        count += 1
        print(f"You have {MAX_ENTRIES - count} entries left")
if count == MAX_ENTRIES:
    print("You have made all the available entries")
else:
    print(f"You have made {count} entries")
    print(f"There are still {MAX_ENTRIES - count} available")

