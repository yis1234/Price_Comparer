""" Component 2 of Price Comparer
This component is a new version of 02_comparer_loop_v4.
Printed the item list to show to the user what they had inserted and made sure
not to print the escape code as part of the list
by Sun Woo Yi
23/05/2022
"""

# initialize loop so that it runs at least once
item_list = []
count = 0
MAX_ENTRIES = 5

while "Xxx" not in item_list and count < MAX_ENTRIES:
    if MAX_ENTRIES - count > 1:
        print(f"\nYou have {MAX_ENTRIES - count} entries left.")
    else:
        # Warns the user there is only one entry left
        print(f"\n***** You have ONLY ONE entry left! *****")
    item_name = input("Please enter the name of the item or enter "
                      "'xxx' to quit: ").title()
    if item_name != "Xxx":
        count += 1  # don't want to include escape code in the count
    item_list.append(item_name)


if count < MAX_ENTRIES:
    print(f"\nYou have made {count} entries\nThere are still"
          f" {MAX_ENTRIES - count} entries available")
else:
    print(f"\nYou have made all the available entries")


if "Xxx" in item_list:
    item_list.remove("Xxx")
    print(item_list)
else:
    print(item_list)
