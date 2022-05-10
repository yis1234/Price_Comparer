""" Component 2 of Price Comparer
This component is a new version of 02_comparer_loop_v2. In this version
checks to see if there is only ONE ticket left and, if so, produce a more
appropriately worded print statement. Also spaces out the print statements.
by Sun Woo Yi
06/05/2022
"""


# initialize loop so that it runs at least once
item_name = ""
count = 0
MAX_ENTRIES = 5

while item_name != "Xxx" and count < MAX_ENTRIES:
    if MAX_ENTRIES - count > 1:
        print(f"\nYou have {MAX_ENTRIES - count} entries left.")
    else:
        print(f"\nYou have ONLY ONE entry left")
    # get details
    item_name = input("Please enter the name of the item: ").title()
    if item_name != "Xxx":
        count += 1

if count < MAX_ENTRIES:
    print(f"\nYou have made {count} entries\nThere are still"
          f" {MAX_ENTRIES - count} entries available")
else:
    print(f"\nYou have made all the available entries")

