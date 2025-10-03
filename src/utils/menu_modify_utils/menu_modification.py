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
def update_existing_item_in_list(list_to_modify, menu_name, output_fn=print):
    """
    Purpose: Update an existing item in the specified list.
    Parameters:
    - list_to_modify: list - the list containing items to be updated. will always be provided by developer not user.
    - menu_name: str - the name of the menu (e.g., "Products", "Couriers"). will always be provided by developer not user.
    - output_fn: print function - will always be the built-in print function. will print the output to the console or terminal for the user to see.
    Returns:
    - True if the item was successfully updated.
    - False if the list is empty and no update can be made.
    - None if no changes were made (e.g., user cancelled the operation or the new item already exists).
    Note: This function relies on user input for selecting and renaming items.
    Dependencies:
    - list_selection_choice: Function to handle user selection from the list. it will take care of displaying the list and validating user input (which item they want to update) until it is a valid input using other helper functions from menu_choice_selection.py file.
    so no invalid inputs can be expected here. it will return the index of the selected item as an integer.
    - user_prompt_for_new_item: Function to prompt the user for a new item name to update the selected item. it will handle input validation, empty input, and cancellation. it will return the new item name or None if the operation is cancelled.
    - add_new_item_to_list: Function to add the new item name from the user_prompt_for_new_item function to the list if it doesn't already exist in the list. it will return True if the item was added successfully, or False if the item already exists in the list.
    """
    if not list_to_modify:
        output_fn(f"The {menu_name} list is empty. Returning to {menu_name} menu.")
        return False
    selected_index = list_selection_choice(
        list_to_modify,
        "Please select the number of the item you want to update: ",
        menu_name,
    )
    output_fn(f"You have selected to update: {list_to_modify[selected_index]}")
    new_item_name = user_prompt_for_new_item(menu_name)
    update_outcome = add_new_item_to_list(menu_name, new_item_name, list_to_modify)
    if update_outcome:
        return update_outcome
    else:
        output_fn(f"No changes made to {menu_name} list.")
        return None


# TO DO: update docstring to reflect the changes made to the function

# TO DO: Create tests for update_existing_item_in_list function
# Tests should cover:
# - Updating an item in a non-empty list
# - Attempting to update an item in an empty list
# - Trying to update an item to a name that already exists in the list
# - Handling user cancellation during the update process
# - Handling invalid inputs during the selection and renaming process
