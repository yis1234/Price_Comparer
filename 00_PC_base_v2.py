""" Added 02_comparer_loop_v4 to the 00_PC_base_v1.
"""


def check_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("Error – please enter a name.")
        else:
            return response


# initialize comparer loop so that it runs at least once
item_name = ""
count = 0
MAX_ENTRIES = 5


# main routine
name = check_blank("What is your name? ")
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


