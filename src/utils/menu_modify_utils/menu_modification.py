from src.utils.menu_utils.menu_choice_selection import list_selection_choice

# functions modifying lists


# helper function to prompt user for new item name
def user_prompt_for_new_item(menu_name, input_fn=input, output_fn=print):
    """
    Prompt the user to enter a new item name.
    Returns the entered item name as a string, or None if cancelled.
    menu_name: str - the name of the menu (e.g., "items", "couriers")
    """
    try:
        while True:
            new_item = (
                input_fn(f"Enter the name of the new {menu_name[:-1]}: ")
                .strip()
                .title()
            )
            inner_loop = 0
            while inner_loop == 0:
                if not new_item:
                    choice = input_fn(
                        "No input provided. Press 1 to try again or 2 to cancel: "
                    )
                    if choice == "2":
                        output_fn(
                            f"Operation cancelled. Returning to {menu_name} menu."
                        )
                        return None
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                else:
                    return new_item
    except KeyboardInterrupt:
        output_fn(f"\nOperation cancelled. Returning to {menu_name} menu.")
        return None
    except StopIteration:
        output_fn(f"\nNo more input available. Returning to {menu_name} menu.")
        return None
    except Exception as e:
        output_fn(
            f"\nAn unexpected error occurred: {e}. Returning to {menu_name} menu."
        )
        return None


# function to add a new item to a list


def add_new_item_to_list(menu_name, new_item, list_to_modify, output_fn=print):
    """
    Add a new item to the specified list and confirm the addition if it doesn't already exist in the list.
    menu_name: str - the name of the menu (e.g., "Products", "Couriers"). will always be provided by developer not user.
    new_item: str - the name of the new item to add. will be provided by user. The parameter will always be a string and will be a global variable in the respective file where this function is called and that variable will always be assigned the return value of user_prompt_for_new_item function.
    list_to_modify: list - the list to which the new item will be added to. will always be provided by developer not user.
    output_fn: print function, will always be provided by developer not user. will always be the built-in print function. will print the output to the console or terminal for the user to see.
    """
    if new_item not in list_to_modify:
        list_to_modify.append(new_item)
        output_fn(f"{new_item} added successfully to {menu_name} list.")
        return True
    else:
        output_fn(f"{new_item} already exists in {menu_name} list.")
        return False

# TO DO: Create tests for add_new_item_to_list function following addition of return statements in the if and else blocks

# function to update an existing item in a list
def update_existing_item_in_list(list_to_modify, menu_name):
    """
    Update an existing item in the specified list.
    menu_name: str - the name of the menu (e.g., "Products", "Couriers"). will always be provided by developer not user.
    list_to_modify: list - the list in which the item will be updated. will always be provided by developer not user.
    first check if the list is empty, if it is empty, print a message and return to the menu.
    Then display the list with index numbers starting from 1.
    output_fn: print function, will always be provided by developer not user. will always be the built-in print function. will print the output to the console or terminal for the user to see.
    """
    if not list_to_modify:
        print(f"The {menu_name} list is empty. Returning to {menu_name} menu.")
        return None
    selected_index = list_selection_choice(
        list_to_modify,
        "Please select the number of the item you want to update: ",
        menu_name,
    )
    print(f"You have selected to update: {list_to_modify[selected_index]}")
    new_item_name = user_prompt_for_new_item(menu_name)
    update_outcome = add_new_item_to_list(
        menu_name, new_item_name, list_to_modify
    )
    if update_outcome:
        return update_outcome
    else:
        print(f"No changes made to {menu_name} list.")
        return None


# TO DO: Create tests for update_existing_item_in_list function
# Tests should cover:
# - Updating an item in a non-empty list
# - Attempting to update an item in an empty list
# - Trying to update an item to a name that already exists in the list
# - Handling user cancellation during the update process
# - Handling invalid inputs during the selection and renaming process
