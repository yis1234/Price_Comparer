""" Component 2 of Price Comparer
This component is a new version of 02_comparer_loop_v2.
Further, improved the emphasis - drawing the user's attention when there is
only one available seat left, and I made a print statement to let the user know
that the escape key is "xxx"
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
        # Warns the user there is only one seat left
        print(f"\n***** You have ONLY ONE entry left! *****")
    # get details
    item_name = input("Please enter the name of the item or enter "
                      "'xxx' to quit: ").title()
    if item_name != "Xxx":
        count += 1  # don't want to include escape code in the count

if count < MAX_ENTRIES:
    print(f"\nYou have made {count} entries\nThere are still"
          f" {MAX_ENTRIES - count} entries available")
else:
    print(f"\nYou have made all the available entries")


