# functions to add new items to a list
import os


def create_new_item(menu_name):
    """
    Prompt the user to enter a new item name.
    Returns the entered item name as a string.
    """
    loop = 0
    try:
        while loop == 0:
            new_item = (
                input(f"Enter the name of the new {menu_name[:-1]}, or <Enter> to cancel: ")
                .strip()
                .capitalize()
            )  # Remove leading/trailing whitespace and capitalize
            if not new_item:
                print("No input provided. would you like to try again? or return to the previous menu?")
                choice = input("1. Try again\n2. Return to previous menu\n>>> ")
                if choice == "1":
                    os.system("sleep 2")
                    os.system("clear")
                    continue
                elif choice == "2":
                    loop = 1
                    return None
                else:
                    print("Invalid input, please try again.")
                    loop = 1
                    return None
            else:
                loop = 1
                return new_item
    except KeyboardInterrupt:
        print("\nInput cancelled by user.")
        return None
    except EOFError:
        print("\nInput terminated unexpectedly.")
        return None
