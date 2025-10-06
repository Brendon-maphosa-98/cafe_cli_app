# function to handle choice (menu and lists) selection and validation


def numbered_display(
    options, menu_name="options", start_index=1, reserve_zero_for_last=False
):
    """
    Generate a numbered list string from `options` for display.
    Parameters:
      options: list of strings or a dictionary of dictionaries. The items to be numbered and displayed.
        - Lists will be menu options in the form of a list of strings or menu items in the form of a list of strings (each string being an item).
        - Dictionaries will be key value pairs where the key is an order number and the value is a dictionary of order details. The last order will NEVER be reserved for 0.
      reserve_zero_for_last: If True, the last item is numbered 0 (for 'back' option). Note: This is only applicable for lists of menu options, not for dictionaries of orders or lists of items.
      start_index: The starting index for numbering (default is 1).
      menu_name: Name of the menu for display purposes (default is "options").
    Returns:
      A formatted string representing the numbered list, or a message if the list is empty.
    Raises:
      TypeError: If `options` is not a list or dictionary. and if `start_index` is not an integer.
    Side Effects:
      - None (pure function).
    Dependencies/Assumptions:
      - `options` is always going to be a list of strings or a dictionary provided by the developer.
      - `start_index` is always going to be an integer provided by the developer.
      - `reserve_zero_for_last` is always going to be a boolean provided by the developer.
      - `menu_name` is always going to be a string provided by the developer.
    """
    try:
        if not isinstance(options, (list, dict)):
            raise TypeError("Options must be a list or a dictionary.")
        if isinstance(start_index, float) or not isinstance(start_index, int):
            raise TypeError("Start index must be an integer.")
        if not isinstance(reserve_zero_for_last, bool):
            raise TypeError("reserve_zero_for_last must be a boolean.")
        if len(options) == 0:
            return f"No {menu_name} to display."
        if isinstance(options, list) and all(
            option.strip() == "" for option in options
        ):
            return f"No {menu_name} to display."
        if isinstance(options, dict) and all(not value for value in options.values()):
            return f"No {menu_name} to display."

        display_str = ""  # Accumulate the formatted list into a single string

        item_index = start_index

        if isinstance(options, list):
            for i, option in enumerate(options):
                if reserve_zero_for_last and i == len(options) - 1:
                    display_str += f"\n0. {option.strip()}"
                else:
                    display_str += f"{item_index}. {option.strip()}\n"
                    item_index += 1
        elif isinstance(options, dict):
            for key, value in options.items():
                display_str += f"Order {key} - "
                order_details = []
                for detail_key, detail_value in value.items():
                    order_details.append(f"{detail_key}: {detail_value}")
                display_str += ", ".join(order_details) + "\n"
        return (
            display_str.strip().title()
        )  # Return the complete formatted list string without trailing newline
    except Exception as e:
        return f"An error occurred while generating the list: {e}"


def choice_validator(user_input, options, allow_zero=False):
    """
    Validate user input against a list of options.
    parameters:
    user_input: str - the input provided by the user to validate. will always be a variable containing a string provided by the user. The developer will provide the variable name but not the value.
    options: list of strings or a dictionary of dictionaries. The items to be numbered and displayed.
        - Lists will be menu options in the form of a list of strings or menu items in the form of a list of strings (each string being an item).
        - Dictionaries will be key value pairs where the key is an order number and the value is a dictionary of order details.
    allow_zero: bool - if True, allows 0 as a valid input for going back or exiting. Default is False. will always be provided by developer not user.
    returns:
    True if the input is valid (within range of options or 0 if allowed), otherwise returns an error message string.
    raises:
    ValueError: if the input cannot be converted to an integer.
    Side Effects:
    None (pure function).
    Dependencies/Assumptions:
    - `user_input` is always going to be a string provided by the user.
    - `options` is always going to be a list of strings or a dictionary provided by the developer.
    - `allow_zero` is always going to be a boolean provided by the developer.
    Note: This function assumes that the options are presented to the user in a numbered format starting from 1,
    with 0 optionally reserved for a 'back' or 'exit' option if `allow_zero` is True.
    """
    try:
        stringint = int(user_input)
        if allow_zero and stringint == 0 and len(options) != 0:
            return True
        elif 1 <= stringint <= len(options):
            return True
        else:
            return "NOT_A_VALID_OPTION"
    except ValueError:
        return "NOT_A_NUMBER"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def list_selection_choice(
    options, prompt_message, allow_zero=False, start_index=1, menu_name="options"
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
    Returns:
      The user's valid selection as a string.
    Raises:
      None (handles invalid input internally).
    Side Effects:
      - Prints the numbered list and prompts to the console.
      - Prints error messages for invalid input.
    Dependencies/Assumptions:
      - `options` is always going to be a list of strings or a dictionary provided by the developer.
      - `prompt_message` is always going to be a string provided by the developer.
      - `allow_zero` is always going to be a boolean provided by the developer.
      - `start_index` is always going to be an integer provided by the developer.
      - `menu_name` is always going to be a string provided by the developer.
    """
    function_loop = 0
    while function_loop == 0:
        print(
            numbered_display(
                options, menu_name, start_index, reserve_zero_for_last=allow_zero
            )
        )
        user_input = input(f"\n{prompt_message}\n>>> ")
        selection_output = choice_validator(user_input, options, allow_zero=allow_zero)
        if selection_output == True:
            function_loop = 1
            return user_input
        else:
            print(f"\n{selection_output}\n\n")


# TO DO - create functions to view orders lists then either create new functions to validate and return the selected order index or modify the existing functions to handle orders lists
