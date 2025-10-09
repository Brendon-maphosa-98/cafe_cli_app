import re

from src.utils.menu_utils.menu_choice_selection import list_selection_choice

# functions modifying lists


# helper function to prompt user for new item name
def user_prompt_for_new_item(menu_name, input_fn=input, output_fn=print):
    """
    This function:
        1) Prompts the user to enter the name of a new item (product or courier).
        2) Validates that the input is not empty.
    Returns:
        The name of the new item as a string if valid input is provided.
        None if the operation is cancelled or invalid input is given.
    Args:
        menu_name: Name of the menu for display purposes (e.g., "Products", "Couriers").
        input_fn: Function to use for input (default is built-in input).
        output_fn: Function to use for output (default is built-in print).
    side effects:
        Prompts the user for input and prints messages to the console.
    dependencies/assumptions:
        The function assumes that the input_fn and output_fn are callable and behave like the built-in input and print functions.
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
                        raise KeyboardInterrupt
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                else:
                    return new_item
    except KeyboardInterrupt:
        output_fn(f"\nOperation cancelled. Returning to {menu_name} menu.")
    except StopIteration:
        output_fn(f"\nNo more input available. Returning to {menu_name} menu.")
    except Exception as e:
        output_fn(
            f"\nAn unexpected error occurred: {e}. Returning to {menu_name} menu."
        )


# helper function to prompt user for order customer first and last name
def user_prompt_for_order_customer_name(input_fn=input, output_fn=print):
    """
    This function:
        1) Prompts the user to enter the first name and last name of the customer for the order.
        2) Validates that both names are provided and not empty.
        3) Validates that the names contain only alphabetic characters.
    Returns:
        A tuple containing the first name and last name as strings if valid input is provided.
        None if the operation is cancelled or invalid input is given.
    Args:
        input_fn: Function to use for input (default is built-in input).
        output_fn: Function to use for output (default is built-in print).
    side effects:
        Prompts the user for input and prints messages to the console.
    dependencies/assumptions:
        The function assumes that the input_fn and output_fn are callable and behave like the built-in input and print functions.
    """
    try:
        while True:
            first_name = input_fn("Enter the customer's first name: ").strip().title()
            last_name = input_fn("Enter the customer's last name: ").strip().title()
            inner_loop = 0
            while inner_loop == 0:
                # Case: either name missing
                if not first_name or not last_name:
                    choice = input_fn(
                        "First name and last name cannot be empty. Press 1 to try again or 2 to cancel: "
                    )
                    if choice == "2":
                        raise KeyboardInterrupt
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                # Case: invalid characters (now allow letters, hyphens and apostrophes)
                elif not re.match(r"^[A-Za-z'-]+$", first_name) or not re.match(
                    r"^[A-Za-z'-]+$", last_name
                ):
                    choice = input_fn(
                        "Names must contain only alphabetic characters, hyphens or apostrophes. Press 1 to try again or 2 to cancel: "
                    )
                    if choice == "2":
                        raise KeyboardInterrupt
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                else:
                    return first_name, last_name
    except KeyboardInterrupt:
        output_fn("Operation cancelled. Returning to Orders menu.")
    except StopIteration:
        output_fn("No more input available. Returning to Orders menu.")
    except Exception as e:
        output_fn(f"An unexpected error occurred: {e}. Returning to Orders menu.")


# helper function to prompt user for customer address
def user_prompt_for_order_customer_address(input_fn=input, output_fn=print):
    """
    This function:
        1) Prompts the user to enter the address of the customer for the order.
        2) Validates that the address is provided and not empty.
        3: Uses regex to validate the address format and ensure it contains valid characters.
    Returns:
        The address as a string if valid input is provided.
        None if the operation is cancelled or invalid input is given.
    Args:
        input_fn: Function to use for input (default is built-in input).
        output_fn: Function to use for output (default is built-in print).
    side effects:
        Prompts the user for input and prints messages to the console.
    dependencies/assumptions:
        The function assumes that the input_fn and output_fn are callable and behave like the built-in input and print functions.
    """
    UK_address_pattern = re.compile(
        r"^\d+\s[A-Za-z0-9\s,'-]+,\s[A-Za-z\s'-]+,\s[A-Z]{1,2}\d{1,2}\s?\d[A-Z]{2}$"
    )  # Simplified UK address regex pattern. This pattern may not cover all valid UK addresses but serves as a basic validation.
    try:
        while True:
            number_and_street = (
                input_fn("Enter the customer's street address (e.g., '123 Main St'): ")
                .strip()
                .title()
            )
            city = (
                input_fn("Enter the customer's city (e.g., 'London'): ").strip().title()
            )
            postcode = (
                input_fn("Enter the customer's postcode (e.g., 'SW1A 1AA'): ")
                .strip()
                .upper()
            )
            address = f"{number_and_street}, {city}, {postcode}"
            inner_loop = 0
            while inner_loop == 0:
                # Case: address missing
                if not number_and_street or not city or not postcode:
                    choice = input_fn(
                        "Address fields cannot be empty. Press 1 to try again or 2 to cancel: "
                    )
                    if choice == "2":
                        raise KeyboardInterrupt
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                # Case: invalid address format
                elif not UK_address_pattern.match(address):
                    choice = input_fn(
                        "Address format is invalid. Ensure it includes street, city, and postcode, uses valid characters, is a UK address and follows the format '123 Main St, London, SW1A 1AA'.\n\n Press 1 to try again or 2 to cancel: "
                    )
                    if choice == "2":
                        raise KeyboardInterrupt
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                else:
                    return address
    except KeyboardInterrupt:
        output_fn("Operation cancelled. Returning to Orders menu.")

    except StopIteration:
        output_fn("No more input available. Returning to Orders menu.")

    except Exception as e:
        output_fn(f"An unexpected error occurred: {e}. Returning to Orders menu.")


# helper function to prompt user for customer phone number


def user_prompt_for_order_customer_phone(input_fn=input, output_fn=print):
    """
    This function:
        1) Prompts the user to enter the phone number of the customer for the order.
        2) Validates that the phone number is provided and not empty.
        3) Validates that the phone number contains only digits and is of a reasonable length (7 to 15 digits).
    Returns:
        The phone number as a string if valid input is provided.
        None if the operation is cancelled or invalid input is given.
    Args:
        input_fn: Function to use for input (default is built-in input).
        output_fn: Function to use for output (default is built-in print).
    side effects:
        Prompts the user for input and prints messages to the console
    dependencies/assumptions:
        The function assumes that the input_fn and output_fn are callable and behave like the built-in input and print functions.
    """
    Uk_phone_pattern = re.compile(
        r"^07\d{9}$"
    )  # UK mobile number regex pattern. This pattern may not cover all valid UK phone numbers but serves as a basic validation.
    invalid_format_message = "Invalid phone number. Please ensure the number meets these rules:\nMust start with '07'\nMust be 11 digits long\nNo spaces, symbols, or letters\nExample of valid format: 07123456789"
    try:
        while True:
            phone_number = input_fn(
                "Enter the customer's phone number (digits only): "
            ).strip()
            inner_loop = 0
            while inner_loop == 0:
                # Case: phone number missing
                if not phone_number:
                    choice = input_fn(
                        "Phone number cannot be empty. Press 1 to try again or 2 to cancel: "
                    )
                    if choice == "2":
                        raise KeyboardInterrupt
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                # Case: invalid characters (now allow only digits, length between 7 and 15)
                elif not re.match(Uk_phone_pattern, phone_number):
                    choice = input_fn(
                        f"{invalid_format_message}\n\nPress 1 to try again or 2 to cancel: "
                    )
                    if choice == "2":
                        raise KeyboardInterrupt
                    elif choice == "1":
                        inner_loop = 1  # Break inner loop to re-prompt for input
                    else:
                        output_fn("Invalid choice.")
                        inner_loop = 0  # Stay in the inner loop
                else:
                    return phone_number
    except KeyboardInterrupt:
        output_fn("\nOperation cancelled. Returning to Orders menu.")
    except StopIteration:
        output_fn("\nNo more input available. Returning to Orders menu.")
    except Exception as e:
        output_fn(f"\nAn unexpected error occurred: {e}. Returning to Orders menu.")


# helper function to prompt user to select an item/items from the products or couriers list to add to an order


def user_prompt_for_items_selection(
    options,
    prompt_message,
    menu_name="options",
    input_fn=input,
    output_fn=print,
):
    """
    Display a numbered list of options and prompt the user to make a selection.
    Parameters:
      options: list of strings or a dictionary of dictionaries. The items to be numbered and displayed.
        - Lists will be menu options in the form of a list of strings or menu items in the form of a list of strings (each string being an item).
        - Dictionaries will be key value pairs where the key is an order number and the value is a dictionary of order details. The last order will NEVER be reserved for 0.
      prompt_message: The message to display when prompting the user for input.
      allow_zero: If True, allows 0 as a valid input for going back or exiting (default is False).
      start_index: The starting index for numbering (default is 1).
      menu_name: Name of the menu for display purposes (default is "options").
      input_fn: Function to use for input (default is built-in input).
      output_fn: Function to use for output (default is built-in print).
    Returns:
      The user's valid selection as a string.
      None if the operation is cancelled.
    Raises:
      None (handles invalid input internally).
    Side Effects:
      - Prints the numbered list and prompts to the console.
      - Prints error messages for invalid input.
      - Prompts the user for input and prints messages to the console.
    Dependencies/Assumptions:
      - `options` is always going to be a list of strings or a dictionary provided by the developer.
      - `prompt_message` is always going to be a string provided by the developer.
      - `allow_zero` is always going to be a boolean provided by the developer.
      - `start_index` is always going to be an integer provided by the developer.
      - `menu_name` is always going to be a string provided by the developer.
      - `input_fn` and `output_fn` are callable and behave like the built-in input and print functions.
      - `list_selection_choice(options, prompt, allow_zero, start_index, menu_name) -> str` returns a valid selection or None if cancelled.
    """
    function_loop = 0
    compiled_products = []
    while function_loop == 0:
        selected_index = list_selection_choice(
            options,
            prompt_message,
            menu_name=menu_name,
        )
        if selected_index is not None and menu_name == "Couriers":
            function_loop = 1
            return selected_index
        elif selected_index is not None and menu_name == "Products":
            more_item_question = input_fn(
                f"{options[int(selected_index)-1]} selected, would you like to select another product? press 1 for yes or 2 for no: "
            )
            if more_item_question == "1":
                compiled_products.append(selected_index)
                function_loop = 0
            elif more_item_question == "2":
                compiled_products.append(selected_index)
                function_loop = 1
                return compiled_products
        else:
            error_next_step = input_fn(
                f"{selected_index}, please try again or press 0 to cancel.\n\n"
            )
            if error_next_step == "0":
                output_fn(f"Operation cancelled. Returning to {menu_name} menu.")
                return None
            else:
                function_loop = 0
    ## REFACTOR NOTE: Go through all other functions in codebase and refactor for the following before continuing with the above function:
    # - ensure consistent naming conventions for variables and functions across the codebase
    # - ensure consistent return types (e.g., always return a list for multiple selections, even if it's a single item)
    # - ensure consistent formatting and style across the codebase
    # - add type hints for better clarity and maintainability
    # - add more detailed docstrings for better understanding of function purposes and behaviors
    # - when above is done modify the tests for the functions that were modified to ensure they still pass and cover edge cases and unhappy cases
    # - then come back to this function and refactor it again if needed
    # - finally, add tests for this function to ensure it works as expected and covers edge cases and unhappy cases.


# function to add a new item to a list


def add_new_item_to_collection(new_item, dict_to_modify):
    """
    This function:
        1) Checks if `new_item` is already in `dict_to_modify`.
        2) If not present, appends `new_item` to `dict_to_modify and returns True.
        3) If already present, does not modify the list and returns False.
    Args:
      new_item: str - the item to be added to the list. will be a variable containing a string provided by the user via prompt outside this function and passed to this function by the developer.
      dict_to_modify: dict - the dictionary to which the new item will be added. will be a variable containing a dictionary provided by the developer.
    Returns:
      True: The item was successfully added.
      False: The item already exists in the list; no changes were made.
    Side Effects:
      - Mutates `dict_to_modify` in place if the item is added.
    assumptions/Dependencies:
      - `new_item` is a non-empty string provided by the user via prompt outside this function and passed to this function by the developer.
      - `dict_to_modify` is a mutable dictionary provided by the developer.
    """
    try:
        if new_item in dict_to_modify.values():
            return False
        else:
            new_key = (
                max(dict_to_modify.keys(), default=0) + 1
            )  # Get next available key
            dict_to_modify[new_key] = new_item
            return True
    except Exception as e:
        print(f"An error occurred while adding the item: {e}. No changes made.")
        return False


# function to update an existing item in a list
def update_existing_item_in_list(dict_to_modify, menu_name):
    """
    Interactively update an item in `dict_to_modify`.

    This function:
      1) Prompts the user to select an existing item (via `list_selection_choice`),
      2) Prompts for a new value (via `user_prompt_for_new_item`),
      3) Updates the selected item in-place.

    Args:
      dict_to_modify: dict - dictionary of either products or couriers to be updated in place.
      menu_name: Human-readable name of the contents of the dictionary ("Products", "Couriers").

    Returns:
      True: An item was successfully updated.
      False: The list was empty; nothing was updated.
      None: The user canceled during the new-value prompt (no changes applied).

    Side Effects:
      - Mutates `dict_to_modify` in place when an update occurs.
      - Performs interactive prompts via helper functions.

    Dependencies/Assumptions:
      - `list_selection_choice(options, prompt, menu_name) -> int` returns a valid index for `dict_to_modify`.
      - `user_prompt_for_new_item(menu_name) -> str | None` returns the new value or `None` to cancel.
    """
    if not dict_to_modify:
        return False
    selected_index = list_selection_choice(
        dict_to_modify,
        "Please select the number of the item you want to update: ",
        menu_name,
    )
    new_item_name = user_prompt_for_new_item(menu_name)
    if new_item_name is None:
        return new_item_name
    else:
        # Update the selected item in the dictionary
        dict_to_modify[int(selected_index)] = new_item_name  # type: ignore
        return True


# function to delete an item from a list
def delete_item_from_list(dict_to_modify, user_input, menu_name, output_fn=print):
    """Delete an item from `dict_to_modify` after user selection.

    This function:
      1) Prompts the user to select an existing item (via `list_selection_choice`),
      2) Optionally cancels if no selection is made,
      3) Deletes the selected item from the dictionary.
      4) Reports status via `output_fn`.

    Args:
      dict_to_modify: dict - dictionary of either products or couriers to be modified in place.
      menu_name: Human-readable name of the contents of the dictionary ("Products", "Couriers").
      output_fn (Callable[[str], None], optional): Function used to emit user-facing messages.
        Defaults to built-in `print`.

    Returns:
      bool | None:
        True: An item was successfully deleted.
        False: The list was empty; nothing was deleted.
        None: The user canceled the operation (no changes applied).

    Side Effects:
      - Mutates `dict_to_modify` in place by removing one element when deletion occurs.
      - Emits messages through `output_fn`.
      - Performs interactive prompts via helper functions.

    Dependencies/Assumptions:
      - `list_selection_choice(options, prompt, menu_name) -> int | None` returns either:
          * a valid index into `dict_to_modify` (0-based), or
          * `None` to indicate user cancellation.
      - The `dict_to_modify` is a mutable dictionary provided by the developer.
      - The `menu_name` is a non-empty string that will always be provided by the developer, not the user and will be a plural noun (e.g., "Products", "Couriers").
    """
    try:
        if not dict_to_modify:
            output_fn(f"The {menu_name} list is empty. Nothing to delete.")
            return False
        selected_index = list_selection_choice(
            dict_to_modify,
            user_input,
            menu_name,
        )
        if selected_index is None:
            output_fn(f"Operation cancelled. Returning to {menu_name} menu.")
        else:
            deleted_item = dict_to_modify.pop(int(selected_index))
            output_fn(f"{deleted_item} has been deleted from the {menu_name} list.")
            return True
    except Exception as e:
        output_fn(f"An error occurred while deleting the item: {e}. No changes made.")
