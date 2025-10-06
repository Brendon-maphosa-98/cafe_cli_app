# function to handle choice (menu and lists) selection and validation


def numbered_display(
    options, menu_name="options", start_index=1, reserve_zero_for_last=False
):
    """
    Generate a numbered list string from `options` for display.
    Parameters:
      options: List of strings or a dictionary to be displayed as a numbered list.
      reserve_zero_for_last: If True, the last item is numbered 0 (for 'back' option).
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
        if not isinstance(options, list):
            raise TypeError("Options must be a list.")
        if isinstance(start_index, float) or not isinstance(start_index, int):
            raise TypeError("Start index must be an integer.")
        if not isinstance(reserve_zero_for_last, bool):
            raise TypeError("reserve_zero_for_last must be a boolean.")
        if len(options) == 0:
            return f"No {menu_name} to display."
        if all(option.strip() == "" for option in options):
            return f"No {menu_name} to display."

        display_str = ""  # Accumulate the formatted list into a single string

        item_index = start_index

        for i, option in enumerate(options):
            if reserve_zero_for_last and i == len(options) - 1:
                display_str += f"\n0. {option.strip()}"
            else:
                display_str += f"{item_index}. {option.strip()}\n"
                item_index += 1

        return (
            display_str.strip().title()
        )  # Return the complete formatted list string without trailing newline
    except Exception as e:
        return f"An error occurred while generating the list: {e}"


def choice_validator(user_input, options, allow_zero=False):
    """
    Validate user input against available options from a numbered list. this is used in conjunction with numbered_display.
    user_input: str - the input provided by the user to validate. It will always be a string.
    options: list - the list of available options to validate against. this will always be a list of strings. will always be provided by developer not user.will always be a list of items or a selection of menu items in the form of a list of strings.
    allow_zero: bool - if True, allows 0 as a valid input for going back or exiting. Default is False. will always be provided by developer not user.
    Return the selected option index as an integer if valid,
    or an appropriate error message string if invalid.
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
    Display a menu of options, prompt the user for input, and validate the selection.
    Continuously prompt the user until they provide valid input.
    Return the user's valid selection as a string.
    parameters:
    options: list - the list of available options to display and select from. this will always be a list of strings. will always be provided by developer not user. will always be a list of items or a selection of menu items in the form of a list of strings.
    prompt_message: str - the message to display when prompting the user for input. will always be provided by developer not user.
    allow_zero: bool - if True, allows 0 as a valid input for going back or exiting. Default is False. will always be provided by developer not user.
    start_index: int - the starting index for numbering the options. Default is 1. will always be provided by developer not user.
    menu_name: str - the name of the menu for display purposes. Default is "options". will always be provided by developer not user.
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