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


# function to update an existing item in a list
def update_existing_item_in_list(list_to_modify, menu_name, output_fn=print):
    """
    Interactively update an item in `list_to_modify`.

    This function:
      1) Prompts the user to select an existing item (via `list_selection_choice`),
      2) Prompts for a new value (via `user_prompt_for_new_item`),
      3) Updates the selected item in-place and reports status via `output_fn`.

    Args:
      list_to_modify: Mutable sequence of strings to be updated in place.
      menu_name: Human-readable name of the list (e.g., "Products", "Couriers") used in prompts/messages.
      output_fn: Callable used to emit user-facing messages (defaults to built-in `print`).

    Returns:
      True: An item was successfully updated.
      False: The list was empty; nothing was updated.
      None: The user canceled during the new-value prompt (no changes applied).

    Side Effects:
      - Mutates `list_to_modify` in place when an update occurs.
      - Emits messages through `output_fn`.
      - Performs interactive prompts via helper functions.

    Dependencies/Assumptions:
      - `list_selection_choice(options, prompt, menu_name) -> int` returns a valid index for `list_to_modify`.
      - `user_prompt_for_new_item(menu_name) -> str | None` returns the new value or `None` to cancel.
    """
    if not list_to_modify:
        output_fn(f"The {menu_name} list is empty. Returning to {menu_name} menu.")
        return False
    selected_index = list_selection_choice(
        list_to_modify,
        "Please select the number of the item you want to update: ",
        menu_name,
    )
    output_fn(f"You have selected to update: {list_to_modify[int(selected_index)]}")  # type: ignore
    new_item_name = user_prompt_for_new_item(menu_name)
    if new_item_name is None:
        return new_item_name
    else:
        list_to_modify[int(selected_index)] = new_item_name  # type: ignore
        output_fn(f"{menu_name[:-1]} updated successfully to {new_item_name}.")
        return True


# function to delete an item from a list
def delete_item_from_list(list_to_modify, menu_name, output_fn=print):
    """Delete an item from `list_to_modify` after user selection.

    This function:
      1) Prompts the user to select an existing item (via `list_selection_choice`),
      2) Optionally cancels if no selection is made,
      3) Deletes the selected item from the list,
      4) Reports status via `output_fn`.

    Args:
      list_to_modify (list[str]): Mutable sequence of strings from which an item will be deleted.
      menu_name (str): Human-readable name of the list (e.g., "Products", "Couriers") used in prompts/messages.
      output_fn (Callable[[str], None], optional): Function used to emit user-facing messages.
        Defaults to built-in `print`.

    Returns:
      bool | None:
        True: An item was successfully deleted.
        False: The list was empty; nothing was deleted.
        None: The user canceled the operation (no changes applied).

    Side Effects:
      - Mutates `list_to_modify` in place by removing one element when deletion occurs.
      - Emits messages through `output_fn`.
      - Performs interactive prompts via helper functions.

    Dependencies/Assumptions:
      - `list_selection_choice(options, prompt, menu_name) -> int | None` returns either:
          * a valid index into `list_to_modify` (0-based), or
          * `None` to indicate user cancellation.
      - The `list_to_modify` is a list of strings.
      - The `menu_name` is a non-empty string that will always be provided by the developer, not the user and will be a plural noun (e.g., "Products", "Couriers","Orders").
    """
    if not list_to_modify:
        output_fn(f"The {menu_name} list is empty. Returning to {menu_name} menu.")
        return False
    selected_index = list_selection_choice(
        list_to_modify,
        "Please select the number of the item you want to delete: ",
        menu_name,
    )
    if selected_index is None:
        return selected_index
    else:
        output_fn(f"You have selected to delete: {list_to_modify[int(selected_index)]}")  # type: ignore
        list_to_modify.pop(list_to_modify[int(selected_index)])  # type: ignore
        output_fn(f"{menu_name[:-1]} deleted successfully.")
        return True
